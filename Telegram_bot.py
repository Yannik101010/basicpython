from telegram.ext import *
from telegram import Update
import responses as re

# Indicate starting
print("let's go")




# Bot token
api = '1829949109:AAHFKQSs971wrW09KZhUM-l9A19e-Y6thFU'




# Commands
def start_command(update, context):
    '''
    Function fo the "/start" commands

    variables:
    update:
    context:
    '''
    update.message.reply_text("I am very limited so far but soon I'll be able to share information about the stock market")


def help_command(update, context):
    '''
    Function fo the "/help" command. Sends information about the possible commands and the bot itself

    variables:
    update:
    context:
    '''
    #update.message.reply_text("I can not help you")
    update.send_photo(message.chat.id, photo=open('catto.png', 'rb'))




#message_handler
def message_receiver(update: Update, context: CallbackContext) -> None:
    '''
    Passes the user input to responses to get the output of the bot
    '''
    # Format input
    # "update.message.text" stores user input
    user_input = str(update.message.text).lower()
    # Compute response
    resp = re.response(user_input)


    # Pass response to bot
    update.message.reply_text(resp)


# def echo(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(update.message.text)




def error(update, context):
    '''
    Outputs message in console if querie is unmatched.
    '''
    print("Bot received an unknown input")




def main():
    #Initialize bot
    bot = Updater(api, use_context = True)
    dispatcher = bot.dispatcher

    # Command handler
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Message handler
    # Filters for text and not command inputs
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_receiver))

    # Error handler
    dispatcher.add_error_handler(error)

    # Let bot fetch for input from telegram
    bot.start_polling()
    bot.idle()




main()
