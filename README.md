# Lenspy 📄➡️📝

**Lenspy** is a simple, lightweight, and open-source Python application that scans text within images and converts them into editable `.txt` files.

The application runs from the command line and requires minimal configuration.

## 🚀 Features

- **Format Support:** Supports `.jpg`, `.png`, and `.jpeg` formats.
- **Fast Output:** Saves text to the `output/` folder in a file-per-image structure.
- **Language Support:** Use any language supported by Tesseract.
- **Open Source:** Small, dependency-light codebase.

## 🛠️ Requirements

To run this project, install the following:

1. **Python 3.x**
2. **Tesseract-OCR Engine** — on Windows the UB-Mannheim build is recommended.

Windows users: download and install from the UB-Mannheim releases and note the installed path (for example `C:\Program Files\Tesseract-OCR\tesseract.exe`).

## 📦 Installation

1. Clone Lenspy and switch to the directory:

```powershell
git clone https://github.com/hazarute/lenspy.git
cd lenspy
```

2. Install Python dependencies:

```powershell
pip install -r requirements.txt
```

3. Make sure Tesseract is installed. If it's not on your PATH, run the script with `--tesseract-cmd` pointing to the binary.

## 💻 Usage

1. Create an `input/` folder (or use `--input-dir`) and place `.jpg`/`.jpeg`/`.png` files there.

2. Run the script:

```powershell
python main.py
```

3. The script lists images in `input/` by number; you can enter a number, filename, or full path.

4. By default output is written to `output/<image_name>.txt`. Use `-o/--output` to set a filename or `--output-dir` to change the folder.

5. Example: run with a custom Tesseract binary on Windows PowerShell:

```powershell
python main.py --tesseract-cmd "C:\Program Files\Tesseract-OCR\tesseract.exe" --lang eng
```

## 📂 Project Structure

```
lenspy/
├── main.py
├── README.md
├── requirements.txt
├── input/
└── output/
```

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Contributing

Contributions are welcome. Please open issues or pull requests on the GitHub repository. A basic `.gitignore` is recommended for local virtual environments (`venv/`) and Python cache files (`__pycache__/`, `*.pyc`).

## Contact

Hazar Ute — hazarute@gmail.com
Project Link: https://github.com/hazarute/lenspy

-----

## Türkçe — Lenspy

**Lenspy**, görsellerin içerisindeki metinleri tarayıp bunları düzenlenebilir `.txt` dosyasına dönüştüren basit, hafif ve açık kaynaklı bir Python uygulamasıdır.

Uygulama komut satırından çalışır ve minimum ayar gerektirir.

## 🚀 Özellikler

- **Format Desteği:** `.jpg`, `.png` ve `.jpeg` formatları desteklenir.
- **Hızlı Çıktı:** Her görsel için `output/` içinde bir `.txt` dosyası oluşturulur.
- **Dil Desteği:** Tesseract'ın desteklediği diller kullanılabilir.

## 🛠️ Gereksinimler

1. **Python 3.x**
2. **Tesseract-OCR Motoru** — Windows için UB-Mannheim sürümü önerilir.

Windows kullanıcıları: UB-Mannheim sürümünü indirip yükleyin ve kurulum yolunu not edin (ör: `C:\Program Files\Tesseract-OCR\tesseract.exe`).

## 📦 Kurulum

```powershell
git clone https://github.com/hazarute/lenspy.git
cd lenspy
pip install -r requirements.txt
```

## 💻 Kullanım

1. `input/` klasörünü oluşturun veya `--input-dir` ile farklı bir klasör belirtin ve görselleri buraya koyun.
2. Aşağıdaki komutla çalıştırın:

```powershell
python main.py
```

3. Script, `input/` içindeki görselleri numaralandırır; numara, dosya adı veya tam yol ile seçim yapabilirsiniz.

4. Varsayılan çıktı: `output/<gorsel_adi>.txt`. `-o/--output` veya `--output-dir` ile değiştirebilirsiniz.

5. Örnek (Windows PowerShell, özel Tesseract yolu belirtilmiş):

```powershell
python main.py --tesseract-cmd "C:\Program Files\Tesseract-OCR\tesseract.exe" --lang eng
```

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır — ayrıntılar için `LICENSE` dosyasına bakın.

## Katkı

Katkılar memnuniyetle kabul edilir. Lütfen GitHub üzerinde issue veya pull request açın. Lokal virtual environmentlar (`venv/`) ve Python cache dosyaları (`__pycache__/`, `*.pyc`) için `.gitignore` kullanılması önerilir.

## İletişim

Hazar Ute — hazarute@gmail.com
Proje Linki: https://github.com/hazarute/lenspy
