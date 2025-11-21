# Lenspy 📄➡️📝

**Lenspy** is a simple, lightweight, and open-source Python application that scans text within images and converts them into editable `.txt` files.

The application runs from the command line and requires minimal configuration.

## 🚀 Features

  * **Format Support:** Supports `.jpg`, `.png`, and `.jpeg` formats.
  * **Fast Output:** Saves text to the `output/` folder within a file-based structure.
  * **Language Support:** You can use all languages supported by Tesseract.
  * **Open Source:** The code is clean and compatible with the standard Python library.

## 🛠️ Requirements

To run this project, the following software must be installed on your computer:

1.  **Python 3.x**
2.  **Tesseract-OCR Engine:** Download and install the [UB-Mannheim installer](https://github.com/UB-Mannheim/tesseract/wiki) for Windows; use package managers for Linux and Mac.

## 📦 Installation

1.  Clone Lenspy and switch to the directory:

    ```bash
    git clone https://github.com/username/Lenspy.git
    cd Lenspy
    ```

2.  Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  Ensure Tesseract is installed and added to your PATH, or provide the full path via `--tesseract-cmd`.

## 💻 Usage

1.  Create an `input/` folder (or use `--input-dir` if you prefer a different folder) and place the `.jpg`, `.jpeg`, or `.png` files to be OCR'd inside.

2.  Run the following command in the terminal:

    ```bash
    python main.py
    ```

3.  The script lists the images in the `input/` folder by number, then asks you to enter a number, filename, or full path.

4.  By default, the OCR output is written to `output/<image_name>.txt`. You can specify a custom file with `-o/--output` or use a different folder with `--output-dir`.

5.  You can set the Tesseract language with the `--lang` parameter or point to a custom binary with `--tesseract-cmd`.

## 📂 Project Structure

```
Lenspy/
├── main.py          # Script managing the OCR flow
├── README.md        # This documentation
├── requirements.txt # Pillow and pytesseract dependencies
├── input/           # Folder where images to be OCR'd are placed
└── output/          # .txt outputs generated for each image
```
## 📞 Contact

Hazar Ute - hazarute@gmail.com

Project Link: [https://github.com/hazarute/lenspy](https://github.com/hazarute/lenspy)

-----

**Lenspy**, görsellerin içerisindeki metinleri tarayıp bunları düzenlenebilir `.txt` dosyasına dönüştüren basit, hafif ve açık kaynaklı bir Python uygulamasıdır.

Uygulama komut satırından çalışır ve olabildiğince az ayar gerektirir.

## 🚀 Özellikler

* **Format Desteği:** `.jpg`, `.png` ve `.jpeg` formatlarını destekler.
* **Hızlı Çıktı:** Dosya bazlı bir yapı içinde `output/` klasörüne metin kaydeder.
* **Dil Desteği:** Tesseract’ın desteklediği tüm dilleri kullanabilirsiniz.
* **Açık Kaynak:** Kodun tamamı sade ve Python standart kütüphanesiyle uyumludur.

## 🛠️ Gereksinimler

Bu projeyi çalıştırmak için bilgisayarınızda şu yazılımlar bulunmalıdır:

1.  **Python 3.x**
2.  **Tesseract-OCR Motoru:** Windows için [UB-Mannheim installer](https://github.com/UB-Mannheim/tesseract/wiki) indirip kurun; Linux ve Mac için paket yöneticilerini kullanın.

## 📦 Kurulum

1.  Lenspy’ı klonlayın ve dizine geçin:
    ```bash
    git clone https://github.com/hazarute/lenspy.git
    cd Lenspy
    ```

2.  Gerekli Python paketlerini yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3.  Tesseract’ın kurulu ve PATH’e ekli olduğundan emin olun veya `--tesseract-cmd` ile tam yolu verin.

## 💻 Kullanım

1.  `input/` klasörünü oluşturun (veya farklı klasör kullanacaksanız `--input-dir`) ve OCR yapılacak `.jpg`, `.jpeg` veya `.png` dosyalarını buraya yerleştirin.
2.  Terminalden şu komutu çalıştırın:

    ```bash
    python main.py
    ```

3.  Script `input/` klasöründeki görselleri numaralı olarak listeler, ardından bir sayı, dosya adı veya tam yol girmenizi ister.
4.  OCR çıktısı varsayılan olarak `output/<gorsel_adi>.txt` dosyasına yazılır. `-o/--output` ile özel bir dosya belirtebilir, `--output-dir` ile farklı klasör kullanabilirsiniz.
5.  `--lang` parametresiyle Tesseract dilini ayarlayabilir, `--tesseract-cmd` ile özel binary gösterebilirsiniz.

## 📂 Proje Yapısı

```
Lenspy/
├── main.py          # OCR akışını yöneten script
├── README.md        # Bu dokümantasyon
├── requirements.txt # Pillow ve pytesseract bağımlılıkları
├── input/           # OCR yapılacak görsellerin yerleştirildiği klasör
└── output/          # Her görsel için oluşturulan .txt çıktılar
```

## 📞 İletişim

Hazar Ute - hazarute@gmail.com

Proje Linki: [https://github.com/hazarute/lenspy](https://github.com/hazarute/lenspy)