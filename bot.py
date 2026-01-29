import asyncio
import os
import csv
import random
from twikit import Client

async def main():
    client = Client('en-US')
    try:
        await client.login(
            auth_info_1=os.environ.get('X_USERNAME'),
            auth_info_2=os.environ.get('X_EMAIL'),
            password=os.environ.get('X_PASSWORD')
        )

        frases_data = []
        # Abrimos tu archivo lyrics.csv
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
