# TechES — Blog SEO en Español 🚀

Sistema completo para un blog de tecnología en español con generación automática de contenido con IA.

---

## 🗂️ Estructura del Proyecto

```
es-tech-blog/
├── src/
│   ├── content/blog/         ← Artículos en Markdown (el bot los escribe aquí)
│   ├── layouts/BaseLayout.astro
│   ├── components/           ← Header, Footer, PostCard, AdSenseBanner
│   └── pages/                ← index, blog/[slug], categoria/[tag], sobre-nosotros...
├── public/robots.txt
├── content_bot.py            ← 🤖 Bot de contenido con IA
├── config.py                 ← ⚙️ API key y configuración
├── topics.json               ← 📋 50 temas SEO listos para generar
└── requirements.txt
```

---

## 🚀 Kurulum ve Çalıştırma Talimatları

### 1. Gereksinimler
- **Node.js** v18+ (https://nodejs.org)
- **Python** 3.9+ (https://python.org)

### 2. İlk Kurulum

```bash
# Web sitesi bağımlılıklarını kur
npm install

# Python bot bağımlılıklarını kur
pip install -r requirements.txt
```

### 3. API Key Ayarla

`config.py` dosyasını aç ve API key'ini gir:

```python
GEMINI_API_KEY = "BURAYA_GEMINI_API_KEY_GIRIN"
```

> 🔑 Ücretsiz Gemini API Key için: https://aistudio.google.com/app/apikey

---

## 🤖 İçerik Botu Kullanımı

### Tek Makale Üret:
```bash
python content_bot.py --topic "Las mejores herramientas de IA para estudiantes" --keyword "ia para estudiantes gratis"
```

### Tüm Konuları Üret (topics.json):
```bash
python content_bot.py --bulk
```

### API Çağrısı Yapmadan Test Et:
```bash
python content_bot.py --dry-run --topic "Alternativas a Canva gratis"
```

### Kategori Belirt:
```bash
python content_bot.py --topic "..." --tag "alternativas" --category "Alternativas"
```

Tags: `ia` | `alternativas` | `tecnologia` | `guias`

---

## 🌐 Web Sitesini Çalıştır

```bash
# Geliştirme modu (localhost:4321)
npm run dev

# Production build
npm run build

# Build önizleme
npm run preview
```

---

## ☁️ Vercel'e Deploy (ÜCRETSİZ)

1. [vercel.com](https://vercel.com) adresine git ve GitHub hesabınla giriş yap
2. "New Project" → GitHub'daki bu repo'yu seç
3. Ayarlar otomatik gelir (Astro framework algılanır)
4. "Deploy" butonuna bas → 2 dakikada site yayında!
5. "Settings → Domains" bölümüne kendi domain adını ekle

---

## 📰 AdSense Entegrasyonu

AdSense onayı için gerekli sayfalar hazır:
- `/sobre-nosotros` (Hakkımızda)
- `/politica-de-privacidad` (Gizlilik Politikası)
- `/contacto` (İletişim)

Onay aldıktan sonra `src/layouts/BaseLayout.astro` dosyasındaki bu satırı aktif et:

```html
<!-- <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXX"...> -->
```

Ve `src/components/AdSenseBanner.astro` dosyasındaki placeholder'ları gerçek AdSense kodlarıyla değiştir.

---

## 🔗 Önemli Linkler

- Gemini API Key: https://aistudio.google.com/app/apikey
- Vercel Deploy: https://vercel.com
- Domain (Alastyr): https://www.alastyr.com
- Google AdSense: https://adsense.google.com
- Google Search Console: https://search.google.com/search-console
