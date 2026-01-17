import time
from config import SYMBOLS, BALANCE, RISK_PERCENT, SCAN_INTERVAL
from strategy import analyze
from telegram_alerts import send_signal

def run():
    while True:
        for symbol in SYMBOLS:
            trade = analyze(symbol, BALANCE, RISK_PERCENT)
            if trade:
                send_signal(trade)
        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    run()
