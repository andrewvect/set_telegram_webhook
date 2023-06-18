import json
import os
import time
import requests
from config import bot_token, additional_path


def ngrok_url():
    os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

    with open('tunnels.json') as data_file:
        datajson = json.load(data_file)

    ngrok_http = ""
    ngrok_https = ""
    for i in datajson['tunnels']:
        if i['public_url'][0:5] == "https":
            ngrok_https += i['public_url']
        else:
            ngrok_http += i['public_url']

    url_to_set_webhook = f"https://api.telegram.org/bot{bot_token}/setWebhook?url={ngrok_https}/{additional_path}"
    url_to_delete_webhook = f"https://api.telegram.org/bot{bot_token}/deleteWebhook?drop_pending_updates=True"
    print(url_to_set_webhook)

    return {"url_to_set_webhook": url_to_set_webhook, "url_to_delete_webhook": url_to_delete_webhook}


def set_webhook_to_tg_bot():
    a = ngrok_url()
    requests.get(a["url_to_delete_webhook"])
    print("webhook delete")
    time.sleep(2.5)
    requests.get(a["url_to_set_webhook"])
    print("webhook set")


if __name__ == "__main__":
    set_webhook_to_tg_bot()
