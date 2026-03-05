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
- [Geliştirici](#-geliştirici)

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
