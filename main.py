from deriv_api import get_candles
from trend import trend_direction
from structure import structure_levels
from entry import liquidity_sweep, confirm_entry
from risk import trade_levels
from telegram import send
from config import SYMBOLS

def run():
    for symbol in SYMBOLS:
        tf_4h = get_candles(symbol, 14400)
        tf_1h = get_candles(symbol, 3600)
        tf_15m = get_candles(symbol, 900)
        tf_5m = get_candles(symbol, 300)

        direction = trend_direction(tf_4h)
        if not direction:
            continue

        support, resistance = structure_levels(tf_1h)

        sweep = liquidity_sweep(tf_15m, support, resistance, direction)
        if not sweep:
            continue

        if not confirm_entry(tf_5m, direction):
            continue

        entry = tf_5m[-1]["close"]
        sl, tp = trade_levels(entry, direction)

        send(f"""
📊 {symbol}

Direction: {direction}
Entry TF: 5M

Entry: {entry}
SL: {sl}
TP: {tp}
RR: 1:2
""")

