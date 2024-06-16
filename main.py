from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
print(tradingview_ta.__version__)
# Example output: 3.1.3

handler = TA_Handler(
    symbol="",
    exchange="",
    screener="",
    interval="",
    timeout=None
)


class Interval:
    INTERVAL_1_MINUTE = "1m"
    INTERVAL_5_MINUTES = "5m"
    INTERVAL_15_MINUTES = "15m"
    INTERVAL_30_MINUTES = "30m"
    INTERVAL_1_HOUR = "1h"
    INTERVAL_2_HOURS = "2h"
    INTERVAL_4_HOURS = "4h"
    INTERVAL_1_DAY = "1d"
    INTERVAL_1_WEEK = "1W"
    INTERVAL_1_MONTH = "1M"

analysis = handler.get_analysis()
