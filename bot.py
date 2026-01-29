import asyncio
import os
import csv
import random
from twikit import Client

async def main():
    # 1. Configurar el cliente de Twikit
    client = Client('en-US')
    
    try:
        # 2. Iniciar sesión usando tus Secrets de GitHub
        # Estos datos los saca de la configuración que pusimos en el main.yml
        print("Intentando iniciar sesión en X...")
        await client.login(
            auth_info_1=os.environ.get('X_USERNAME'),
            auth_info_2=os.environ.get('X_EMAIL'),
            password=os.environ.get('X_PASSWORD')
        )
        print("✅ Sesión iniciada con éxito.")

        # 3. Leer tu base de datos lyrics.csv
        frases_data = []
        if not os.path.exists('lyrics.csv'):
            print("❌ Error: No se encontró el archivo lyrics.csv")
            return

        with open('lyrics.csv', mode='r', encoding='utf-8') as f:
            # DictReader usa la primera fila (Frase, Keyword) como nombres de columna
            reader = csv.DictReader(f)
            for row in reader:
                # Solo guardamos la fila si tiene contenido en la columna 'Frase'
                if row.get('Frase'):
                    frases_data.append(row)

        if not frases_data:
            print("❌ El archivo CSV está vacío o no tiene el formato correcto.")
            return

        # 4. Elegir una frase al azar de tu lista
        seleccionada = random.choice(frases_data)
        tweet_text = seleccionada['Frase'].strip()

        # 5. ¡PUBLICAR EL POST!
        print(f"Preparando post: {tweet_text}")
        await client.create_tweet(text=tweet_text)
        print(f"🚀 ¡Publicado con éxito en X!")

    except Exception as e:
        # Si hay un error (ej: contraseña mal o cuenta bloqueada), lo dirá aquí
        print(f"⚠️ Hubo un error durante la ejecución: {e}")

if __name__ == "__main__":
    asyncio.run(main())
