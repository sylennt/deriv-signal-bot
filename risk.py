def risk_model(entry, direction, levels, balance, risk_percent):
    if direction == "buy":
        stop = levels["support"]
        target = levels["resistance"]
    else:
        stop = levels["resistance"]
        target = levels["support"]

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
        "entry": round(entry, 2),
        "stop": round(stop, 2),
        "target": round(target, 2),
        "rr": rr,
        "lot": lot
    }
