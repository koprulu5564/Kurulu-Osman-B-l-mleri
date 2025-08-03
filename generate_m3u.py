import requests
import os

# Ayarlar
BASE_URL = "https://www.atv.com.tr/kurulus-osman/"
PROXY_PREFIX = "https://stream-extractor.koprulu.workers.dev/?url="
EXT = "&ext=mp4"
COVER_ART = "https://iaatv.tmgrup.com.tr/71709e/500/268/0/0/500/268?u=https://iatv.tmgrup.com.tr/2024/09/24/500x268/1727165994263.jpg"
CATEGORY = "Kuruluş Osman"

def get_last_episode():
    try:
        with open("last_episode.txt", "r") as f:
            return int(f.read().strip())
    except:
        return 194

def check_episode(episode):
    try:
        url = f"{PROXY_PREFIX}{BASE_URL}{episode}-bolum/izle"
        return requests.head(url, timeout=5).status_code == 200
    except:
        return False

def generate_m3u(end_episode):
    m3u = f"""#EXTM3U
#EXTINF:-1 group-title="{CATEGORY}",{CATEGORY}
{COVER_ART}\n"""
    
    for ep in range(1, end_episode + 1):
        m3u += f"""#EXTINF:-1 tvg-id="KurulusOsman{ep}" tvg-name="Bölüm-{ep}" group-title="{CATEGORY}",Kuruluş Osman Bölüm-{ep}
{PROXY_PREFIX}{BASE_URL}{ep}-bolum/izle{EXT}\n"""
    
    with open("kurulus-osman.m3u", "w", encoding="utf-8") as f:
        f.write(m3u)

if __name__ == "__main__":
    last_ep = get_last_episode()
    if check_episode(last_ep + 1):
        new_ep = last_ep + 1
        with open("last_episode.txt", "w") as f:
            f.write(str(new_ep))
        generate_m3u(new_ep)
    else:
        generate_m3u(last_ep)
