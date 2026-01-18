def detect_trend(df):
    highs = df["high"].tail(20)
    lows = df["low"].tail(20)

    if highs.is_monotonic_increasing and lows.is_monotonic_increasing:
        return "bullish"

    if highs.is_monotonic_decreasing and lows.is_monotonic_decreasing:
        return "bearish"

    return "range"


def support_resistance(df):
    recent = df.tail(50)

    support = recent["low"].min()
    resistance = recent["high"].max()

    return {
        "support": support,
        "resistance": resistance
    }

