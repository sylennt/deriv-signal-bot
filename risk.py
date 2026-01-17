def trade_levels(entry, sweep_low, sweep_high, direction):
    buffer = 5

    if direction == "BUY":
        sl = sweep_low - buffer
        tp = entry + (entry - sl) * 2

    else:
        sl = sweep_high + buffer
        tp = entry - (sl - entry) * 2

    return sl, tp
