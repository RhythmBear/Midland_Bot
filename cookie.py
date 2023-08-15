import requests
import os
from dotenv import load_dotenv

load_dotenv()


def send_message_to_private_channel(bot_token, channel_username, message, recipient_user_id):
    """
    Send a message to a private Telegram channel.

    Args:
        bot_token (str): The token of your Telegram bot.
        channel_username (str): The username of the private channel (including the "@" symbol).
        message (str): The message to send.
        recipient_user_id (str): The User ID of the recipient within the private channel.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": channel_username,
        "text": message,
    }

    response = requests.post(api_url, data=data)

    if response.status_code == 200:
        return True
    else:
        print("Failed to send message:", response.text)
        return False


# Replace with your bot token and the private channel's username
bot_token = os.getenv("BOT_TOKEN")
private_channel_username = os.getenv("BOT_USERNAME")  # Replace with the private channel's username
message = "Hello, Testing 1, 2"
recipient_user_id = "RECIPIENT_USER_ID"  # Replace with the User ID of the recipient

# Send the message to the private channel
result = send_message_to_private_channel(bot_token, private_channel_username, message, recipient_user_id)
if result:
    print("Message sent to private channel successfully!")
else:
    print("Failed to send message to private channel.")
