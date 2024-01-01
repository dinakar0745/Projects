import subprocess
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters, Updater



def check_open_ports(target):
    # Run the netstat command to check open ports
    result = subprocess.run(['netstat', '-lnt'], capture_output=True, text=True)
    open_ports_info = result.stdout

    return f'Open ports on {target}:\n\n{open_ports_info}'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! Send me an IP address or website, and I'll check its open ports.")

def handle_text(update: Update, context: CallbackContext) -> None:
    target = update.message.text.strip()
    open_ports_info = check_open_ports(target)

    # Send open ports information to the user
    update.message.reply_text(open_ports_info)

def main():
    updater = Updater(token='6509035885:AAFyCd3tni_llhte9fap7JMFy7LEQg8wkgo', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    text_handler = MessageHandler(Filters.TEXT & ~Filters.COMMAND, handle_text)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
