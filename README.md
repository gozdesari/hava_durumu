Gerçek Zamanlı Hava Durumu Veri Akışı Projesi

Proje Amacı:
Bu projenin amacı, gerçek zamanlı veri akışı sağlayan bir sistem geliştirmek ve bu sistemi bulut ortamında çalıştırmaktır. Projede IoT mantığı simüle edilerek hava durumu verileri çekilmiş, bu veriler WebSocket aracılığıyla bir sunucuya gönderilmiş ve AWS üzerinde işlenip saklanmıştır.

Kullanılan Teknolojiler:
Python
FastAPI
WebSocket
AWS EC2 (Sunucu)
AWS DynamoDB (Veritabanı)
boto3 (AWS bağlantısı)
Open-Meteo API (veri kaynağı)

Sistem Mimarisi:
Proje 3 ana bileşenden oluşmaktadır:

Producer (IoT Simülasyonu):
Sensör gibi davranır
Open-Meteo API üzerinden gerçek hava durumu verisi çeker
Veriyi JSON formatında WebSocket ile server’a gönderir

Server (FastAPI - EC2)

AWS EC2 üzerinde çalışır
WebSocket ile gelen verileri alır
Verileri işler (ortalama, maksimum sıcaklık vb.)
DynamoDB’ye kaydeder

Database (DynamoDB):
Veriler bulut ortamında saklanır
Gerçek zamanlı veri birikimi sağlanır

Veri Akışı:
Producer → WebSocket → FastAPI (EC2) → DynamoDB

Yapılan İşlemler:
Gerçek zamanlı veri akışı sağlandı
IoT cihazı simülasyonu gerçekleştirildi
WebSocket ile sürekli bağlantı kuruldu
Veriler AWS DynamoDB’ye kaydedildi
Ortalama ve maksimum sıcaklık hesaplandı
Yüksek sıcaklık durumunda uyarı sistemi eklendi

AWS Kullanımı:
EC2: Backend uygulamasını çalıştırmak için kullanıldı
DynamoDB: Verilerin saklanması için kullanıldı
IAM Role: EC2’nin DynamoDB’ye erişebilmesi için kullanıldı

Projeyi Çalıştırma:
1. Server’ı başlat

```bash
cd server
uvicorn main:app --host 0.0.0.0 --port 8000
```

2. Producer’ı çalıştır

```bash
cd producer
python producer.py
```

Notlar:
* Producer dosyasında WebSocket adresi EC2 public IP olacak şekilde ayarlanmalıdır.
* AWS tarafında DynamoDB tablolarının oluşturulmuş olması gerekmektedir.
* EC2 instance’a DynamoDB erişim yetkisi verilmelidir (IAM role).

Sonuç:
Bu projede gerçek zamanlı veri akışı, IoT simülasyonu ve bulut bilişim teknolojileri bir arada kullanılarak uçtan uca çalışan bir sistem geliştirilmiştir. Sistem, WebSocket ile veri iletimi, FastAPI ile işleme ve AWS ile bulut entegrasyonunu başarıyla gerçekleştirmektedir.



