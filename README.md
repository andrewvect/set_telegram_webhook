# set_telegram_webhook
Simple script to set telegram webhook to local machine with ngrok when develop telegram bots

1. First you need to upload ngrok sctipt from here <a>https://ngrok.com</a> and add bash script in main directory.
2. After you need to add number your localhost application port and your token bot in file config.py
3. Run file run_ngrok.py (don't close shell window with process)
4. Run file set_web_hook.py it's delete old webhook and set new
