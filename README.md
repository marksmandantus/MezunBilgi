# Mezun Bilgi Sistemi

![Logo](https://example.com/logo.png)

Mezun Bilgi Sistemi, üniversite mezunlarının bilgilerini ve etkinliklere katılımını yöneten bir web uygulamasıdır.

## Kurulum

Bu proje için aşağıdaki adımları izleyerek kurulum yapabilirsiniz:

1. Öncelikle Python paketlerini yüklemek için terminale aşağıdaki komutu girin:

pip install -r requirements.txt


2. Veritabanını oluşturmak için terminale aşağıdaki komutu girin:

python manage.py migrate


3. Projeyi çalıştırmak için terminale aşağıdaki komutu girin:
   
python manage.py runserver


4. Tarayıcınızda [http://127.0.0.1:8000/](http://127.0.0.1:8000/) adresine giderek uygulamayı kullanmaya başlayabilirsiniz.

## Özellikler

- Kullanıcılar sisteme kayıt olabilir ve giriş yapabilir.
- Mezunlar profil bilgilerini düzenleyebilir ve mezuniyet bilgilerini ekleyebilir.
- Etkinlikler oluşturulabilir ve mezunlar etkinliklere katılabilir.
- Kullanıcılar birbirlerini takip edebilir ve takip ettikleri kullanıcıların etkinlik katılımlarını görebilir.

## Ekran Görüntüleri

![Anasayfa](/screenshots/home.png)
_Anasayfa görüntüsü._

![Mezun Profili](/screenshots/profile.png)
_Mezun profili görüntüsü._

## Katkıda Bulunma

Katkıda bulunmak için lütfen [CONTRIBUTING.md](/CONTRIBUTING.md) dosyasını inceleyin.

## Lisans

Bu proje [MIT Lisansı](/LICENSE) ile lisanslanmıştır.
