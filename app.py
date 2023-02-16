from flask import Flask ,request
import requests
import os
from telegram import Bot, Update


app = Flask(__name__)
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook',methods=['POST','GET'])

def webhook():
    if request.method == 'GET':
        return 'Helo World'
    elif request.method == 'POST':

        data = request.get_json(force=True)
    
        update:Update = Update.de_json(data, bot)

        chat_id = update.message.chat_id
        text = update.message.text
        if text !=None:

            bot.send_message(chat_id, text)
        print(chat_id)

    return "Assalomu alaykum"