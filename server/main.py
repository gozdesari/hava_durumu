from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json
import sys

sys.path.append("../database")

from database import (
    create_table,
    insert_data,
    get_last_temperatures,
    create_analysis_table,
    insert_analysis
)

app = FastAPI()

create_table()
create_analysis_table()

@app.get("/")
def read_root():
    return {"message": "Server çalışıyor"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client bağlandı")

    try:
        while True:
            data = await websocket.receive_text()
            print("Gelen veri:", data)

            parsed_data = json.loads(data)
            insert_data(parsed_data)

            temps = get_last_temperatures()

            if temps:
                avg_temp = sum(temps) / len(temps)
                max_temp = max(temps)

                warning = "Normal"
                if parsed_data["temperature"] > 25:
                    warning = "Sıcaklık çok yüksek!"

                print(f"Ortalama sıcaklık: {avg_temp:.2f}")
                print(f"Max sıcaklık: {max_temp}")
                print(f"Uyarı: {warning}")

                insert_analysis(
                    avg_temp,
                    max_temp,
                    warning,
                    parsed_data["timestamp"]
                )

            await websocket.send_text(f"Veri alındı: {data}")

    except WebSocketDisconnect:
        print("Client bağlantıyı kapattı")