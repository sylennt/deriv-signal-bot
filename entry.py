def find_entry(candles_15m, candles_5m, support, resistance, direction):
    """
    Checks for:
    1) Liquidity sweep on 15M
    2) Entry confirmation on 5M

    Returns:
        dict with entry info or None
    """

    last_15m = candles_15m[-1]
    last_5m = candles_5m[-1]

    # BUY logic
    if direction == "BUY":
        # Liquidity sweep below support
        if last_15m["low"] < support and last_15m["close"] > support:
            # 5M confirmation candle
            if last_5m["close"] > last_5m["open"]:
                return {
                    "direction": "BUY",
                    "entry": last_5m["close"],
                    "sweep_low": last_15m["low"]
                }

    # SELL logic
    if direction == "SELL":
        # Liquidity sweep above resistance
        if last_15m["high"] > resistance and last_15m["close"] < resistance:
            # 5M confirmation candle
            if last_5m["close"] < last_5m["open"]:
                return {
                    "direction": "SELL",
                    "entry": last_5m["close"],
                    "sweep_high": last_15m["high"]
                }

    return None


