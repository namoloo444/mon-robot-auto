import requests
import time
import os
from flask import Flask
from threading import Thread

# --- CONFIGURATION ---
# Remplace par l'URL qui finit par /autofaucet/ si possible
URL_FIRE = "https://firefaucet.win"

app = Flask('')

@app.route('/')
def home():
    return "Robot de Namolo en cours..."

def run_faucet():
    # C'EST ICI QUE TU DOIS COLLER TON COOKIE
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Infinix)",
        "Cookie": "_ga=GA1.1.507508636.1774193934; _ga_62J3KC448K=GS2.1.s1774198477$o2$g1$t1774199588$j60$10$h0"
    }
    print("[*] Robot de gain 24h/24 : LANCE")
    while True:
        try:
            r = requests.get(URL_FIRE, headers=headers, timeout=30)
            print(f"[+] {time.strftime('%H:%M')} - Gain validé !")
        except:
            print("[!] Erreur de connexion")
        time.sleep(125)

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    t = Thread(target=run_faucet)
    t.start()
    run()

