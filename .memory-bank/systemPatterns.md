# Sistem Düzeni ve Veri Akışı

- Proje kökünde `main.py` ana uygulamayı çalıştıran script olarak yer alır. Terminalden `python main.py` komutuyla başlatılır.
- Görseller `input/` klasörüne kopyalanır; script bu klasördeki `.jpg`, `.jpeg` ve `.png` dosyalarını numaralı olarak listeler ve kullanıcı bir sayı, dosya adı veya tam yol girerek seçim yapabilir. Tam yol girilirse `input/` dışındaki dosyalar da kullanılabilir.
- OCR çıktısı varsayılan olarak `output/<gorsel_adi>.txt` dosyasına yazılır; `-o/--output` ile farklı bir dosya belirtilebilir veya `--output-dir` değiştirilebilir.
- `input/` ve `output/` klasörleri yoksa script onları otomatik oluşturur (`list_input_images` ve `save_output` adımlarında bu sağlanır).
- Kısa döngü: `input` klasörüne görsel koy → `python main.py` çalıştır → `output/<stem>.txt` dosyası oluşturulur ve durum yazılır.
- Bağımlılıklar `requirements.txt` içinde listelenmeli ve Python sanal ortamında yönetilmeli.
