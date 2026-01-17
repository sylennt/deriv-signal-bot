def trend_direction(candles):
    highs = [c["high"] for c in candles[-6:]]
    lows = [c["low"] for c in candles[-6:]]

    if highs[-1] > highs[0] and lows[-1] > lows[0]:
        return "BUY"
    if highs[-1] < highs[0] and lows[-1] < lows[0]:
        return "SELL"
    return None

