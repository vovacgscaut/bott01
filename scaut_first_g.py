import telebot

token = '6  '

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    mess="Привет,на манеже-одни и те же"
    if message.text==message.from_user.first_name:
        bot.send_message(message.chat.id,mess ) 
    else:     
        bot.send_message(message.chat.id,message.text )
bot.polling(none_stop=True)