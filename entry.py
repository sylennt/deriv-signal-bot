def liquidity_sweep(candles_15m, support, resistance, direction):
    last = candles_15m[-1]

    if direction == "BUY" and last["low"] < support and last["close"] > support:
        return "BUY"

    if direction == "SELL" and last["high"] > resistance and last["close"] < resistance:
        return "SELL"

    return None


def confirm_entry(candles_5m, direction):
    c = candles_5m[-1]

    if direction == "BUY" and c["close"] > c["open"]:
        return True
    if direction == "SELL" and c["close"] < c["open"]:
        return True

    return False

