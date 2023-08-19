import telebot

TELEGRAM_KEY = '1715171950:AAEqzqxHhdJ63_U_3ArhP-UpYdY7P71zGk0'

bot = telebot.TeleBot(TELEGRAM_KEY)

@bot.message_handler(commands=["twitch"])
def twitch(mensagem):
    texto = "https://www.twitch.tv/beardev86"
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["youtube"])
def youtube(mensagem):
    texto = "https://www.youtube.com/channel/UCbiLJBtxHcw93K9aMaIc22g"
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["tiktok"])
def tiktok(mensagem):
    texto = "https://www.tiktok.com/@beardev1"
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["menu"])
def menu(mensagem):
    texto = """Menu
                /twitch
                /youtube
                /tiktok
                """
    bot.send_message(mensagem.chat.id, texto)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escreve algo cacietan
    """
    bot.send_message(mensagem.chat.id, texto)

bot.polling()