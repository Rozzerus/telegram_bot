import telebot
import os

token = os.environ['ROWER_BOT_TOKEN']
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "Привет":
        bot.send_message(chat_id=message.chat.id, text="Привет, чем я могу тебе помочь?")
    elif "бот скажи: " in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text=message.text.split(":", 1)[1])
    elif "пиво" in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text="пива нет но ты держись")
    elif "греб" in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text="да гребу я! гребу!")
    elif "бот" in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text="бот дартаньян, все пи*расы")


bot.polling(none_stop=True, interval=0)
