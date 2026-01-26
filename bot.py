import tweepy
import pandas as pd
import random
import os

# Sacamos las llaves de los "Secrets" de GitHub
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_secret = os.environ["ACCESS_SECRET"]

# Autenticación
client = tweepy.Client(
    consumer_key=api_key, consumer_secret=api_secret,
    access_token=access_token, access_token_secret=access_secret
)

def tuit_diario():
    try:
        # Cargamos las frases
        df = pd.read_csv('lyrics.csv')
        # Elegimos una al azar
        lyric = random.choice(df['Frase'].values)
        # Publicamos
        client.create_tweet(text=lyric)
        print(f"Publicado: {lyric}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    tuit_diario()
