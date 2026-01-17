import time
from config import SYMBOLS, BALANCE, RISK_PERCENT, SCAN_INTERVAL_SECONDS
from strategy import analyze_symbol
from telegram_alerts import send_signal

def run():
    while True:
        for symbol in SYMBOLS:
            trade = analyze_symbol(symbol, BALANCE, RISK_PERCENT)
            if trade:
                send_signal(trade)
        time.sleep(SCAN_INTERVAL_SECONDS)

if __name__ == "__main__":
    run()

