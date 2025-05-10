import os
import requests
import time

BOT_TOKEN = os.environ['BOT_TOKEN']
JOIN_URL = os.environ['JOIN_URL']

def get_updates(offset=None):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    if offset:
        url += f'?offset={offset}'
    return requests.get(url).json()

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        for update in updates.get('result', []):
            last_update_id = update['update_id'] + 1
            message = update.get('message', {}).get('text', '')
            if message == '/getbabylocation':
                print('Trigger received! Sending Join command...')
                requests.get(JOIN_URL)
        time.sleep(2)

if __name__ == '__main__':
    main()
