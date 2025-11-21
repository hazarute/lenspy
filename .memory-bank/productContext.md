# Ürün Bağlamı

**Problem:** Görsellerdeki metni hızlıca çıkarmak isteyen kullanıcılar, genellikle fazla konfigürasyon, GUI bağımlılıkları ya da karmaşık workflowlarla karşılaşıyor.

**Çözüm:** Lenspy, tek komutla çalıştırılan ve özel bir GUI ya da ayar dosyası gerektirmeyen bir CLI OCR aracı sunuyor. `input/` klasörüne yerleştirilen `.jpg`, `.jpeg` veya `.png` dosyaları numaralı olarak listeleniyor; kullanıcı bir sayı, dosya adı veya tam yol girerek dosyayı seçebiliyor. Script, `pytesseract` kullanarak metni çıkarıyor ve varsayılan olarak `output/<gorsel_adi>.txt` dosyasına kaydediyor.

**Kullanıcı Deneyimi Hedefleri:**
- Ekstra konfigürasyon gerektirmeden `input/` ve `output/` klasörleriyle çalışsın.
- Görsele ulaşmak için basit bir numaralı seçim arayüzü sağlasın.
- Tesseract kurulumunu README üzerinden anlatıp, `requirements.txt` ile bağımlılıkları tek komutta yüklesin.
