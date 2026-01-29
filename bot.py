import asyncio
import os
import csv
import random
from twikit import Client

async def main():
    client = Client('en-US')
    
    # Nombre del archivo donde guardaremos la sesión para que X no sospeche
    auth_file = 'cookies.json'
    
    try:
        # Intentamos cargar la sesión si ya existe
        if os.path.exists(auth_file):
            client.load_cookies(auth_file)
            print("Sesión cargada desde cookies.")
        else:
            print("Iniciando sesión por primera vez...")
            await client.login(
                auth_info_1=os.environ.get('X_USERNAME'),
                auth_info_2=os.environ.get('X_EMAIL'),
                password=os.environ.get('X_PASSWORD')
            )
            # Guardamos las cookies para la próxima vez
            client.save_cookies(auth_file)
            print("Sesión guardada.")

        # Leer tu archivo lyrics.csv
        frases_data = []
        with open('lyrics.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('Frase'):
                    frases_data.append(row['Frase'].strip())

        if frases_data:
            tweet_text = random.choice(frases_data)
            await client.create_tweet(text=tweet_text)
            print(f"✅ ¡Publicado!: {tweet_text}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
