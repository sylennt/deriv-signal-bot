def liquidity_sweep(candles_15m, support, resistance, direction):
    last = candles_15m[-1]

    if direction == "BUY":
        if last["low"] < support and last["close"] > support:
            return {
                "direction": "BUY",
                "sweep_low": last["low"]
            }

    if direction == "SELL":
        if last["high"] > resistance and last["close"] < resistance:
            return {
                "direction": "SELL",
                "sweep_high": last["high"]
            }

    return None


