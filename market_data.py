import pandas as pd

def candles_to_df(candles):
    df = pd.DataFrame(candles)
    df["time"] = pd.to_datetime(df["epoch"], unit="s")
    df = df.rename(columns={
        "open": "open",
        "high": "high",
        "low": "low",
        "close": "close"
    })
    return df[["time", "open", "high", "low", "close"]]
