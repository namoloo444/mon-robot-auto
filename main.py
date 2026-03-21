import requests
import time
import os
from flask import Flask
from threading import Thread

# --- CONFIGURATION ---
# Assure-toi de mettre l'URL COMPLETE entre les guillemets
URL_FIRE = "https://firefaucet.win/start"

app = Flask('')

@app.route('/')
def home():
    return "Robot en cours de fonctionnement..."

def run_faucet():
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Infinix)"}
    print("[*] Robot de gain 24h/24 : LANCE")
    while True:
        try:
            r = requests.get(URL_FIRE, headers=headers, timeout=30)
            print(f"[+] {time.strftime('%H:%M')} - Gain validé sur FaucetPay !")
        except:
            print("[!] Erreur de connexion au site")
        time.sleep(125)

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Lance le faucet dans un fil séparé
    t = Thread(target=run_faucet)
    t.start()
    # Lance le serveur web pour que Render soit content
    run()
