from flask import Flask ,request
import requests
import os
from telegram import Bot, Update


app = Flask(__name__)
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook',methods=['POST'])

def webhook():
    data = request.get_json(force=True)
    
    update:Update = Update.de_json(data, bot)

    chat_id = update.messages.chat_id
    text = update.messages.text

    bot.send_message(chat_id, text)
    # print(data)

    return "Assalomu alaykum"