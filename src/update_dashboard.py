import asyncio
import websocket
import json
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class DashboardData(BaseModel):
    timestamp:str
    metric:float

    @app.get("/dashboard")
    @staticmethod
    def get_dashboard_data():
        # data = df.reset_index().to_dict("records")
        # return {"data", data}
        pass

    @staticmethod
    async def update_dashboard(ws):
        while True:
            data = await DashboardData.get_dashboard_data()
            await ws.send(json.dumps(data))
            await asyncio.sleep(5)

    def on_message(ws,message):
        # handle incoming websocket message from the front-end
        pass

    def on_error(ws,error):
        print(f"WebSocket error: {error}")

    def on_close(ws):
        print("WebSocket connection closed")

    def on_open(ws):
        asyncio.get_event_loop().create_task(DashboardData.update_dashboard(ws))
        ws = websocket.WebSocketApp(
            "ws://localhost:8000/ws",
            on_message=DashboardData.on_message
            on_error=DashboardData.on_error
            on_close=DashboardData.on_close
        )
        ws.on_open = DashboardData.on_open
        ws.run_forever()


    