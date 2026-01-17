def detect_trend(df):
    highs = df["high"].tail(30)
    lows = df["low"].tail(30)

    if highs.is_monotonic_increasing and lows.is_monotonic_increasing:
        return "bullish"
    if highs.is_monotonic_decreasing and lows.is_monotonic_decreasing:
        return "bearish"
    return "range"


def structure_levels(df):
    recent = df.tail(60)
    return {
        "support": recent["low"].min(),
        "resistance": recent["high"].max()
    }
