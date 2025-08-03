import requests
from datetime import datetime

BASE_URL = "https://www.atv.com.tr/kurulus-osman/"
PROXY_PREFIX = "https://stream-extractor.koprulu.workers.dev/?url="
EXT = "&ext=mp4"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
COVER_ART = "https://iaatv.tmgrup.com.tr/71709e/500/268/0/0/500/268?u=https://iatv.tmgrup.com.tr/2024/09/24/500x268/1727165994263.jpg"
CATEGORY = "Kuruluş Osman"  # Özel kategori adı

def generate_m3u(start_episode=1, end_episode=194):
    m3u_content = "#EXTM3U\n"
    m3u_content += f'#EXTINF:-1 tvg-id="{CATEGORY}" group-title="{CATEGORY}",{CATEGORY}\n'
    m3u_content += f"{COVER_ART}\n"  # Kategori için logo
    
    for episode in range(start_episode, end_episode + 1):
        episode_url = f"{BASE_URL}{episode}-bolum/izle"
        proxy_url = f"{PROXY_PREFIX}{episode_url}{EXT}"
        title = f"Kuruluş Osman Bölüm-{episode}"
        
        m3u_content += f'#EXTINF:-1 tvg-id="KurulusOsman{episode}" tvg-name="{title}" tvg-logo="{COVER_ART}" group-title="{CATEGORY}",{title}\n'
        m3u_content += f"{proxy_url}\n"
    
    return m3u_content
