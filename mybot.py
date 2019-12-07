#bot commands '/start','/pi'
#bot questions 'Hi','How are you?','Fine','Who are you?','What is bot?','Who makes you?','Bye'
from telegram.ext import Updater
updater = Updater(token='994234344:AAGhFXvdPEkSGZB0LSSAbDLmaNY8DFiXL3Q', use_context=True)

dispatcher = updater.dispatcher


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def pi(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="pi = 3.1416")


from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

from telegram.ext import CommandHandler
pi_handler = CommandHandler('pi', pi)
dispatcher.add_handler(pi_handler)






updater.start_polling()

from telegram.ext import MessageHandler, Filters



def hi(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text='Hi There! ')

hi_handler = MessageHandler(Filters.regex('Hi'), hi)
dispatcher.add_handler(hi_handler)  

def how(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text='I am fine. And you?')

how_handler = MessageHandler(Filters.regex('How are you?'), how)
dispatcher.add_handler(how_handler)  

def fine(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text='Great!')

fine_handler = MessageHandler(Filters.regex('Fine'), fine)
dispatcher.add_handler(fine_handler)

def who(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text='I am a bot')

who_handler = MessageHandler(Filters.regex('Who are you?'), who)
dispatcher.add_handler(who_handler)

def bot(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text='An Internet bot, also known as a web robot, robot or simply bot, is a software application that runs automated tasks (scripts) over the Internet.[1] Typically, bots perform tasks that are both simple and structurally repetitive, at a much higher rate than would be possible for a human alone. The largest use of bots is in web spidering (web crawler), in which an automated script fetches, analyzes and files information from web servers at many times the speed of a human. More than half of all web traffic is made up of bots. (From Wikipedia)')

bot_handler = MessageHandler(Filters.regex('What is bot?'), bot)
dispatcher.add_handler(bot_handler)

def bye(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text='Have a Nice day! bye :)')

bye_handler = MessageHandler(Filters.regex('Bye'), bye)
dispatcher.add_handler(bye_handler) 

def make(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text='@pollob1563 and special Thanks for Google Code-In 2019(Fedora Project)')

make_handler = MessageHandler(Filters.regex('Who makes you?'), make)
dispatcher.add_handler(make_handler) 

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand your talk")

unknown_handler = MessageHandler(Filters.text, unknown)
dispatcher.add_handler(unknown_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


