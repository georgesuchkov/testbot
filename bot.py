import telebot

hero = {'pa': ['as', 'sd', 'sx'], 'ck': [1,2,3]}
bot = telebot.TeleBot('985438739:AAFzf4x7gyP7E4FIfpuE4kqR5_6Epneei68')

def mess(n):
    final = ''
    for i in hero[n]:
        final += i + ', '
    return final


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Салют, задротище')


@bot.message_handler(content_types=['text'])
def send_text(message):
    n = message.text.lower()
    bot.send_message(message.chat.id, mess(n))

bot.polling()
