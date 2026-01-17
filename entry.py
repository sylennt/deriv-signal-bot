def entry_signal(df, trend, sr):
    last = df.iloc[-1]

    if trend == "bullish" and last["low"] <= sr["support"]:
        return "buy", last["close"]

    if trend == "bearish" and last["high"] >= sr["resistance"]:
        return "sell", last["close"]

    return None, None

