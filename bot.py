import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
@bot.messange_handler(content_types=['text'])
def lalala(massage):
	bot.send_massage(massage.chat.id, message.text)


bot.polling(none_stop=True)
