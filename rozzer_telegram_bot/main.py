import telebot
import os

token = os.environ['ROWER_BOT_TOKEN']
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "Привет":
        bot.send_message(chat_id=message.chat.id, text="Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(chat_id=message.chat.id, text="Напиши привет")
    elif "скажи" in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text="привет мир")
    elif "пиво" in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text="пива нет но ты держись")
    elif "греб" in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text="да гребу я! гребу!")
    elif "бот" in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text="бот дартаньян, все пи*расы")


bot.polling(none_stop=True, interval=0)
