from deriv_ws import get_candles
from market_data import candles_to_df
from structure import detect_trend, find_support_resistance
from entry import entry_signal
from risk import build_trade

def analyze_symbol(symbol, balance, risk_percent):
    df_4h = candles_to_df(get_candles(symbol, 14400))
    df_1h = candles_to_df(get_candles(symbol, 3600))
    df_15m = candles_to_df(get_candles(symbol, 900))

    trend_4h = detect_trend(df_4h)
    trend_1h = detect_trend(df_1h)

    if trend_4h != trend_1h or trend_4h == "range":
        return None

    sr = find_support_resistance(df_15m)
    direction, entry = entry_signal(df_15m, trend_4h, sr)

    if not direction:
        return None

    trade = build_trade(entry, direction, sr, balance, risk_percent)
    if not trade:
        return None

    trade["symbol"] = symbol
    trade["direction"] = direction
    return trade
