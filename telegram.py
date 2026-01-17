import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_signal(trade):
    message = f"""
📊 {trade['symbol']}
📌 {trade['direction'].upper()}
Entry: {trade['entry']}
SL: {trade['stop']}
TP: {trade['target']}
RR: {trade['rr']}
Lot: {trade['lot']}
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    })

