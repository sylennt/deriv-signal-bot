def liquidity_sweep(df, direction):
    highs = df["high"].tail(20)
    lows = df["low"].tail(20)
    last = df.iloc[-1]

    equal_high = highs.iloc[-2] == highs.iloc[-3]
    equal_low = lows.iloc[-2] == lows.iloc[-3]

    if direction == "sell" and equal_high:
        if last["high"] > highs.iloc[-2] and last["close"] < highs.iloc[-2]:
            return True

    if direction == "buy" and equal_low:
        if last["low"] < lows.iloc[-2] and last["close"] > lows.iloc[-2]:
            return True

    return False
