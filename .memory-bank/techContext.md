# Teknoloji Bağlamı

- **Dil:** Python 3.x sürümlerine uyumlu.
- **Bağımlılıklar:** `pytesseract`, `Pillow`; `requirements.txt` içinde tanımlı ve `pip install -r requirements.txt` ile yükleniyor.
- **OCR motoru:** Sisteme Tesseract-OCR kurulmuş olmalı (Windows için UB-Mannheim sürümü önerilir). `--tesseract-cmd` ile özel binary yolunu göstermek mümkün.
- **Çalışma akışı:** `python main.py` çalıştığında script önce `input/` klasörünü tarar, desteklenen görselleri numaralı listede sunar ve seçilen görseli `pytesseract` ile işler.
- **Çıktı:** İlgili görselin satır adı `output/<gorsel_adi>.txt` olarak oluşturulur; `-o`/`--output` ile farklı bir dosya veya `--output-dir` ile başka klasör belirtilebilir.
- **Ortam:** Sanal ortam (virtualenv/venv/conda) kullanılmalı; bağımlılık değişiklikleri `requirements.txt` ile kontrol altında tutulmalı.
