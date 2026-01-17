import websocket, json

def get_candles(symbol, granularity, count=300):
    ws = websocket.create_connection(
        f"wss://ws.derivws.com/websockets/v3?app_id=1089"
    )

    payload = {
        "ticks_history": symbol,
        "style": "candles",
        "granularity": granularity,
        "count": count
    }

    ws.send(json.dumps(payload))
    data = json.loads(ws.recv())
    ws.close()

    return data["candles"]

