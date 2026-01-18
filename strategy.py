from deriv_ws import get_candles
from market_data import to_df
from structure import detect_trend, support_resistance
from liquidity import liquidity_sweep
from entry import entry_signal
from risk import build_trade


def analyze(symbol, balance, risk_percent):
    candles_4h = get_candles(symbol, 14400)
    candles_1h = get_candles(symbol, 3600)
    candles_15m = get_candles(symbol, 900)

    if not candles_4h or not candles_1h or not candles_15m:
        return None

    df_4h = to_df(candles_4h)
    df_1h = to_df(candles_1h)
    df_15m = to_df(candles_15m)

    trend_4h = detect_trend(df_4h)
    trend_1h = detect_trend(df_1h)

    # Trend alignment check
    if trend_4h != trend_1h or trend_4h == "range":
        return None

    sr = support_resistance(df_15m)
    sweep = liquidity_sweep(df_15m)

    if not sweep:
        return None

    direction, entry = entry_signal(df_15m, trend_4h, sr, sweep)
    if not direction:
        return None

    trade = build_trade(entry, direction, sr, balance, risk_percent)
    if not trade:
        return None

    trade["symbol"] = symbol
    trade["direction"] = direction

    return trade
