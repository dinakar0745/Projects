const axios = require('axios');

// Replace 'YOUR_BOT_TOKEN' with your actual Telegram Bot API token
const botToken = '6522128577:AAG8UIuJpFNOgJw5hBVG7Tfr2jNJytncRt4';
const chatId = '5401582830'; // Replace with the chat ID of the recipient

const sendMessage = async (text) => {
  try {
    const response = await axios.post(`https://api.telegram.org/bot${botToken}/sendMessage`, {
      chat_id: chatId,
      text: text,
    });

    if (response.data.ok) {
      console.log('Message sent successfully:', text);
    } else {
      console.error('Failed to send message:', response.data);
    }
  } catch (error) {
    console.error('Error sending message:', error);
  }
};

// Example usage:
const messageText = 'Hello, this is a test message from your Telegram bot!';
sendMessage(messageText);
