<?php

// Replace 'YOUR_BOT_TOKEN' with your actual Telegram Bot API token
$botToken = '6596665027:AAE9TyAXpHEbw8YsNjY-nC1RggCmwVF5r9g';
$chatId = '1698583707'; // Replace with the chat ID of the recipient

// Function to send a message using the Telegram Bot API
function sendMessage($message) {
    global $botToken, $chatId;
    
    $url = "https://api.telegram.org/bot{$botToken}/sendMessage";
    $data = array(
        'chat_id' => $chatId,
        'text' => $message
    );
    
    $options = array(
        'http' => array(
            'method'  => 'POST',
            'header'  => 'Content-Type: application/x-www-form-urlencoded',
            'content' => http_build_query($data)
        )
    );
    
    $context  = stream_context_create($options);
    $result = file_get_contents($url, false, $context);
    
    if ($result === false) {
        echo "Failed to send message.";
    } else {
        echo "Message sent successfully: $message";
    }
}

// Example usage:
$messageText = "Hello, this is a test message from your Telegram bot!";
sendMessage($messageText);
