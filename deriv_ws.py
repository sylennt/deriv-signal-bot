import websocket
import json

DERIV_WS_URL = "wss://ws.derivws.com/websockets/v3?app_id=1089"

def get_candles(symbol, timeframe, count=300):
    ws = websocket.create_connection(DERIV_WS_URL)

    payload = {
        "ticks_history": symbol,
        "style": "candles",
        "granularity": timeframe,
        "count": count
    }

    ws.send(json.dumps(payload))
    response = json.loads(ws.recv())
    ws.close()

    # Handle Deriv errors safely
    if "error" in response:
        print(f"[Deriv Error] {symbol}: {response['error']['message']}")
        return []

    if "candles" not in response:
        print(f"[Deriv Warning] No candles returned for {symbol}")
        return []

    return response["candles"]

