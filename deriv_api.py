import websocket
import json

def get_candles(symbol, timeframe, count=300):
    ws = websocket.create_connection("wss://ws.derivws.com/websockets/v3?app_id=1089")

    payload = {
        "ticks_history": symbol,
        "style": "candles",
        "granularity": timeframe,
        "count": count
    }

    ws.send(json.dumps(payload))
    response = json.loads(ws.recv())
    ws.close()

    candles = response["candles"]
    return candles

