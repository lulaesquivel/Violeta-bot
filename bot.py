import tweepy
import os
import pandas as pd
import random

def tuit_diario():
    try:
        # Autenticación
        client = tweepy.Client(
            consumer_key=os.environ["API_KEY"],
            consumer_secret=os.environ["API_SECRET"],
            access_token=os.environ["ACCESS_TOKEN"],
            access_token_secret=os.environ["ACCESS_SECRET"]
        )

        # Verificamos quién es el bot
        auth = tweepy.OAuth1UserHandler(
            os.environ["API_KEY"], os.environ["API_SECRET"],
            os.environ["ACCESS_TOKEN"], os.environ["ACCESS_SECRET"]
        )
        api = tweepy.API(auth)
        user = api.verify_credentials()
        print(f"Conectado como: {user.screen_name}")

        # Intentar tuitear
        df = pd.read_csv('lyrics.csv')
        lyric = random.choice(df['Frase'].values)
        client.create_tweet(text=lyric)
        print("¡Tuit enviado con éxito!")

    except Exception as e:
        print(f"Error detallado: {e}")

if __name__ == "__main__":
    tuit_diario()
