def entry_price(df, direction):
    candle = df.iloc[-1]
    return candle["close"]
