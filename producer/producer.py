import asyncio
import json
import requests
import websockets
from datetime import datetime

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=41.0015&longitude=39.7178&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

WS_URL = "ws://127.0.0.1:8000/ws"


async def send_weather_data():
    while True:
        try:
            response = requests.get(API_URL)
            data = response.json()

            current = data["current"]

            weather_data = {
                "city": "Trabzon",
                "temperature": current["temperature_2m"],
                "humidity": current["relative_humidity_2m"],
                "wind_speed": current["wind_speed_10m"],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            async with websockets.connect(WS_URL) as websocket:
                await websocket.send(json.dumps(weather_data))
                reply = await websocket.recv()
                print("Server cevabı:", reply)
                print("Gönderilen veri:", weather_data)

        except Exception as e:
            print("Hata oluştu:", e)

        await asyncio.sleep(10)


asyncio.run(send_weather_data())