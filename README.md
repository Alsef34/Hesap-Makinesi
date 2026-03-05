# Hesap-Makinesi

# 🧮 Python Hesap Makinesi ve Modern Web Arayüzü

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

Bu proje, temel programlama mantığı ile modern web tasarımını bir araya getiren iki aşamalı bir geliştirme çalışmasıdır. Arka planda matematiksel işlemleri yöneten modüler bir Python scripti bulunurken, ön yüzde bu projeyi tanıtan ve "Glassmorphism" (cam efekti) tasarımıyla dikkat çeken dinamik bir web sayfası yer almaktadır.

## 📑 İçindekiler
- [Proje Hakkında](#-proje-hakkında)
- [Kullanılan Teknolojiler](#-kullanılan-teknolojiler)
- [Özellikler](#-özellikler)
- [Dosya Mimarisi](#-dosya-mimarisi)
- [Kurulum ve Çalıştırma](#-kurulum-ve-çalıştırma)
- [Kod Yapısı ve Mantık](#-kod-yapısı-ve-mantık)

---

## 🚀 Proje Hakkında

Bu çalışma, temel algoritma kurma ve frontend tasarımı yeteneklerini birleştirmeyi amaçlamaktadır. 
* **Terminal tarafında**, kullanıcıdan alınan float (ondalıklı) sayılar ve operatörler `if-elif-else` mantığıyla işlenir ve matematiksel işlemler özel tanımlanmış fonksiyonlar (`toplama`, `cikarma` vb.) üzerinden yürütülür.
* **Web tarafında** ise, HTML5 ve CSS3 kullanılarak, projenin amacını anlatan şık bir sunum sayfası hazırlanmıştır. Tasarımda agresif siyah ve kırmızı tonları, hareketli degrade (animated gradient) arka plan ve koyu tema cam efekti kullanılarak profesyonel bir görünüm elde edilmiştir.

---

## 💻 Kullanılan Teknolojiler

- **Backend / Mantık:** Python 3
- **Frontend / Tasarım:** HTML5, CSS3
- **Tasarım Konseptleri:** - Glassmorphism (Buzlu Cam Efekti)
  - CSS Keyframe Animasyonları (Hareketli Arka Plan)
  - Flexbox (Merkezi Hizalama)

---

## ✨ Özellikler

### Python (Hesap Makinesi)
- Kullanıcıdan `float` veri tipinde güvenli girdi alma.
- `+`, `-`, `*`, `/` işlemleri için bağımsız fonksiyon yapısı.
- Hatalı operatör girişlerine karşı `Geçersiz işlem seçildi.` uyarısı.
- Temiz, okunabilir ve yorum satırlarıyla desteklenmiş kod dizilimi.

### HTML / CSS (Web Arayüzü)
- Tüm cihazlara ve ekran boyutlarına uyumlu (Responsive) esnek yapı.
- `linear-gradient` ve `@keyframes` ile 12 saniyelik döngüde akan siyah/kan kırmızısı arka plan animasyonu.
- `backdrop-filter: blur(12px)` kullanılarak oluşturulan şık ve okunaklı bilgi kartı.
- Vurgulanmış ve genişletilmiş proje açıklama alanı.

---

## 📂 Dosya Mimarisi

Projenin kök dizin yapısı aşağıdaki gibidir:

```text
proje/
│
├── hesap_makinesi.py    # Matematiksel işlemleri yapan ana Python scripti
├── index.html           # Proje tanıtımını barındıran web sayfasının iskeleti
├── style.css            # Animasyonlu arka plan ve karanlık tema stil dosyası
└── README.md            # Bu dokümantasyon dosyası

```

---
## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel ortamınızda test etmek ve çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

### 1. Web Arayüzünü Görüntüleme
Frontend tarafı tamamen statik dosyalardan oluştuğu için ekstra bir sunucu kurulumuna gerek yoktur. Proje klasöründeki `index.html` dosyasını favori web tarayıcınızda açmanız yeterlidir.

### 2. Python Kodunu Çalıştırma
Uygulama arka plan işlemleri için Python 3 gerektirir. İşletim sisteminize göre terminal veya komut satırını açarak aşağıdaki komutları kullanabilirsiniz:

**Ubuntu / Linux Ortamında:**
Terminali açın ve projenin bulunduğu dizine gidin:

```bash
cd /projenin/bulundugu/dizin
python3 hesap_makinesi.py

```

---

## 🧠 Kod Yapısı ve Mantık
Bu proje, temel backend mantığı ile modern frontend sunumunu bir araya getiren bir mimariye sahiptir.

Modüler Fonksiyon Mimarisi: Python tarafında her matematiksel işlem (toplama, cikarma, carpma, bolme) ayrı birer fonksiyon olarak tanımlanmıştır. Bu yaklaşım, kodun okunabilirliğini artırırken karmaşıklığı engeller ve ileride eklenebilecek gelişmiş matematiksel işlemler (örneğin üs alma, karekök) için esnek bir altyapı sunar.

Kontrollü Veri Akışı: Kullanıcıdan alınan girdiler doğrudan float tipine dönüştürülerek ondalıklı hesaplamalara olanak tanınmış, hatalı işlem türü girişleri ise if-elif-else kontrol bloklarıyla filtrelenerek kullanıcıya geri bildirim verilmesi sağlanmıştır.

Modern UI Tasarımı: Ön yüz tasarımında, modern web standartlarına uygun olarak Flexbox kullanılmış ve elementler sayfa merkezine hizalanmıştır. CSS @keyframes animasyonlarıyla desteklenen koyu tema ve "Glassmorphism" (cam efekti) kart yapısı, kodlanan mantığa şık ve dikkat çekici bir arayüz kazandırmıştır.




