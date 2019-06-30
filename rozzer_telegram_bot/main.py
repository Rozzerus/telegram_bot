import os

import apiai
import json
import telebot

bot_token = os.environ['ROWER_BOT_TOKEN']
dialogflow_token = os.environ['DIALOGFLOW_TOKEN']
bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    request = apiai.ApiAI(dialogflow_token).text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot'
    request.query = message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=message.chat.id, text=response)
    else:
        bot.send_message(chat_id=message.chat.id, text='Я Вас не совсем понял!')


bot.polling(none_stop=True, interval=0)
