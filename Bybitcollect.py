from pybit.unified_trading import HTTP
import pandas as pd
import datetime as dt

KEY= ""
SECRET = ""

timeframe='60'
period=14

def collect_data():
    session = HTTP(
        api_key = KEY,
        api_secret = SECRET,
        testnet = False
    )

    response = session.get_kline(category='linear',
                                symbol = 'SOLUSDT',
                                interval=timeframe).get('result')

    data = response.get('list', None)
    
    if not data: 
        return
    data = pd.DataFrame(data,
                    columns =[
                        'timestamp',
                        'open',
                        'high',
                        'low',
                        'close',
                        'volume',
                        'turnover'
                        ],
                    )

    f = lambda x: dt.datetime.utcfromtimestamp(int(x)/1000)
    data.index = data.timestamp.apply(f)
    return data[::-1].apply(pd.to_numeric)

def calculate_rsi():
    df=collect_data()
    #
    df['gain'] = (df['close'] - df['open']).apply(lambda x: x if x > 0 else 0)
    df['loss'] = (df['close'] - df['open']).apply(lambda x: -x if x < 0 else 0)

    df['ema_gain'] = df['gain'].ewm(span=period, min_periods=period).mean()
    df['ema_loss'] = df['loss'].ewm(span=period, min_periods=period).mean()

    df['rs'] = df['ema_gain'] / df['ema_loss']

    df['rsi'] = 100 - (100 / (df['rs'] + 1))
    
    return df['rsi'].iloc[-1]

print(calculate_rsi())