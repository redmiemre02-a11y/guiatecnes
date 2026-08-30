#!/usr/bin/env python3
"""
TechES - İçerik Botu v3.0 (Akıllı Yayın Modu)
================================================
- İlk çalıştırma: Her kategoriden 1 yazı (14 yazı)
- Günlük mod: Rastgele 2 yazı (daha önce yazılmamış konulardan)
- progress.json ile hangi konuların yazıldığını takip eder
- GitHub Actions ile tam otomatik çalışır

Kullanım:
  python content_bot.py --init      → Her kategoriden 1 yazı (başlangıç)
  python content_bot.py --daily     → Günlük 2 rastgele yazı
  python content_bot.py --daily --count 3  → Günlük 3 yazı
  python content_bot.py --topic "..." --keyword "..."  → Tek yazı
  python content_bot.py --status    → Kaç konu kaldı, kaçı yazıldı
  python content_bot.py --dry-run --daily → Test et, API çağrısı yapma
"""

import os
import sys
import json
import time
import random
import argparse
import re
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

try:
    from openai import OpenAI
except ImportError:
    print("❌ openai kurulu değil! → pip install openai")
    sys.exit(1)

try:
    from config import DEEPSEEK_API_KEY, DEEPSEEK_MODEL, OUTPUT_PATH, AUTHOR_NAME, PEXELS_API_KEY
except ImportError:
    print("❌ config.py bulunamadı!")
    sys.exit(1)


PROGRESS_FILE = "progress.json"
TOPICS_FILE   = "topics.json"


# ============================================================
# RENK KODLARI
# ============================================================
class C:
    RESET  = '\033[0m'
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    RED    = '\033[91m'
    CYAN   = '\033[96m'
    BOLD   = '\033[1m'
    DIM    = '\033[2m'

def ok(msg):   print(f"{C.GREEN}✅ {msg}{C.RESET}")
def info(msg): print(f"{C.CYAN}ℹ  {msg}{C.RESET}")
def warn(msg): print(f"{C.YELLOW}⚠️  {msg}{C.RESET}")
def err(msg):  print(f"{C.RED}❌ {msg}{C.RESET}")
def step(msg): print(f"{C.BOLD}→  {msg}{C.RESET}")


# ============================================================
# PROGRESS TAKIBI
# ============================================================
def load_progress() -> dict:
    """Hangi konuların yazıldığını yükler."""
    if Path(PROGRESS_FILE).exists():
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"written": [], "total_written": 0, "last_run": None}


def save_progress(progress: dict):
    """İlerlemeyi kaydeder."""
    progress["last_run"] = datetime.now().isoformat()
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def load_topics() -> list:
    """topics.json'ı yükler."""
    if not Path(TOPICS_FILE).exists():
        err(f"{TOPICS_FILE} bulunamadı!")
        sys.exit(1)
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_pending_topics() -> list:
    """Henüz yazılmamış konuları döndürür."""
    all_topics = load_topics()
    progress   = load_progress()
    written    = set(progress.get("written", []))
    return [t for t in all_topics if t["keyword"] not in written]


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================
def slugify(text: str) -> str:
    text = text.lower()
    for a, b in [('áàäâ','a'),('éèëê','e'),('íìïî','i'),('óòöô','o'),('úùüû','u'),('ñ','n')]:
        for ch in a: text = text.replace(ch, b)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return re.sub(r'-+', '-', text).strip('-')[:80]


def reading_time(text: str) -> int:
    return max(1, round(len(text.split()) / 200))


def clean(text: str) -> str:
    text = re.sub(r'^```(?:markdown|md|json)?\n?', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n?```\s*$', '', text, flags=re.MULTILINE)
    return text.strip()


# ============================================================
# PEXELS — Resim Çek
# ============================================================
TAG_QUERIES = {
    "ia":             "artificial intelligence technology",
    "alternativas":   "software apps computer",
    "tecnologia":     "technology digital",
    "guias":          "tutorial learning computer",
    "finanzas":       "finance money investment",
    "ciberseguridad": "cybersecurity privacy lock",
    "emprendimiento": "business entrepreneur laptop",
    "salud":          "health wellness smartwatch",
    "hogar":          "smart home technology gadget",
    "gaming":         "gaming pc setup rgb",
    "movil":          "smartphone mobile app",
    "familia":        "family children technology",
    "educacion":      "education online learning",
    "productividad":  "productivity workspace laptop",
}

FALLBACK_IMAGES = {
    "ia":             "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=1200",
    "finanzas":       "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1200",
    "ciberseguridad": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200",
    "emprendimiento": "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=1200",
    "gaming":         "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200",
    "movil":          "https://images.unsplash.com/photo-1512054502232-10a0a035d672?w=1200",
    "salud":          "https://images.unsplash.com/photo-1585435557343-3b092031a831?w=1200",
    "hogar":          "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200",
    "educacion":      "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=1200",
    "productividad":  "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=1200",
    "alternativas":   "https://images.unsplash.com/photo-1537432376769-00f5c2f4c8d2?w=1200",
    "tecnologia":     "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200",
    "guias":          "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=1200",
    "familia":        "https://images.unsplash.com/photo-1536640712-4d4c36ff0e4e?w=1200",
}

def fetch_image(keyword: str, tag: str) -> dict:
    query   = TAG_QUERIES.get(tag, keyword)
    encoded = urllib.parse.quote(query)
    url     = f"https://api.pexels.com/v1/search?query={encoded}&per_page=5&orientation=landscape&size=large"
    try:
        req = urllib.request.Request(url, headers={
            "Authorization": PEXELS_API_KEY,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        with urllib.request.urlopen(req, timeout=8) as r:
            data   = json.loads(r.read().decode())
            photos = data.get("photos", [])
            if photos:
                p = random.choice(photos)   # Her seferinde farklı resim
                return {"url": p["src"]["large2x"], "photographer": p["photographer"],
                        "photographer_url": p["photographer_url"], "alt": f"Imagen de {keyword}"}
    except Exception as e:
        warn(f"Pexels hatası: {e}")
    fallback = FALLBACK_IMAGES.get(tag, "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200")
    return {"url": fallback, "photographer": "Unsplash", "photographer_url": "https://unsplash.com",
            "alt": f"Imagen de {keyword}"}


# ============================================================
# DEEPSEEK — Chat
# ============================================================
def get_client():
    return OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")


def chat(client, system: str, user: str, temperature: float = 0.7) -> str:
    r = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        temperature=temperature, max_tokens=4096,
    )
    return r.choices[0].message.content.strip()


# ============================================================
# 3 ADIMLI MAKALE ÜRETİMİ
# ============================================================
def gen_outline(client, topic: str, keyword: str) -> str:
    step("1/4 → Outline oluşturuluyor...")
    return chat(client,
        "Eres experto en SEO de tecnología. Responde SOLO con el esquema solicitado, sin explicaciones.",
        f"""Crea un esquema para un artículo sobre:
TEMA: "{topic}" | KEYWORD: "{keyword}"

Incluye: título H1 SEO (máx 65 chars), TL;DR con 3 puntos, 4-6 secciones H2 con H3,
tabla comparativa (5+ columnas), FAQ con 3 preguntas específicas.""",
        temperature=0.4)


def gen_article(client, topic: str, keyword: str, outline: str) -> str:
    step("2/4 → Makale yazılıyor (EEAT uyumlu)...")
    return chat(client,
        """Eres blogger de tecnología con 10 años de experiencia. Español nativo, tono personal.
REGLAS: 1) NUNCA empieces con "En el mundo digital actual" o similares.
2) Usa "En nuestras pruebas...", "Lo que notamos fue...".
3) Párrafos máx 3 líneas. 4) Para cada herramienta: ¿Para quién?, ✅Pros, ❌Contras, 💰Precio.
5) Tabla comparativa. 6) FAQ con respuestas de 2-4 líneas. 7) 1.200-1.800 palabras.""",
        f"""Escribe el artículo completo siguiendo este esquema:
{outline}

TEMA: "{topic}" | KEYWORD: "{keyword}"

SALIDA: Solo Markdown. Empieza con ## ⚡ TL;DR""",
        temperature=0.75)


def gen_meta(client, body: str, topic: str, keyword: str) -> dict:
    step("3/4 → Meta veriler üretiliyor...")
    raw = chat(client,
        "Eres experto SEO. Responde SOLO con JSON válido, sin texto adicional.",
        f"""Analiza este artículo y devuelve JSON:
KEYWORD: "{keyword}" | TEMA: "{topic}"
FRAGMENTO: {body[:1500]}

{{"title": "título SEO máx 65 chars con keyword",
  "description": "meta desc 140-155 chars con keyword",
  "tags_extra": ["tag2", "tag3"]}}""",
        temperature=0.2)
    raw = clean(raw)
    try:    return json.loads(raw)
    except: return {"title": topic[:65], "description": f"Todo sobre {keyword} en 2026.", "tags_extra": []}


# ============================================================
# TEK MAKALEYİ KAYDET
# ============================================================
def generate_one(topic_item: dict, dry_run: bool = False) -> bool:
    """Tek bir konuyu işler. Başarılıysa True döner."""
    topic   = topic_item["topic"]
    keyword = topic_item["keyword"]
    tag     = topic_item.get("tag", "tecnologia")

    info(f"Konu  : {topic}")
    info(f"Keyword: {keyword} | Tag: {tag}")

    if dry_run:
        warn("DRY RUN — yazılmadı")
        return True

    client = get_client()
    try:
        outline = gen_outline(client, topic, keyword);  time.sleep(1)
        body    = clean(gen_article(client, topic, keyword, outline)); time.sleep(1)
        meta    = gen_meta(client, body, topic, keyword); time.sleep(0.5)

        step("4/4 → Resim aranıyor (Pexels)...")
        img = fetch_image(keyword, tag)
        ok(f"Resim: {img['photographer']}")

        # Frontmatter
        all_tags  = [tag] + [t for t in meta.get("tags_extra", []) if t != tag]
        rt        = reading_time(body)
        fm = f"""---
title: "{meta['title'].replace('"', "'")}"
description: "{meta['description'].replace('"', "'")}"
pubDate: {datetime.now().strftime('%Y-%m-%d')}
heroImage: "{img['url']}"
heroImageAlt: "{img['alt']}"
photographer: "{img['photographer']}"
photographerUrl: "{img['photographer_url']}"
tags: {json.dumps(all_tags, ensure_ascii=False)}
author: "{AUTHOR_NAME}"
readingTime: {rt}
---
"""
        out_dir = Path(OUTPUT_PATH)
        out_dir.mkdir(parents=True, exist_ok=True)
        filepath = out_dir / (slugify(keyword) + ".md")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fm + "\n" + body)

        ok(f"Kaydedildi → {filepath.name} (~{len(body.split())} kelime, {rt} dk okuma)")
        return True

    except Exception as e:
        err(f"Hata: {e}")
        return False


# ============================================================
# MODLAR
# ============================================================
def mode_init(dry_run: bool):
    """Her kategoriden 1 yazı — site başlangıcı için."""
    all_topics = load_topics()
    progress   = load_progress()
    written    = set(progress.get("written", []))

    # Her tag'den ilk yazılmamış konuyu seç
    seen_tags = set()
    selected  = []
    for t in all_topics:
        if t["tag"] not in seen_tags and t["keyword"] not in written:
            selected.append(t)
            seen_tags.add(t["tag"])

    print(f"\n{C.BOLD}INIT MODU — Her kategoriden 1 yazı ({len(selected)} adet){C.RESET}\n")

    for i, item in enumerate(selected, 1):
        print(f"\n{'─'*50}")
        print(f"{C.BOLD}[{i}/{len(selected)}]{C.RESET}")
        success = generate_one(item, dry_run)
        if success and not dry_run:
            progress["written"].append(item["keyword"])
            progress["total_written"] = progress.get("total_written", 0) + 1
            save_progress(progress)
        if not dry_run and i < len(selected):
            info("6 saniye bekleniyor..."); time.sleep(6)

    print(f"\n{'═'*50}")
    ok(f"Init tamamlandı! {len(selected)} kategoriye birer yazı yayınlandı.")
    info("Şimdi GitHub'a push edip Vercel'den deploy al.")


def mode_daily(count: int, dry_run: bool):
    """Günlük mod — rastgele N yazı, daha önce yazılmamış konulardan."""
    pending  = get_pending_topics()
    progress = load_progress()

    if not pending:
        warn("Tüm konular yazıldı! topics.json'a yeni konular ekle.")
        return

    # Rastgele seç ama farklı kategorilerden
    random.shuffle(pending)
    # Farklı tag'lerden seçmeye çalış
    selected = []
    used_tags = set()
    for item in pending:
        if len(selected) >= count:
            break
        if item["tag"] not in used_tags or len(selected) < count:
            selected.append(item)
            used_tags.add(item["tag"])
    selected = selected[:count]

    kalan = len(pending) - len(selected)
    print(f"\n{C.BOLD}GÜNLÜK MOD — {len(selected)} yazı | Kalan stok: {kalan} konu{C.RESET}\n")

    written_today = 0
    for i, item in enumerate(selected, 1):
        print(f"\n{'─'*50}")
        print(f"{C.BOLD}[{i}/{len(selected)}]{C.RESET}")
        success = generate_one(item, dry_run)
        if success and not dry_run:
            progress["written"].append(item["keyword"])
            progress["total_written"] = progress.get("total_written", 0) + 1
            save_progress(progress)
            written_today += 1
        if not dry_run and i < len(selected):
            info("6 saniye bekleniyor..."); time.sleep(6)

    print(f"\n{'═'*50}")
    ok(f"Bugün {written_today} yazı yayınlandı!")
    info(f"Toplam yazılan: {progress.get('total_written', 0)} | Kalan: {kalan} konu")


def mode_status():
    """Kaç konu yazıldı, kaçı kaldı."""
    all_topics = load_topics()
    progress   = load_progress()
    written    = set(progress.get("written", []))
    pending    = [t for t in all_topics if t["keyword"] not in written]

    # Kategori bazlı durum
    from collections import Counter
    all_tags     = Counter(t["tag"] for t in all_topics)
    written_tags = Counter(t["tag"] for t in all_topics if t["keyword"] in written)

    print(f"\n{C.BOLD}{'═'*50}")
    print(f"  TechES İçerik Durumu")
    print(f"{'═'*50}{C.RESET}")
    print(f"  Toplam konu   : {len(all_topics)}")
    print(f"  Yazılan       : {C.GREEN}{len(written)}{C.RESET}")
    print(f"  Kalan         : {C.YELLOW}{len(pending)}{C.RESET}")
    print(f"  Son çalışma   : {progress.get('last_run', 'Hiç çalışmadı')[:10]}")
    print(f"\n  {'Kategori':<20} {'Toplam':>7} {'Yazılan':>8} {'Kalan':>7}")
    print(f"  {'─'*46}")
    for tag in sorted(all_tags):
        total   = all_tags[tag]
        done    = written_tags.get(tag, 0)
        left    = total - done
        bar     = "█" * done + "░" * left
        color   = C.GREEN if left == 0 else C.YELLOW if done > 0 else C.RESET
        print(f"  {tag:<20} {total:>7} {color}{done:>8}{C.RESET} {left:>7}  {color}{bar}{C.RESET}")
    print(f"\n  Tahmini kalan süre: ~{len(pending) // 2} gün (günde 2 yazı)")
    print(f"{'═'*50}\n")


# ============================================================
# CLI
# ============================================================
def main():
    parser = argparse.ArgumentParser(
        description="TechES İçerik Botu v3.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modlar:
  --init              Her kategoriden 1 yazı (siteyi başlatmak için)
  --daily             Günlük 2 rastgele yazı (GitHub Actions ile çalışır)
  --daily --count 3   Günlük 3 yazı
  --status            Kaç konu yazıldı, kaçı kaldı
  --topic "..." --keyword "..."  Tek yazı yaz
  --dry-run           API çağrısı yapmadan test et
        """
    )
    parser.add_argument("--init",    action="store_true", help="Her kategoriden 1 yazı")
    parser.add_argument("--daily",   action="store_true", help="Günlük rastgele yazı")
    parser.add_argument("--count",   type=int, default=2, help="Günlük kaç yazı (varsayılan: 2)")
    parser.add_argument("--status",  action="store_true", help="Durum raporu")
    parser.add_argument("--topic",   type=str, help="Tek konu")
    parser.add_argument("--keyword", type=str, help="Tek konu için keyword")
    parser.add_argument("--tag",     type=str, default="tecnologia")
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    print(f"""
{C.CYAN}{C.BOLD}╔══════════════════════════════════════════╗
║  TechES — İçerik Botu v3.0              ║
║  Model: {DEEPSEEK_MODEL:<32}║
╚══════════════════════════════════════════╝{C.RESET}
""")

    if args.status:
        mode_status()
    elif args.init:
        mode_init(dry_run=args.dry_run)
    elif args.daily:
        mode_daily(count=args.count, dry_run=args.dry_run)
    elif args.topic:
        item = {"topic": args.topic, "keyword": args.keyword or args.topic[:50], "tag": args.tag}
        generate_one(item, dry_run=args.dry_run)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
