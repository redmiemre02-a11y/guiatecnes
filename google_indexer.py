import os
import json
import urllib.request
import re
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/indexing"]
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), "service_account.json")
SITEMAP_URL = "https://guiatecnes.com/sitemap-0.xml"

def get_urls_from_sitemap(sitemap_url):
    print(f"Fetching sitemap from: {sitemap_url}")
    req = urllib.request.Request(sitemap_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        xml = resp.read().decode('utf-8')
    urls = re.findall(r'<loc>(.*?)</loc>', xml)
    print(f"Total URLs found in sitemap: {len(urls)}")
    return urls

def main():
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print(f"ERROR: {SERVICE_ACCOUNT_FILE} bulunamadi!")
        print("Lutfen Google Cloud Console'dan indirdiginiz service_account.json dosyasini es-tech-blog klasorune ekleyin.")
        return

    print("Google Service Account yukleniyor...")
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("indexing", "v3", credentials=credentials)

    urls = get_urls_from_sitemap(SITEMAP_URL)
    
    # Google Indexing API gunluk maksimum 200 istek kotasi tanir
    limit = min(200, len(urls))
    print(f"\nToplam {limit} adet URL Google Indexing API'ye gonderilecek...\n")

    success_count = 0
    error_count = 0

    for idx, url in enumerate(urls[:limit], 1):
        body = {
            "url": url,
            "type": "URL_UPDATED"
        }
        try:
            response = service.urlNotifications().publish(body=body).execute()
            print(f"[{idx}/{limit}] [OK] {url}")
            success_count += 1
        except Exception as e:
            print(f"[{idx}/{limit}] [HATA] {url} -> {e}")
            error_count += 1

    print("\n" + "="*50)
    print(f"Bitti! Basarili: {success_count} | Hatali: {error_count}")
    print("Google botlari bu sayfalari oncelikli siraya aldi.")
    print("="*50)

if __name__ == "__main__":
    main()
