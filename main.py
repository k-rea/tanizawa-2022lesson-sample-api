from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv('./data/L01-2022P-2K_13.csv', header=0, encoding='cp932')
df['緯度'] = df['緯度'] // 3600 + (df['緯度'] % 3600) // 60 / 60 + (df['緯度'] % 60 / 3600)
df['経度'] = df['経度'] // 3600 + (df['経度'] % 3600) // 60 / 60 + (df['経度'] % 60 / 3600)


@app.get("/")
async def root(n: float, e: float, s: float, w: float):
    _df = df[
        (df['緯度'] <= n) &
        (df['経度'] <= e) &
        (df['緯度'] >= s) &
        (df['経度'] >= w)
        ]
    return {
        "message": 'hello world',
        "query": f'n:{n}, e:{e}, s:{s}, w:{w}',
        "length": _df.shape[0],
        "data": _df.to_dict(orient='records')
    }
