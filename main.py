import pandas as pd
from binance.client import Client
import time

client = Client(api_key='ygLyQROn7y7SdNvMoJepOdhZJV4OJUPeq1hhYe2929CopY2ZqGREhnWnVy1FQMEs',  api_secret = 'aACSH2BCvZKNwp7bbQR5vtMOJAGMvJ8SUB2Cdfw5sBF1g8sRjhRevQfu6EYpssKC')

while True:
    tickers = client.get_all_tickers()
    dados = []

    for index in range(0, len(tickers)):
        simbol = []
        simbol.append(tickers[index]['symbol'])
        simbol.append(tickers[index]['price'])
        dados.append(simbol)

    df = pd.DataFrame(dados, columns=['Token', 'Preço'])

    BTCUSD = df.loc[df['Token'] == 'BTCUSDT'].drop_duplicates()
    print(BTCUSD)
    print("-" * 30)
    time.sleep(7)