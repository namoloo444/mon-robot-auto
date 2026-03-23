import requests
import time
import os
from flask import Flask
from threading import Thread

# --- CONFIGURATION NAMOLO ---
URL_FIRE = "https://firefaucet.win/autofaucet/"
# COLLE TON COOKIE ENTIER ICI ENTRE LES GUILLEMETS
MON_COOKIE = '_ga=GA1.1.507508636.1774193934; _ga_62J3KC448K=GS2.1.s1774198477$o2$g1$t1774199588$j60$10$h0'

app = Flask('')
@app.route('/')
def home(): return "Robot Namolo Turbo 62s en ligne"

def run_faucet():
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Infinix)"
        "Cookie": MON_COOKIE
    }
    print("[*] Robot TURBO lancé : Utilisation des ACP en cours...")
    
    while True:
        try:
            # Le script visite la page pour valider l'utilisation des ACP
            r = requests.get(URL_FIRE, headers=headers, timeout=20)
            if r.status_code == 200:
                print(f"[+] {time.strftime('%H:%M')} - 16 Satoshi validés via ACP !")
            else:
                print(f"[!] Erreur {r.status_code} - Vérifie ton Cookie")
        except:
            pass
        
        # Réglé sur 62 secondes comme tu as demandé
        time.sleep(62)

if __name__ == "__main__":
    t = Thread(target=run_faucet)
    t.start()
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
    
