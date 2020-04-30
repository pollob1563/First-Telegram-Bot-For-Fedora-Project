#bot commands '/start','/help'.'/covid_19'
#bot questions 'Hi','How are you?','Fine','Who are you?','What is bot?','Who makes you?','Bye'


from telegram.ext import Updater
updater = Updater(token='994234344:AAGes7bwQFXR1i76tfLaUEM5GZA0UPbzmtc', use_context=True)

dispatcher = updater.dispatcher
# #####################################          WEB Srcping     ##################################### 
import requests
from lxml import html

IEDCR_page=requests.get('https://www.iedcr.gov.bd/')
IEDCR_info = html.fromstring(IEDCR_page.content)

total_cases=IEDCR_info.xpath('/html/body/div/div[4]/table/tbody/tr[4]/td[4]/text()')

total_recovered = IEDCR_info.xpath('/html/body/div/div[5]/div[2]/center[2]/h3/text()')

total_death = IEDCR_info.xpath('/html/body/div/div[5]/div[4]/center[2]/h3/text()')

new_cases = IEDCR_info.xpath('/html/body/div/div[4]/table/tbody/tr[3]/td[4]/text()')

new_death=IEDCR_info.xpath('/html/body/div/div[5]/div[3]/center[2]/h3/text()')

new_recovered=IEDCR_info.xpath('/html/body/div/div[5]/div[1]/center[2]/h3/text()')

# #####################################          WEB Srcping     ##################################### 

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)             

from telegram.ext import CommandHandler

#Command

def start(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!. If you need help than, type '/help' at chat box.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def help(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello!\nYou can control me by sending these commands and questions:\n\n<i>Commands:</i>\n/start - Restart The bot\n/help - If you need help\n/covid_19 - Know COVID-19 live stats of BD\n\n<i>Questions:</i>\n\n<b>Hi</b>\n<b>How are you?</b>\n<b>Fine</b>\n<b>Who are you?</b>\n<b>What is bot?</b>\n<b>Who makes you?</b>\n<b>Covid-19</b>\n<b>Corona</b>\n<b>Bye</b>',parse_mode='HTML')

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def a(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='<b>COVID-19 Stats: Bangladesh</b>\n\nTotal Cases: ' + str(total_cases[0])+'\n\nTotal Recovered: '+str(total_recovered[0])+'\n\nTotal Deaths: '+str(total_death[0])+'\n\n<b>Today Stats: </b>\n\nNew Cases: '+str(new_cases[0])+'\n\nNew Recovered: '+str(new_recovered[0])+'\n\nNew Deaths: '+str(new_death[0])+'\n\nSource: IEDCR\n\n<b>Developed By NerdsLab</b>\n\n',parse_mode='HTML')

a_handler = CommandHandler('covid_19', a)
dispatcher.add_handler(a_handler)

#Message

from telegram.ext import MessageHandler, Filters

def hi(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hi There! ')

hi_handler = MessageHandler(Filters.regex(r"(?i)hi"), hi)
dispatcher.add_handler(hi_handler)  

def how(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='I am fine. And you?')

how_handler = MessageHandler(Filters.regex(r"(?i)How are you?"), how)
dispatcher.add_handler(how_handler)  

def fine(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='Great!')

fine_handler = MessageHandler(Filters.regex(r"(?i)Fine"), fine)
dispatcher.add_handler(fine_handler)

def who(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='I am a bot')

who_handler = MessageHandler(Filters.regex(r"(?i)Who are you?"), who)
dispatcher.add_handler(who_handler)

def bot(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='An Internet bot, also known as a web robot, robot or simply bot, is a software application that runs automated tasks (scripts) over the Internet.[1] Typically, bots perform tasks that are both simple and structurally repetitive, at a much higher rate than would be possible for a human alone. The largest use of bots is in web spidering (web crawler), in which an automated script fetches, analyzes and files information from web servers at many times the speed of a human. More than half of all web traffic is made up of bots. (From Wikipedia)')

bot_handler = MessageHandler(Filters.regex(r"(?i)What is bot?"), bot)
dispatcher.add_handler(bot_handler)

def bye(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='Have a Nice day! bye :)')

bye_handler = MessageHandler(Filters.regex(r"(?i)bye"), bye)
dispatcher.add_handler(bye_handler) 

def make(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='@pollob1563 and special Thanks for Google Code-In 2019(Fedora Project)')

make_handler = MessageHandler(Filters.regex(r"(?i)Who makes you?"), make)
dispatcher.add_handler(make_handler) 

def covid(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text='<b>COVID-19 Stats: Bangladesh</b>\n\nTotal Cases: ' + str(total_cases[0])+'\n\nTotal Recovered: '+str(total_recovered[0])+'\n\nTotal Deaths: '+str(total_death[0])+'\n\n<b>Today Stats: </b>\n\nNew Cases: '+str(new_cases[0])+'\n\nNew Recovered: '+str(new_recovered[0])+'\n\nNew Deaths: '+str(new_death[0])+'\n\nSource: IEDCR\n\n<b>Developed By NerdsLab</b>\n\n',parse_mode='HTML')

covid_handler = MessageHandler(Filters.regex(r"(?i)covid-19"), covid)
dispatcher.add_handler(covid_handler)
covid_handler = MessageHandler(Filters.regex(r"(?i)corona"), covid)
dispatcher.add_handler(covid_handler)

def unknown(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing') 
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

def unknown1(update, context):
    context.bot.send_chat_action(update.message.chat.id, 'typing')   
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand your talk")

unknown1_handler = MessageHandler(Filters.text, unknown1)
dispatcher.add_handler(unknown1_handler)

updater.start_polling()
