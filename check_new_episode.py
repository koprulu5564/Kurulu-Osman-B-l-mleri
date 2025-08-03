import requests
import os
from generate_m3u import generate_m3u, save_m3u

def get_last_episode():
    # Dosyadan son bölüm numarasını oku
    if os.path.exists("last_episode.txt"):
        with open("last_episode.txt", "r") as f:
            return int(f.read().strip())
    return 194  # Varsayılan değer

def set_last_episode(episode):
    # Son bölüm numarasını kaydet
    with open("last_episode.txt", "w") as f:
        f.write(str(episode))

def check_new_episode(last_episode):
    next_episode = last_episode + 1
    test_url = f"https://www.atv.com.tr/kurulus-osman/{next_episode}-bolum/izle"
    proxy_url = f"https://stream-extractor.koprulu.workers.dev/?url={test_url}"
    
    try:
        response = requests.head(proxy_url, timeout=10)
        if response.status_code == 200:
            print(f"Yeni bölüm bulundu: {next_episode}")
            return next_episode
        else:
            print(f"Henüz yeni bölüm yok (Bölüm {next_episode} için 200 dönmedi)")
            return None
    except Exception as e:
        print(f"Kontrol sırasında hata oluştu: {str(e)}")
        return None

if __name__ == "__main__":
    last_episode = get_last_episode()
    new_episode = check_new_episode(last_episode)
    
    if new_episode:
        # Yeni M3U oluştur
        m3u_content = generate_m3u(1, new_episode)
        save_m3u(m3u_content)
        set_last_episode(new_episode)
        print("M3U playlist güncellendi!")
    else:
        print("Yeni bölüm bulunamadı, işlem sonlandırıldı.")
