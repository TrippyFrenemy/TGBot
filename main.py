import requests
from datetime import datetime
import telebot
import secret_key


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    # print(response)
    sell_price = response["btc_usd"]["sell"]
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}$"


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the 'price' to find out the cost of BTC")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                bot.send_message(
                    message.chat.id,
                    get_data()
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "SMTH went wrong"
                )
        else:
            bot.send_message(
                message.chat.id,
                "Not an option"
            )
    bot.polling()


if __name__ == "__main__":
    telegram_bot(secret_key.TOKEN_TELGRAM_BOT)
