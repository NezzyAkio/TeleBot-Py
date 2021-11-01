from telegram import *
import telegram.ext

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text('Hello World🌎')

def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome message
    /help -> Help messages
    /contact -> Information about contac
    """,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Discord", url="https://example.com")],
            [InlineKeyboardButton(text="Support XeonTera", url="https://example.com")],
        ])
    )

def contact(update, context):
    update.message.reply_text("You can contact Akio in Discord or Instagram!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Discord", url="https://example.com")],
            [InlineKeyboardButton(text="Instagram", url="https://example.com")],
        ])
    )

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))

updater.start_polling()
updater.idle()

#=================#
## Coded by Akio ##
#=================#