#%%
import pandas as pd

df = pd.read_json('https://raw.githubusercontent.com/nmelgar/tickers-web-scrap-python/refs/heads/main/stock_tickers_data.json')

print(df.to_string()) 
# %%
