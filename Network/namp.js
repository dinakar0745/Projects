const TelegramBot = require('node-telegram-bot-api');
const { exec } = require('child_process');

const token = '6509035885:AAFyCd3tni_llhte9fap7JMFy7LEQg8wkgo';
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, "Hello! Send me an IP address, and I'll perform an nmap scan on it.");
});

bot.onText(/(\d+\.\d+\.\d+\.\d+)/, async (msg, match) => {
  const chatId = msg.chat.id;
  const ipAddress = match[1];

  try {
    const scanResult = await performNmapScan(ipAddress);
    bot.sendMessage(chatId, scanResult);
  } catch (error) {
    bot.sendMessage(chatId, `Error performing nmap scan: ${error.message}`);
  }
});

function performNmapScan(ipAddress) {
  return new Promise((resolve, reject) => {
    const command = `sudo nmap -O -p- ${ipAddress}`;

    exec(command, (error, stdout, stderr) => {
      if (error) {
        reject(error);
        return;
      }

      // Process the nmap result as needed
      const result = `Scan result for ${ipAddress}:\n\n${stdout}`;

      resolve(result);
    });
  });
}
