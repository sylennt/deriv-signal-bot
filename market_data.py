import pandas as pd

def to_df(candles):
    df = pd.DataFrame(candles)
    df["time"] = pd.to_datetime(df["epoch"], unit="s")
    return df[["time", "open", "high", "low", "close"]]
