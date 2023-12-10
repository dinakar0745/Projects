import logging
import socket
import nmap
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your Telegram Bot Token
TOKEN = '6509035885:AAFyCd3tni_llhte9fap7JMFy7LEQg8wkgo'

# Function to get IP details
def get_ip_details(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    try:
        # Get the IP address from the user's message
        ip_address = context.args[0]

        # Check if the IP address is valid
        try:
            socket.inet_aton(ip_address)
        except socket.error:
            update.message.reply_text("Invalid IP address format.")
            return

        # Check if the IP address is reachable
        reachable = is_ip_reachable(ip_address)

        if reachable:
            # Get port details using nmap
            ports = get_open_ports(ip_address)
            update.message.reply_text(f"IP: {ip_address}\nReachable: Yes\nOpen Ports: {', '.join(map(str, ports))}")
        else:
            update.message.reply_text(f"IP: {ip_address}\nReachable: No")

    except IndexError:
        update.message.reply_text("Please provide an IP address.")
    except Exception as e:
        logging.error(f"Error: {e}")
        update.message.reply_text("An error occurred while processing the request.")

# Function to check if IP is reachable
def is_ip_reachable(ip_address):
    try:
        socket.create_connection((ip_address, 80), timeout=5)
        return True
    except (socket.timeout, socket.error):
        return False

# Function to get open ports using nmap
def get_open_ports(ip_address):
    scanner = nmap.PortScanner()
    scanner.scan(ip_address, arguments='-O -sS -p 1-1000 --open')
    open_ports = [port for port in scanner[ip_address]['tcp'] if scanner[ip_address]['tcp'][port]['state'] == 'open']
    return open_ports

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater('YOUR_TELEGRAM_BOT_TOKEN')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command handler
    dp.add_handler(CommandHandler("ipdetails", get_ip_details))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal (Ctrl-C) to stop the bot
    updater.idle()

if __name__ == '__main__':
    main()
