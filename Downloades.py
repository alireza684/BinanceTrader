from binance.client import Client
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
api_key = "------"
secret = "------"
# now = datetime.utcnow()
# start = str(now - timedelta(days = 60))
start = str(pd.to_datetime(client._get_earliest_valid_timestamp("LINKUSDT", "15m"), unit = "ms")) # Replace "LINKUSDT" and "15m" with any currency pair and timeframe you want.
client = Client(api_key = api_key, api_secret = secret, tld = "com", testnet = False)
bars = client.futures_historical_klines(symbol = "LINKUSDT", interval = "15m",
                                        start_str = start, end_str = None, limit = 1000)
df = pd.DataFrame(bars)
df["Date"] = pd.to_datetime(df.iloc[:,0], unit = "ms")
df.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume",
                "Clos Time", "Quote Asset Volume", "Number of Trades",
                "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore", "Date"]
df = df[["Date", "Open", "High", "Low", "Close"]].copy()
df.set_index("Date", inplace = True)
for column in df.columns:
    df[column] = pd.to_numeric(df[column], errors = "coerce")
df.to_csv("LINKUSDT_15m.csv")
print("Done!")

