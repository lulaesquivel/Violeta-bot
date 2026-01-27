import tweepy
import os
import pandas as pd
import random

def tuit_diario():
    try:
        # Autenticación estrictamente para v2 (Free)
        client = tweepy.Client(
            consumer_key=os.environ["API_KEY"],
            consumer_secret=os.environ["API_SECRET"],
            access_token=os.environ["ACCESS_TOKEN"],
            access_token_secret=os.environ["ACCESS_SECRET"]
        )

        # Leer archivo
        df = pd.read_csv('lyrics.csv')
        lyric = random.choice(df['Frase'].values)
        
        # Publicar (v2)
        print("Intentando publicar en v2...")
        client.create_tweet(text=lyric)
        print("¡Tuit enviado con éxito!")

    except Exception as e:
        print(f"Error detallado: {e}")

if __name__ == "__main__":
    tuit_diario()
