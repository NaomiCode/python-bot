import os
import pprint

import pymongo.typings
from dotenv import load_dotenv
import telebot
from pymongo import MongoClient

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
client = MongoClient("localhost", 27017)
space = client["space-x-bot"]
users = space["users"]


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    tg_data = message.chat
    user_id = message.chat.id
    ref_from_id = tg_data.id if message.text == "/start" else int(message.text.split()[1])

    user_data = users.find_one({"user_id": user_id})
    if user_data is None:
        user = {"user_id": tg_data.id, "name": tg_data.first_name, "username": tg_data.username,
                "birthday": tg_data.birthdate,
                "ref from user": ref_from_id,
                "balance": 0, "multi tap": 1, "limit": 1, "speed": 1, "tap bot": False, "guru": 3, "refill": 3,
                "last click": None, "amount": 0, "league": 0, "energy": 500, "claimed_ref": [], "claimed_tasks": [],
                "total_click": 0, "ip": None}
        users.insert_one(user)

        if ref_from_id != user_id:
            users.find_one_and_update({'user_id': ref_from_id}, {"$addToSet": {"ref to user": user_id}})


if __name__ == '__main__':
    bot.polling(none_stop=True)
