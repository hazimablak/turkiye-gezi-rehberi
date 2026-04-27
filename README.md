<div align="center">
  <h1>🌍 Türkiye Gezi Rehberi</h1>
  <h3>Turkey Travel Guide</h3>
  
  <p>
    <a href="#tr"><strong>🇹🇷 Türkçe</strong></a> · 
    <a href="#en"><strong>🇬🇧 English</strong></a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
  </p>

  <p>
    <strong>Türkiye'nin 81 ilini ve 7 coğrafi bölgesini keşfet</strong><br>
    <em>Explore Turkey's 81 provinces and 7 geographical regions</em>
  </p>
</div>

---

<a id="tr"></a>

## 🇹🇷 Türkçe

### 📌 Proje Hakkında

**Türkiye Gezi Rehberi**, Türkiye'nin 81 ilinin ve 7 coğrafi bölgesinin tarihi, kültürel ve turistik zenginliklerini modern bir web arayüzüyle sunan **interaktif bir platformdur**. Proje, klasik ansiklopedik bilgilerin ötesine geçerek **kullanıcı deneyimini (UI/UX)** ön planda tutan bir yaklaşımla geliştirilmiştir.

### ✨ Öne Çıkan Özellikler

- **🎨 Modern Mimari:** Glassmorphism ve Bento Grid UI sistemleri kullanılarak tasarlanmış şık ve çağdaş arayüz
- **📊 İnteraktif Pano (Dashboard):** Dinamik JavaScript altyapısı ile anlık güncellenen bölge ve şehir panosu
- **📚 Eksiksiz İçerik:** Türkiye'nin 7 coğrafi bölgesi ve 81 ilinin tamamı için optimize edilmiş gezi kartları
- **📱 Tam Uyumlu (Responsive):** Mobil, tablet ve masaüstü cihazlar için %100 uyumlu (Grid & Flexbox) tasarım
- **✅ Temiz Kod (Clean Code):** Modüler dosya yapısı, sürdürülebilir CSS (CSS Variables) ve standartlaştırılmış isimlendirme
- **⚡ Hızlı Performans:** Optimize edilmiş statik dosyalar, veritabanı sorgusu olmaksızın anlık yükleme

### 📋 İçerik Yapısı

```
7 Coğrafi Bölge:
├── Marmara Bölgesi (İstanbul, Bursa, Kocaeli, Edirne, Tekirdağ, Çanakkale, Balıkesir, Yalova)
├── Ege Bölgesi (İzmir, Aydın, Denizli, Muğla, Manisa, Afyon, Uşak)
├── Akdeniz Bölgesi (Antalya, Mersin, Adana, Hatay, Isparta, Burdur, Karaman)
├── İç Anadolu Bölgesi (Ankara, Kayseri, Sivas, Tokat, Amasya, Çorum, Kırıkkale, Yozgat, Nevşehir, Niğde, Aksaray, Kırşehir)
├── Karadeniz Bölgesi (Samsun, Rize, Trabzon, Giresun, Ordu, Gümüşhane, Bayburt, Sinop, Çankırı, Kastamonu)
├── Doğu Anadolu Bölgesi (Erzurum, Van, Erzincan, Elazığ, Bingöl, Tunceli, Malatya, Bitlis, Hakkari)
└── Güneydoğu Anadolu Bölgesi (Gaziantep, Şanlıurfa, Diyarbakır, Mardin, Batman, Siirt, Kilis, Adıyaman)
```

### 🚀 Kurulum ve Çalıştırma

Proje tamamen **statik dosyalardan (HTML/CSS/JS)** oluştuğu için herhangi bir veritabanı veya sunucu kurulumuna **ihtiyaç duymaz**.

#### Adım 1: Projeyi Klonlayın
```bash
git clone https://github.com/hazimablak/turkiye-gezi-rehberi.git
cd turkiye-gezi-rehberi
```

#### Adım 2: Açın
Aşağıdaki yöntemlerden birini seçin:

**Seçenek A: Doğrudan Tarayıcı**
- `index.html` dosyasını tarayıcınızda açın (Chrome, Edge, Safari, Firefox vb.)

**Seçenek B: VS Code Live Server**
- VS Code'da `Live Server` eklentisini kurun
- `index.html` dosyasına sağ tıklayın → `Open with Live Server`

**Seçenek C: Python Basit Sunucu**
```bash
python -m http.server 8000
# Tarayıcıda http://localhost:8000 açın
```

### 📁 Dosya Yapısı

```
turkiye-gezi-rehberi/
├── index.html              # Ana sayfa
├── css/
│   ├── style.css          # Ana stil dosyası
│   ├── variables.css      # CSS değişkenleri (renkler, fontlar vb.)
│   └── responsive.css     # Responsive tasarım kuralları
├── js/
│   ├── app.js             # Ana JavaScript dosyası
│   ├── data.js            # Bölge ve il verileri
│   └── dashboard.js       # Dashboard fonksiyonları
└── assets/
    ├── images/            # Bölge ve il görselleri
    └── icons/             # İkonlar
```

### 🛠️ Kullanılan Teknolojiler

| Teknoloji | Versiyon | Açıklama |
|-----------|----------|----------|
| **HTML5** | - | Semantik yapı ve içerik |
| **CSS3** | - | Glassmorphism, Grid, Flexbox, Animations |
| **JavaScript (Vanilla)** | ES6+ | Dinamik işlevsellik ve veri yönetimi |
| **Responsive Design** | - | Mobile-First yaklaşımı |

### 💡 Tasarım Yönetmelikleri

- **Renk Sistemi:** CSS Variables ile merkezi renk yönetimi
- **Tipografi:** Modern web fontları (Google Fonts uyumlu)
- **Spacing:** 8px Grid sistemi
- **Breakpoints:** 
  - Mobil: < 480px
  - Tablet: 480px - 1024px
  - Desktop: > 1024px

### 🎯 Hedefler ve Vizyonu

- ✅ Türk turizmi hakkında kapsamlı bilgi sunmak
- ✅ Paydaşları birbirine bağlamak ve kültürel farkındalığı artırmak
- ✅ Öğrencilerin coğrafi bilgi düzeyini geliştirmek
- ✅ Profesyonel bir web deneyimi sağlamak

### 🤝 Katkıda Bulunma

Projeyi geliştirmek isterseniz:

1. **Fork** edin
2. **Feature Branch** oluşturun (`git checkout -b feature/AmazingFeature`)
3. **Commit** edin (`git commit -m 'Add some AmazingFeature'`)
4. **Push** edin (`git push origin feature/AmazingFeature`)
5. **Pull Request** açın

### 📝 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasını inceleyiniz.

### 👨‍💻 Geliştirici

**Hazım Ablak**
- 🎓 Siirt Üniversitesi, Bilgisayar Mühendisliği
- 💼 Bilgisayar Mühendisi / Kurucu
- 🔗 [GitHub](https://github.com/hazimablak)
- 📸 [Instagram](https://instagram.com)

### 📞 İletişim

Sorularınız, önerileriniz veya yardımınız için lütfen bize ulaşın:
- 📧 Email: [email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/hazimablak/turkiye-gezi-rehberi/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/hazimablak/turkiye-gezi-rehberi/discussions)

### 🙏 Teşekkürler

Bu projeyi gerçekleştirmemizde destek veren Siirt Üniversitesi Bilgisayar Mühendisliği Bölümü'ne teşekkür ederiz.

---

<a id="en"></a>

## 🇬🇧 English

### 📌 About the Project

**Turkey Travel Guide** is an **interactive platform** that presents the historical, cultural, and tourist riches of Turkey's 81 provinces and 7 geographical regions through a modern web interface. The project goes beyond classic encyclopedic information with an approach that prioritizes **user experience (UI/UX)**.

### ✨ Key Features

- **🎨 Modern Architecture:** Sleek and contemporary interface designed using Glassmorphism and Bento Grid UI systems
- **📊 Interactive Dashboard:** Region and city dashboard that updates instantly with dynamic JavaScript infrastructure
- **📚 Comprehensive Content:** Highly optimized travel cards for all 7 geographical regions and 81 provinces of Turkey
- **📱 Fully Responsive:** 100% compatible design (Grid & Flexbox) for mobile, tablet, and desktop devices
- **✅ Clean Code:** Modular file structure, maintainable CSS (CSS Variables), and standardized naming conventions
- **⚡ Fast Performance:** Optimized static files with instant loading without database queries

### 📋 Content Structure

```
7 Geographical Regions:
├── Marmara Region (Istanbul, Bursa, Kocaeli, Edirne, Tekirdağ, Çanakkale, Balıkesir, Yalova)
├── Aegean Region (Izmir, Aydın, Denizli, Muğla, Manisa, Afyon, Uşak)
├── Mediterranean Region (Antalya, Mersin, Adana, Hatay, Isparta, Burdur, Karaman)
├── Central Anatolia Region (Ankara, Kayseri, Sivas, Tokat, Amasya, Çorum, Kırıkkale, Yozgat, Nevşehir, Niğde, Aksaray, Kırşehir)
├── Black Sea Region (Samsun, Rize, Trabzon, Giresun, Ordu, Gümüşhane, Bayburt, Sinop, Çankırı, Kastamonu)
├── Eastern Anatolia Region (Erzurum, Van, Erzincan, Elazığ, Bingöl, Tunceli, Malatya, Bitlis, Hakkari)
└── Southeastern Anatolia Region (Gaziantep, Şanlıurfa, Diyarbakır, Mardin, Batman, Siirt, Kilis, Adıyaman)
```

### 🚀 Installation & Setup

Since the project consists entirely of **static files (HTML/CSS/JS)**, it does not require any database or server installation.

#### Step 1: Clone the Repository
```bash
git clone https://github.com/hazimablak/turkiye-gezi-rehberi.git
cd turkiye-gezi-rehberi
```

#### Step 2: Open
Choose one of the following methods:

**Option A: Direct Browser**
- Open `index.html` in your browser (Chrome, Edge, Safari, Firefox, etc.)

**Option B: VS Code Live Server**
- Install the `Live Server` extension in VS Code
- Right-click on `index.html` → `Open with Live Server`

**Option C: Python Simple Server**
```bash
python -m http.server 8000
# Open http://localhost:8000 in your browser
```

### 📁 File Structure

```
turkiye-gezi-rehberi/
├── index.html              # Homepage
├── css/
│   ├── style.css          # Main stylesheet
│   ├── variables.css      # CSS variables (colors, fonts, etc.)
│   └── responsive.css     # Responsive design rules
├── js/
│   ├── app.js             # Main JavaScript file
│   ├── data.js            # Region and province data
│   └── dashboard.js       # Dashboard functions
└── assets/
    ├── images/            # Region and province images
    └── icons/             # Icons
```

### 🛠️ Technologies Used

| Technology | Version | Description |
|-----------|---------|-------------|
| **HTML5** | - | Semantic structure and content |
| **CSS3** | - | Glassmorphism, Grid, Flexbox, Animations |
| **JavaScript (Vanilla)** | ES6+ | Dynamic functionality and data management |
| **Responsive Design** | - | Mobile-First approach |

### 💡 Design Guidelines

- **Color System:** Centralized color management with CSS Variables
- **Typography:** Modern web fonts (Google Fonts compatible)
- **Spacing:** 8px Grid system
- **Breakpoints:**
  - Mobile: < 480px
  - Tablet: 480px - 1024px
  - Desktop: > 1024px

### 🎯 Goals and Vision

- ✅ Provide comprehensive information about Turkish tourism
- ✅ Connect stakeholders and raise cultural awareness
- ✅ Enhance students' geographical knowledge level
- ✅ Deliver a professional web experience

### 🤝 Contributing

If you'd like to improve the project:

1. **Fork** the repository
2. Create a **Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

### 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

### 👨‍💻 Developer

**Hazım Ablak**
- 🎓 Siirt University, Computer Engineering
- 💼 Computer Engineer / Founder
- 🔗 [GitHub](https://github.com/hazimablak)
- 📸 [Instagram](https://instagram.com)

### 📞 Contact

For questions, suggestions, or support:
- 📧 Email: [email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/hazimablak/turkiye-gezi-rehberi/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/hazimablak/turkiye-gezi-rehberi/discussions)

### 🙏 Acknowledgments

We thank Siirt University Computer Engineering Department for supporting the realization of this project.

---

<div align="center">
  <p>
    <strong>Made with ❤️ by <a href="https://github.com/hazimablak">Hazım Ablak</a></strong>
  </p>
  <p>
    <a href="#tr">⬆️ Başa Dön / Back to Top ⬆️</a>
  </p>
</div>
