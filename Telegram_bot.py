from telegram.ext import *
from telegram import Update
import responses as re

# Indicate starting
print("let's go")

# Bot token
api = '1900786729:AAH4qtdXzL4WwndpXWABExJtFJtCWPb7E3g'




# Commands
def start_command(update, context):
    '''
    Function for the "/start" commands

    variables:
    update:
    context:
    '''
    update.message.reply_text("I am very limited so far but soon I'll be able to share information about the stock market")

def help_command(update: Update, context: CallbackContext) -> None:
    '''
    Function for the "/help" command. Sends information about the possible commands and the bot itself

    variables:
    update:
    context:
    '''
    update.message.reply_text("I can not help you")




def photo_sender(update: Update, context: CallbackContext) -> None:
    '''
    Function to send photos from url/local path to chat

    variables:
    update:
    context:
    '''

    # Fetches individual id from user
    chat_id = update.message.chat.id
    # Copies photo into chat using the bots function with a path or a url as second argument
    update.message.bot.send_photo(chat_id, open("cat.jpg", "rb"))




#message_handler
def message_receiver(update: Update, context: CallbackContext) -> None:
    '''
    Passes the user input to responses to get the output of the bot.

    '''
    # Format input
    # "update.message.text" stores user input
    user_input = str(update.message.text).lower()
    # Compute response
    resp = re.response(user_input)

    # Pass response to bot
    update.message.reply_text(resp)




# Sends input from user back to him
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
    # Messages with "/"
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Callt send_photo function for specific string (in chat /b)
    # 1. Argument könnte noch durch variable ersetzt werden um nicht für jedes Stichwort neuen handler haben zu müssen
    dispatcher.add_handler(CommandHandler("btc", help_command))

    # Message handler
    # Filters for text and not command inputs
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_receiver))

    # Error handler
    dispatcher.add_error_handler(error)

    # Let bot fetch for input from telegram
    bot.start_polling()
    bot.idle()




main()
