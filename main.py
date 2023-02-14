# метод определения движения цены
# мы берём стоимость обоеих криптовалют в течении определённого времени
# далее мы сравниваем движение двух криптовалют
# если биткоин растёт, а эфир падает то эфир совершил собственное движение и при обратной ситуации



import threading

from tradingview_ta import TA_Handler

btc = TA_Handler(
    symbol="BTCUSDT",
    exchange="COINBASE",
    screener="crypto",
    interval="1m",
    timeout=None
)
eth = TA_Handler(
    symbol="ETHUSDT",
    exchange="COINBASE",
    screener="crypto",
    interval="1m",
    timeout=None
)
btch = TA_Handler(
    symbol="BTCUSDT",
    exchange="COINBASE",
    screener="crypto",
    interval="1m",
    timeout=None
)
ethh = TA_Handler(
    symbol="ETHUSDT",
    exchange="COINBASE",
    screener="crypto",
    interval="1m",
    timeout=None
)


def minute1():
    threading.Timer(61, minute1).start()
    ethp = eth.get_analysis().indicators["close"]
    btcp = btc.get_analysis().indicators["close"]
    return ethp, btcp


def hour1():
    threading.Timer(601, hour1).start()
    ethph = ethh.get_analysis().indicators["close"]
    return ethph


while True:
    ethph = hour1()
    ethp, btcp = minute1()
    btcn = btc.get_analysis().indicators["close"]
    ethn = eth.get_analysis().indicators["close"]
    ethhn = ethh.get_analysis().indicators["close"]
    if (btcp >= btcn and ethp < ethn) or (btcp <= btcn and ethp > ethn):
        print("собственное движение")
        if ethn > ethp:
            percent = 1 - (ethp / ethn)
            print(f"цена повысилась на {percent}%")
            print(ethp, btcp, ethph)
            print(ethn, btcn, ethhn)
            if percent >= 0.01:
                print("цена повысилась на 1% и более")
                print(ethp, btcp, ethph)
                print(ethn, btcn, ethhn)
        if ethn < ethp:
            percent = 1 - (ethn / ethp)
            print(f"цена понизилась на {percent}%")
            print(ethp, btcp, ethph)
            print(ethn, btcn, ethhn)
    else:
        print("изменений не произошло")
