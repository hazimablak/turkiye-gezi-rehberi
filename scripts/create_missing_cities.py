from pathlib import Path

output = Path(__file__).resolve().parent.parent / 'pages' / 'cities'
missing = ['bursa', 'gaziantep', 'giresun', 'gumushane', 'hatay', 'istanbul']
proper = {
    'bursa': 'Bursa',
    'gaziantep': 'Gaziantep',
    'giresun': 'Giresun',
    'gumushane': 'Gümüşhane',
    'hatay': 'Hatay',
    'istanbul': 'İstanbul',
}

def make_page(city):
    title = proper[city]
    slogan = f'{title}, tarih, lezzet ve kültürün iç içe geçtiği eşsiz bir destinasyondur.'
    description = f'{title}, zengin tarihi mirası ve benzersiz doğal güzellikleriyle Türkiye ziyaretçilerine unutulmaz bir deneyim sunar.'
    hero_image = '../../assets/images/default.jpg'
    attractions = [
        ('Şehir Merkezi', 'Şehrin canlı merkezinde yer alan çarşılar, kafeler ve sokaklar; yerel yaşamı hissetmek için ideal.'),
        ('Tarihi Mekanlar', 'Kentteki eski mahalleler, anıtlar ve tarihi yapılar; geçmişle bugünü bir arada sunan rotalar.'),
        ('Doğal Güzellikler', 'Yeşil vadiler, göller ve yürüyüş parkurları; şehir sınırları içindeki doğal kaçamaklar.'),
        ('Müze ve Kültür', 'Şehrin geçmişini anlatan müzeler, sanat galerileri ve kültür merkezleri; keşif için güçlü duraklar.'),
        ('Yerel Pazarlar', 'Taze ürünler, hediyelik eşyalar ve yöresel lezzetlerle dolu canlı pazarlar; şehir deneyimini tamamlar.'),
    ]
    foods = [
        ('Yöresel Kebap', 'Şehrin en bilinen et yemeği; baharatlı, lezzetli ve her ziyaretçinin tatması gereken bir özel tarif.'),
        ('Yerel Tatlı', 'Yöresel tatlı çeşidi; şehrin kendine özgü malzemeleri ve sunumuyla farklı bir lezzet sunar.'),
        ('Geleneksel Çorba', 'Bölgesel malzemelerle hazırlanan çorba; serin akşamlarda içinizi ısıtan bir gelenek.'),
        ('Hamur İşi', 'Kahvaltıdan akşam yemeğine kadar tercih edilen yerel hamur işi; yöresel peynir, et veya tatlı dolgusuyla hazırlanır.'),
    ]
    template = '''<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} Gezi Rehberi | Türkiye Gezi Rehberi</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../../css/main.css">
    <style>
        .city-detail-header {{ text-align: center; margin-bottom: 3rem; }}
        .city-detail-header h2 {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--primary-color); }}
        .city-detail-header p {{ font-size: 1.1rem; color: #555; max-width: 800px; margin: 1rem auto; line-height: 1.8; }}
        .category-title {{ font-size: 2rem; margin: 3rem 0 1.5rem 0; border-bottom: 2px solid var(--secondary-color); display: inline-block; padding-bottom: 0.5rem; }}
        .image-box img {{ width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem; background-color: #f0f0f0; }}
    </style>
</head>
<body>
    <header class="navbar">
        <div class="container nav-container">
            <a href="../../index.html" class="logo"><i class="fas fa-map-marked-alt"></i> TÜRKİYE GEZİ REHBERİ</a>
            <nav class="nav-menu">
                <ul>
                    <li><a href="../../index.html">Ana Sayfa</a></li>
                    <li class="dropdown">
                        <a href="#" class="active">Popüler Şehirler <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-content">
                            <li><a href="adana.html">Adana</a></li><li><a href="adiyaman.html">Adıyaman</a></li><li><a href="ankara.html">Ankara</a></li><li><a href="bursa.html">Bursa</a></li><li><a href="canakkale.html">Çanakkale</a></li><li><a href="erzurum.html">Erzurum</a></li><li><a href="gaziantep.html">Gaziantep</a></li><li><a href="hatay.html">Hatay</a></li><li><a href="istanbul.html">İstanbul</a></li><li><a href="konya.html">Konya</a></li><li><a href="siirt.html">Siirt</a></li>
                        </ul>
                    </li>
                    <li><a href="../regions/bolgeler.html">Bölgeler</a></li>
                    <li><a href="../../hakkimizda.html">Hakkımızda</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section class="page-hero" style="background-image: url('{hero_image}');">
            <img src="" onerror="this.parentNode.style.backgroundImage = 'url(../../assets/images/default.jpg)';" style="display:none;">
            <div class="page-hero-overlay"></div>
            <div class="container page-hero-content">
                <h1>{title}</h1>
                <p>{slogan}</p>
            </div>
        </section>

        <section class="container" style="padding: 4rem 0;">
            <div class="city-detail-header">
                <h2>{title} Hakkında</h2>
                <p>{description}</p>
            </div>

            <h3 class="category-title"><i class="fas fa-map-signs"></i> Gezilecek Yerler</h3>
            <div class="bento-grid">
                {attractions}
            </div>

            <h3 class="category-title"><i class="fas fa-utensils"></i> Meşhur Lezzetler</h3>
            <div class="bento-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));">
                {foods}
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-item"><i class="fas fa-envelope"></i><div><h4>E-Posta</h4><a href="mailto:hazimablak1453@gmail.com">gezirehberi@gmail.com</a></div></div>
            <div class="footer-item"><i class="fas fa-phone-alt"></i><div><h4>İrtibat No</h4><a href="tel:+905303611650">+90 530 361 16 50</a></div></div>
            <div class="footer-item"><i class="fab fa-instagram"></i><div><h4>Instagram</h4><a href="https://www.instagram.com/hazim.ablak" target="_blank" rel="noopener noreferrer">@hazim.ablak</a></div></div>
        </div>
        <div class="footer-bottom"><p>&copy; 2026 Türkiye Gezi Rehberi. Tüm Hakları Saklıdır.</p></div>
    </footer>
</body>
</html>'''
    attr_html = ''.join([
        f'                <div class="bento-box image-box">\n'
        f'                    <img src="../../assets/images/default.jpg" onerror="this.src=\'../../assets/images/default.jpg\'" alt="{name}">\n'
        f'                    <h3>{name}</h3>\n'
        f'                    <p>{desc}</p>\n'
        f'                </div>\n'
        for name, desc in attractions
    ])
    food_html = ''.join([
        f'                <div class="bento-box image-box">\n'
        f'                    <img src="../../assets/images/default.jpg" onerror="this.src=\'../../assets/images/default.jpg\'" alt="{name}">\n'
        f'                    <h3>{name}</h3>\n'
        f'                    <p>{desc}</p>\n'
        f'                </div>\n'
        for name, desc in foods
    ])
    return template.format(title=title, slogan=slogan, description=description, hero_image=hero_image, attractions=attr_html, foods=food_html)

for city in missing:
    page = output / f'{city}.html'
    page.write_text(make_page(city), encoding='utf-8')
    print(f'Created {page.name}')
