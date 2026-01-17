def structure_levels(candles):
    highs = [c["high"] for c in candles[-80:]]
    lows = [c["low"] for c in candles[-80:]]

    resistance = max(highs)
    support = min(lows)

    return support, resistance

