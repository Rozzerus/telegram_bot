import json
import os

import apiai
import telebot

bot_token = os.environ['ROWER_BOT_TOKEN']
dialogflow_token = os.environ['DIALOGFLOW_TOKEN']
bot = telebot.TeleBot(bot_token)

trigger_words = ['@rozzercatspamerbot', 'rowerbot', 'бот', 'кот', 'пиво', 'привет', 'пока', 'дом', 'дим', 'греб',
                 'галера', 'эй ', 'говно', 'обед', 'еда', 'гор', 'кур', 'ху', 'жен', 'нет']


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.chat.type == 'supergroup':
        if in_one_of_trigger_words(message.text):
            bot_say(message)
    else:
        bot_say(message)


def in_one_of_trigger_words(text):
    for trigger_word in trigger_words:
        if trigger_word in text.lower():
            return True
    return False


def bot_say(message):
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
