import os
import logging
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up your API token
API_TOKEN = '6688770369:AAE1aGeeF4T80tT-1Mn4Xx5DzkG4aiLPNpE'

# Set up a directory to store photos
PHOTO_DIRECTORY = 'photos'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your photo bot. Send me photos to store.')

# Function to handle photo messages
def save_photo(update: Update, context: CallbackContext) -> None:
    file_id = update.message.photo[-1].file_id
    file = context.bot.get_file(file_id)
    file.download(os.path.join(PHOTO_DIRECTORY, f"{file_id}.jpg"))
    update.message.reply_text('Photo saved successfully!')

# Function to handle the /showphoto command
def show_photo(update: Update, context: CallbackContext) -> None:
    photo_files = os.listdir(PHOTO_DIRECTORY)
    if not photo_files:
        update.message.reply_text('No photos to display.')
        return

    for photo_file in photo_files:
        context.bot.send_photo(update.message.chat_id, InputFile(os.path.join(PHOTO_DIRECTORY, photo_file)))

# Main function to start the bot
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, save_photo))
    dp.add_handler(CommandHandler("showphoto", show_photo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    if not os.path.exists(PHOTO_DIRECTORY):
        os.makedirs(PHOTO_DIRECTORY)
    main()
