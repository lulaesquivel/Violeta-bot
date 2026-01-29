import asyncio
import os
import csv
import random
from twikit import Client

async def main():
    # Usamos un agente de usuario que parezca un navegador real
    client = Client('en-US')
    
    try:
        print("Esperando unos segundos antes de iniciar...")
        await asyncio.sleep(random.randint(5, 15)) # Espera aleatoria para despistar
        
        await client.login(
            auth_info_1=os.environ.get('X_USERNAME'),
            auth_info_2=os.environ.get('X_EMAIL'),
            password=os.environ.get('X_PASSWORD')
        )

        frases_data = []
        with open('lyrics.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('Frase'):
                    frases_data.append(row['Frase'].strip())

        if frases_data:
            tweet_text = random.choice(frases_data)
            await client.create_tweet(text=tweet_text)
            print(f"✅ ¡Publicado con éxito!: {tweet_text}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
