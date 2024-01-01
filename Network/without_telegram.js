const TelegramBot = require('node-telegram-bot-api');
const { exec } = require('child_process');

const token = '6509035885:AAFyCd3tni_llhte9fap7JMFy7LEQg8wkgo';
const bot = new TelegramBot(token, { polling: true });

function checkOpenPorts(target) {
    return new Promise((resolve, reject) => {
      exec(`sudo nmap -p- --open ${target}`, (error, stdout, _stderr) => {
        if (error) {
          reject(error);
          return;
        }
  
        const openPorts = stdout
          .split('\n')
          .filter(line => line.includes('/tcp'))
          .map(line => {
            const parts = line.trim().split(/\s+/);
            return parts[0];
          });
        console.log(`Open ports on ${target}:\n\n${openPorts.join('\n')}`)
        resolve(`Open ports on ${target}:\n\n${openPorts.join('\n')}`);
      });
    });
  }
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, "Hello! Send me an IP address or website, and I'll check its open ports.");
});

bot.onText(/.*/, async (msg) => {
  const chatId = msg.chat.id;
  const target = msg.text.trim();

  try {
    const openPortsInfo = await checkOpenPorts(target);
    bot.sendMessage(chatId, openPortsInfo);
  } catch (error) {
    bot.sendMessage(chatId, `Error checking open ports: ${error.message}`);
  }
});