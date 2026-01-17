from deriv_ws import get_candles
from market_data import to_df
from structure import detect_trend, structure_levels
from liquidity import liquidity_sweep
from entry import entry_price
from risk import risk_model

def analyze(symbol, balance, risk_percent):
    df_4h = to_df(get_candles(symbol, 14400))
    df_1h = to_df(get_candles(symbol, 3600))
    df_15m = to_df(get_candles(symbol, 900))
    df_5m = to_df(get_candles(symbol, 300))

    trend_4h = detect_trend(df_4h)
    trend_1h = detect_trend(df_1h)

    if trend_4h != trend_1h or trend_4h == "range":
        return None

    direction = "buy" if trend_4h == "bullish" else "sell"

    if not liquidity_sweep(df_5m, direction):
        return None

    levels = structure_levels(df_15m)
    entry = entry_price(df_5m, direction)

    trade = risk_model(entry, direction, levels, balance, risk_percent)
    if not trade:
        return None

    trade.update({
        "symbol": symbol,
        "direction": direction.upper()
    })

    return trade
