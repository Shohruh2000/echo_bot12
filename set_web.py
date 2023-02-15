import requests
import os 
url = 'https://botechotest.pythonanywhere.com/webhook'

TOKEN = os.environ['TOKEN']

poyload = {
    'url':url
}

r = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook",params=poyload)

print(r.status_code)