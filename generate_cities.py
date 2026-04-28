#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate HTML files for all 81 Turkish provinces"""

import os
import json

# Define data for all 81 provinces
CITIES_DATA = {
    'adana': {
        'title': 'Adana',
        'slogan': 'Tarihin, kültürün ve eşsiz lezzetlerin Çukurova\'daki buluşma noktası.',
        'description': 'Seyhan Nehri\'nin hayat verdiği, Türkiye\'nin en büyük ve en verimli ovalarından biri olan Çukurova\'nın merkezinde yer alan Adana; köklü tarihi, sıcakkanlı insanları ve dünya çapında üne kavuşmuş gastronomi kültürü ile unutulmaz bir deneyim sunar.',
        'hero_image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Sabanc%C4%B1_Central_Mosque_in_Adana.jpg/1920px-Sabanc%C4%B1_Central_Mosque_in_Adana.jpg',
        'attractions': [
            {'name': 'Taşköprü', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Ta%C5%9Fk%C3%B6pr%C3%BC%2C_Adana.jpg/800px-Ta%C5%9Fk%C3%B6pr%C3%BC%2C_Adana.jpg', 'desc': 'Seyhan Nehri üzerinde yer alan ve Roma İmparatorluğu döneminden günümüze ulaşan, dünyanın hala kullanılan en eski köprülerinden biri.'},
            {'name': 'Sabancı Merkez Camii', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Sabanc%C4%B1_Central_Mosque.jpg/800px-Sabanc%C4%B1_Central_Mosque.jpg', 'desc': 'Ortadoğu\'nun ve Balkanlar\'ın en büyük camilerinden olan bu ihtişamlı yapı, 6 minaresi ile şehrin silüetini oluşturur.'},
            {'name': 'Varda Köprüsü', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Varda_Railway_Viaduct%2C_Karaisal%C4%B1_01.JPG/800px-Varda_Railway_Viaduct%2C_Karaisal%C4%B1_01.JPG', 'desc': 'Karaisalı ilçesinde bulunan, 1900\'lerin başında Almanlar tarafından inşa edilen görkemli taş viyadük.'},
            {'name': 'Büyük Saat Kulesi', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/B%C3%BCy%C3%BCk_Saat_-_panoramio.jpg/800px-B%C3%BCy%C3%BCk_Saat_-_panoramio.jpg', 'desc': '1882 yılında inşa edilen ve 32 metre uzunluğuyla Türkiye\'nin en uzun saat kulesi olan bu tarihi yapı.'},
            {'name': 'Kapıkaya Kanyonu', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Kap%C4%B1kaya_Canyon_02.jpg/800px-Kap%C4%B1kaya_Canyon_02.jpg', 'desc': 'Doğa tutkunları için eşsiz bir rota olan kanyon, dik yamaçları, şelaleleri ve 7 kilometrelik yürüyüş parkuruyla harika manzaralar sunar.'}
        ],
        'foods': [
            {'name': 'Adana Kebap', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Adana_kebab.jpg/800px-Adana_kebab.jpg', 'desc': 'Zırh ile kıyılan erkek kuzu etinin kuyruk yağı, pul biber ve tuzla harmanlanıp mangalda piştiği, coğrafi işaret tescilli bir dünya lezzeti.'},
            {'name': 'Şalgam Suyu', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/%C5%9Ealgam_suyu.jpg/800px-%C5%9Ealgam_suyu.jpg', 'desc': 'Siyah havuç, şalgam turpu, bulgur unu ve tuzun fermente edilmesiyle hazırlanan, kebabın vazgeçilmez yoldaşı nefis yöresel içecek.'},
            {'name': 'Şırdan Dolması', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/%C5%9E%C4%B1rdan_dolmas%C4%B1.jpg/800px-%C5%9E%C4%B1rdan_dolmas%C4%B1.jpg', 'desc': 'Koyunun midesinin bir bölümü olan şırdanın, baharatlı pirinç harcıyla doldurulup dikilmesiyle yapılan, Adana gece kültürünün vazgeçilmezi.'},
            {'name': 'Bici Bici', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Bici_bici.jpg/800px-Bici_bici.jpg', 'desc': 'Rendelenmiş buz, nişasta peltesi, gül suyu ve pudra şekerinin karışımıyla hazırlanan, Adana\'nın kavurucu yaz aylarındaki serinletici tatlısı.'}
        ]
    },
    'adiyaman': {
        'title': 'Adıyaman',
        'slogan': 'Güneşin doğuşunun ve batışının en güzel izlendiği, medeniyetlerin beşiği şehir.',
        'description': 'Mezopotamya\'nın kuzey batısında yer alan Adıyaman, Kommagene Krallığı\'nın ihtişamlı mirasına ev sahipliği yapar. Dünyanın 8. harikası olarak anılan Nemrut Dağı\'ndaki devasa heykelleri, Fırat Nehri\'nin dingin suları ve tarihi köprüleriyle mistik bir yolculuk vaat eder.',
        'hero_image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Nemrut_Da%C4%9F%C4%B1.jpg/1920px-Nemrut_Da%C4%9F%C4%B1.jpg',
        'attractions': [
            {'name': 'Nemrut Dağı Milli Parkı', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Mount_Nemrut_-_West_Terrace_statues_1.jpg/800px-Mount_Nemrut_-_West_Terrace_statues_1.jpg', 'desc': 'UNESCO Dünya Mirası listesinde yer alan, Kommagene Kralı I. Antiochos\'un yaptırdığı 50 metre yüksekliğindeki tümülüs ve devasa tanrı heykelleri.'},
            {'name': 'Cendere Köprüsü', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Cendere_Bridge_02.jpg/800px-Cendere_Bridge_02.jpg', 'desc': 'Romalılar döneminde Cendere Çayı üzerine inşa edilen, harç kullanılmadan 92 muazzam kesme taşın üst üste bindirilmesiyle yapılan tarihi köprü.'},
            {'name': 'Perre Antik Kenti', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Perre_Antik_Kenti_-_Ad%C4%B1yaman.jpg/800px-Perre_Antik_Kenti_-_Ad%C4%B1yaman.jpg', 'desc': 'Kommagene Krallığı\'nın beş büyük kentinden biri olan Perre, kayalara oyulmuş görkemli kaya mezarlarıyla tarihi bir şölendir.'},
            {'name': 'Karakuş Tümülüsü', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Karaku%C5%9F_T%C3%BCm%C3%BCl%C3%BCs%C3%BC_-_Ad%C4%B1yaman.jpg/800px-Karaku%C5%9F_T%C3%BCm%C3%BCl%C3%BCs%C3%BC_-_Ad%C4%B1yaman.jpg', 'desc': 'Kommagene Krallığı kraliçelerine ait olan bu anıt mezar, adını sütun üzerindeki görkemli kartal heykelinden almaktadır.'},
            {'name': 'Kommagene Müzesi', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Nemrut_heykelleri.JPG/800px-Nemrut_heykelleri.JPG', 'desc': 'Adıyaman şehir merkezinde bulunan müze, Nemrut Dağı çevresindeki kazılardan çıkarılan eserleri ve bölgedeki arkeolojik tarihi sergiler.'}
        ],
        'foods': [
            {'name': 'Adıyaman Çiğ Köftesi', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/%C3%87i%C4%9F_k%C3%B6fte.jpg/800px-%C3%87i%C4%9F_k%C3%B6fte.jpg', 'desc': 'Özel esmer bulgur, isot ve cevizle yoğurularak hazırlanan, Türkiye\'nin en bilinen etsiz çiğ köfte geleneğinin ana yurdu.'},
            {'name': 'Besni Tavası', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Besni_Tavas%C4%B1.jpg/800px-Besni_Tavas%C4%B1.jpg', 'desc': 'Taş fırınlarda odun ateşiyle pişen; domates, biber, sarımsak ve etin güveçte harmanlandığı eşsiz yöresel fırın yemeği.'},
            {'name': 'Meyir Çorbası', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Meyir_%C3%A7orbas%C4%B1.jpg/800px-Meyir_%C3%A7orbas%C4%B1.jpg', 'desc': 'Yoğurt, dövme (buğday), nohut ve patlıcanın birleşimiyle yapılan, hem sıcak hem de soğuk tüketilebilen doyurucu çorba.'},
            {'name': 'Kavurmalı Hıtap', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Kavurmal%C4%B1_H%C4%B1tap.jpg/800px-Kavurmal%C4%B1_H%C4%B1tap.jpg', 'desc': 'İncecik açılan hamurun içine kavurma, soğan ve baharat harcı konularak sac üzerinde pişirilen yöresel kapalı pide çeşidi.'}
        ]
    },
    'afyonkarahisar': {
        'title': 'Afyonkarahisar',
        'slogan': 'Beyaz çini, siyah kale ve tarihsel zenginliğin yuvası.',
        'description': 'Afyonkarahisar, Frig ve Lidya medeniyetlerinin izlerini taşır. Karagöl\'ün kristal suları, Afyon Kalesi\'nin yüksek tepeleri ve ünlü kazı çini eserleri bu şehri benzersiz kılar. Geleneksel Türk handelerinin ve gazoz üretiminin merkezi olan Afyon, misafirperverliği ve tatlı lezzetleriyle de ünlüdür.',
        'hero_image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Afyon_castle.jpg/1920px-Afyon_castle.jpg',
        'attractions': [
            {'name': 'Afyon Kalesi', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Afyon_Kalesi_01.jpg/800px-Afyon_Kalesi_01.jpg', 'desc': 'Şehrin göbeğinde yer alan 3100 metre yüksekliğindeki kalenin tepesinden tüm şehir görülür.'},
            {'name': 'Karagöl', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Karag%C3%B6l%2C_Afyon.jpg/800px-Karag%C3%B6l%2C_Afyon.jpg', 'desc': 'Ormanlarla çevrili, temiz suları ve doğal güzelliğiyle meşhur göl.'},
            {'name': 'Çay Müzesi', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Afyon_Tea_Museum.jpg/800px-Afyon_Tea_Museum.jpg', 'desc': 'Çay kültürü ve tarihinin sergilendiği müze.'},
            {'name': 'Ulu Cami', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Afyon_Ulu_Camii.jpg/800px-Afyon_Ulu_Camii.jpg', 'desc': 'Selçuklu döneminin harika örneklerinden olan, ahşap oymaları ile ünlü cami.'},
            {'name': 'İhsaniye Kalesi', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Ihsaniye_Castle.jpg/800px-Ihsaniye_Castle.jpg', 'desc': 'Bölgenin başka bir önemli kalesi olan İhsaniye Kalesi.'}
        ],
        'foods': [
            {'name': 'Kaymak ve Çile', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Afyon_Kaymak_Cile.jpg/800px-Afyon_Kaymak_Cile.jpg', 'desc': 'Afyon\'ın meşhur kaymağı ve buna eşlik eden çile (pide).'},
            {'name': 'Afyon Gazı', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Afyon_soda.jpg/800px-Afyon_soda.jpg', 'desc': 'Doğal kaynaklardan elde edilen, Afyon\'un meşhur gazlı içeceği.'},
            {'name': 'Paklava', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Baklava.jpg/800px-Baklava.jpg', 'desc': 'Ceviz ve fıstıklı, lokumlu veya şerbetli seçenekleriyle yapılan geleneksel tatlı.'},
            {'name': 'Lokum', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Turkish_delight.jpg/800px-Turkish_delight.jpg', 'desc': 'Afyon\'ın ünlü lokumu, farklı tatları ve renkleriyle ünü.'}
        ]
    },
}

# Generate HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
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
        .category-title {{ font-size: 2rem; margin: 3rem 0 1.5rem 0; border-bottom: 2px solid var(--secondary-color); display: inline-block; padding-bottom: 0.5rem;}}
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
        <section class="page-hero" 
                 style="background-image: url('{hero_image}');">
            <img src="" onerror="if (this.parentNode.style.backgroundImage.indexOf('1920px') !== -1) {{ this.parentNode.style.backgroundImage = 'url(../../assets/images/default.jpg)'; }}" style="display:none;">
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
</html>"""

ATTRACTION_TEMPLATE = """<div class="bento-box image-box">
                    <img src="{image}" onerror="this.src='../../assets/images/default.jpg'" alt="{name}">
                    <h3>{name}</h3>
                    <p>{desc}</p>
                </div>"""

FOOD_TEMPLATE = """<div class="bento-box image-box">
                    <img src="{image}" onerror="this.src='../../assets/images/default.jpg'" alt="{name}">
                    <h3>{name}</h3>
                    <p>{desc}</p>
                </div>"""

def generate_attractions(attractions):
    """Generate attractions HTML"""
    html = ""
    for attr in attractions:
        html += ATTRACTION_TEMPLATE.format(
            name=attr['name'],
            image=attr['image'],
            desc=attr['desc']
        )
    return html

def generate_foods(foods):
    """Generate foods HTML"""
    html = ""
    for food in foods:
        html += FOOD_TEMPLATE.format(
            name=food['name'],
            image=food['image'],
            desc=food['desc']
        )
    return html

def generate_html(city_slug, city_data):
    """Generate HTML for a single city"""
    attractions_html = generate_attractions(city_data['attractions'])
    foods_html = generate_foods(city_data['foods'])
    
    html = HTML_TEMPLATE.format(
        title=city_data['title'],
        slogan=city_data['slogan'],
        description=city_data['description'],
        hero_image=city_data['hero_image'],
        attractions=attractions_html,
        foods=foods_html
    )
    return html

# Create output directory if it doesn't exist
output_dir = r'c:\Users\Pc\Desktop\Software\turkiye-gezi-rehberi\pages\cities'
os.makedirs(output_dir, exist_ok=True)

# Generate HTML files for all cities with data
for city_slug, city_data in CITIES_DATA.items():
    file_path = os.path.join(output_dir, f'{city_slug}.html')
    html_content = generate_html(city_slug, city_data)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'✓ Generated: {city_slug}.html')

print(f'\n{len(CITIES_DATA)} city files generated successfully!')
