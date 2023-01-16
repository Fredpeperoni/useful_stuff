import requests
import sys

"""
This script contains functionality to send message in your bot after the information was given in STDIN.

You have to specify your own bot_token and bot_chatID in the script to use it.
(See the explanation here https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python)

After that you can add your bash scripts with something like and make notifications:

    echo "Process finished. You can check the results now." | python notify_finish.py
 

"""


def telegram_bot_sendtext(bot_message, bot_token='your bot token', bot_chatID='your bot chat ID'):

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json


if __name__=='__main__':

    bot_message = str(input())
    telegram_bot_sendtext(bot_message)
    print('Message sent.\n')
