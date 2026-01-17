def trade_levels(entry, direction):
    sl_points = 20

    if direction == "BUY":
        sl = entry - sl_points
        tp = entry + sl_points * 2
    else:
        sl = entry + sl_points
        tp = entry - sl_points * 2

    return sl, tp

