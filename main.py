"""Lenspy OCR command line interface."""

import argparse
import sys
from pathlib import Path
from typing import Optional

from PIL import Image, UnidentifiedImageError
import pytesseract

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
ALLOWED_EXTENSIONS = ", ".join(sorted(SUPPORTED_EXTENSIONS))
INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract editable text from an image using Lenspy."
    )
    parser.add_argument(
        "image",
        nargs="?",
        type=Path,
        help="Path to the image file to OCR (optional).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Explicit file that will receive the OCR text (overrides the output directory).",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=INPUT_DIR,
        help="Directory that stores the images to process (default: input/).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Directory where OCR results are written (default: output/).",
    )
    parser.add_argument(
        "-l",
        "--lang",
        default="eng",
        help="Tesseract language code (default: eng).",
    )
    parser.add_argument(
        "--tesseract-cmd",
        type=Path,
        help="Full path to the Tesseract binary if it is not on PATH.",
    )
    return parser.parse_args()


def list_input_images(input_dir: Path) -> list[Path]:
    input_dir.mkdir(parents=True, exist_ok=True)
    return sorted(
        path
        for path in input_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def prompt_for_image(input_dir: Path) -> Path:
    candidates = list_input_images(input_dir)
    if candidates:
        print("Images found in the input directory:")
        for index, candidate in enumerate(candidates, 1):
            print(f"  {index}. {candidate.name}")
        print("Enter the number of an image, its name, or a full path.")
    else:
        print(f"The input directory '{input_dir}' is empty. Add images with {ALLOWED_EXTENSIONS} extensions.")

    while True:
        raw = input("Enter the image name (or full path): ").strip()
        if not raw:
            print("Please provide a valid file path.")
            continue
        if raw.isdigit() and candidates:
            selection = int(raw)
            if 1 <= selection <= len(candidates):
                return validate_image_path(candidates[selection - 1])
            print(f"Selection {raw} is out of range. Please choose a number between 1 and {len(candidates)}.")
            continue
        candidate = Path(raw)
        if not candidate.is_absolute():
            candidate = input_dir / candidate
        try:
            return validate_image_path(candidate)
        except ValueError as exc:
            print(exc)


def validate_image_path(path: Path) -> Path:
    if not path.exists() or not path.is_file():
        raise ValueError(f"File not found: {path}")
    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported extension: {path.suffix}. Only {ALLOWED_EXTENSIONS}."
        )
    return path


def resolve_image_path(arg_image: Optional[Path], input_dir: Path) -> Path:
    if arg_image is not None:
        candidate = arg_image if arg_image.is_absolute() else input_dir / arg_image
        return validate_image_path(candidate)
    return prompt_for_image(input_dir)


def ocr_image(image_path: Path, lang: str) -> str:
    try:
        with Image.open(image_path) as image:
            return pytesseract.image_to_string(image, lang=lang)
    except UnidentifiedImageError as exc:
        raise RuntimeError(f"Unable to read the image: {exc}") from exc


def save_output(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"OCR result saved to '{path}'.")


def main() -> None:
    args = parse_args()
    if args.tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = str(args.tesseract_cmd)

    try:
        image_path = resolve_image_path(args.image, args.input_dir)
    except KeyboardInterrupt:
        print("Operation cancelled.", file=sys.stderr)
        sys.exit(0)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

    try:
        text = ocr_image(image_path, args.lang)
    except pytesseract.TesseractNotFoundError as exc:
        print(
            "Tesseract was not found. Please follow the installation steps in README.md.",
            file=sys.stderr,
        )
        print(exc, file=sys.stderr)
        sys.exit(1)
    except pytesseract.TesseractError as exc:
        print("An error occurred while running Tesseract:", file=sys.stderr)
        print(exc, file=sys.stderr)
        sys.exit(1)
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

    if not text.strip():
        print("OCR result is empty. Try a clearer or higher-resolution image.")

    output_target = args.output or (args.output_dir / f"{image_path.stem}.txt")
    save_output(output_target, text)


if __name__ == "__main__":
    main()
