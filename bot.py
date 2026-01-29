import asyncio
import os
import csv
import random
from twikit import Client

async def main():
    client = Client('en-US')
    
    try:
        # 1. Login con tus Secrets
        await client.login(
            auth_info_1=os.environ.get('X_USERNAME'),
            auth_info_2=os.environ.get('X_EMAIL'),
            password=os.environ.get('X_PASSWORD')
        )

        # 2. Leer tu CSV de frases y keywords
        frases_data = []
        with open('lyrics.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                frases_data.append(row)

        if not frases_data:
            print("El archivo CSV está vacío.")
            return

        # 3. Lógica de publicación diaria (Frase al azar)
        # Elegimos una fila al azar de tu lista
        seleccionada = random.choice(frases_data)
        tweet_text = seleccionada['Frase']

        # 4. PUBLICAR
        await client.create_tweet(text=tweet_text)
        print(f"Publicado: {tweet_text}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
