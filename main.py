from telegram import *
import telegram.ext

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text(
        'Join Discord Server And Follow My Instagram',
    )

def help(update, content):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome message
    /help -> Help messages
    /contact -> Information about contac
    """)

def contact(update, content):
    update.message.reply_text("You can contact Akio in Discord!")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))

updater.start_polling()
updater.idle()