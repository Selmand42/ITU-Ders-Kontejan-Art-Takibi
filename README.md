# ITU-Ders-Kontejan-Artis-Takibi

Bu proje, Python ve Selenium kullanarak ders seçim işlemlerini otomatikleştirmek amacıyla geliştirilmiştir. 
Program, belirtilen sürelerde ders seçim ekranını açmanızı bekler, ders seçim istekleri gönderir ve kontenjanı dolu olan derslerin kontenjanlarında azalma olduğunda dersi seçmeye çalışır.

## Gereksinimler
**Python:** Programın çalışabilmesi için bilgisayarınızda Python yüklü olmalıdır. Python'u resmi web sitesinden indirebilirsiniz.

**Selenium:** Python ile web tarayıcılarını otomatikleştirmek için kullanılan Selenium kütüphanesi gereklidir. Selenium'u yüklemek için aşağıdaki komutu kullanabilirsiniz:

```pip install selenium```

**WebDriver:** Selenium'un çalışabilmesi için kullanacağınız tarayıcıya uygun WebDriver'ın sisteminizde bulunması gerekir. Örneğin, Chrome tarayıcısı için ChromeDriver indirilmelidir. WebDriver'ı indirdikten sonra, programınızda doğru yola sahip olduğundan emin olun.

## Kullanım
Programı çalıştırırken aşağıdaki argümanları sırasıyla girmeniz gerekmektedir:

Ders Seçim Ekranını Açma Süresi (saniye): Programın ders seçim ekranını açmanız için bekleyeceği süre.

Ders Seçim İsteği Gönderme Aralığı (saniye): Programın ders seçim isteklerini hangi aralıklarla göndereceği.

Derslerin CRN Kodları: Seçmek istediğiniz derslerin CRN (Course Reference Number) kodları. Birden fazla ders seçmek isterseniz, kodları aralarında boşluk bırakarak girebilirsiniz.

## Örnek Kullanım:


```python Bot.py 60 5 15111 15112 15113```

60 saniye bekleyerek ders seçim ekranını açmanızı bekler.

5 saniyede bir ders seçim isteği gönderir.

15111, 15112 ve 15113 CRN kodlarına sahip dersleri seçmeye çalışır.

## Önemli Notlar
**İstek Süresi:** Bilgi işlem sistemi, 1.1 saniyenin altında yapılan istekleri yanıtlamayabilir. Bu nedenle, ders seçim isteği gönderme aralığını 1.1 saniyeden büyük bir değer olarak ayarlamanız önerilir.

**Kontenjan Takibi:** Program, kontenjanı dolu olan derslerin kontenjanlarında azalma olduğunda dersi seçmeye çalışır. Bu nedenle, programı çalıştırmadan önce derslerin kontenjan durumlarını kontrol etmeniz faydalı olacaktır.
