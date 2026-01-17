import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_signal(trade):
    msg = (
        f"📊 {trade['symbol']}\n"
        f"Direction: {trade['direction']}\n"
        f"Entry: {trade['entry']}\n"
        f"SL: {trade['stop']}\n"
        f"TP: {trade['target']}\n"
        f"RR: {trade['rr']}\n"
        f"Lot: {trade['lot']}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})
