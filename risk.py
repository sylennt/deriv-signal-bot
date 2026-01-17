def build_trade(entry, direction, sr, balance, risk_percent):
    if direction == "buy":
        stop = sr["support"]
        target = sr["resistance"]
    else:
        stop = sr["resistance"]
        target = sr["support"]

    risk = abs(entry - stop)
    reward = abs(target - entry)

    if risk == 0:
        return None

    rr = round(reward / risk, 2)
    if rr < 1.5:
        return None

    risk_amount = balance * (risk_percent / 100)
    lot = round(risk_amount / risk, 2)

    return {
        "entry": entry,
        "stop": stop,
        "target": target,
        "rr": rr,
        "lot": lot
    }
