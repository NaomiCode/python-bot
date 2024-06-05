import pymongo

client_db = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client_db["space-x-bot"]
users_col = mydb["users"]

mydict = {"user_id": 4845151, "name": "mina", "balance": 1000, "referred_by_id": 4845151, "referred_by_name": "Alice",
          "friends": [4845151, 4845152, 4845153], "multi-tap": 1, "limit": 1, "speed": 1, "tap-bot": True, "guru": 2,
          "refill": 1, "last_click": 12324134, "amount": 3241264545, "league": 2, "energy": 254,
          "claimed_ref": [213, 12, 4], "claimed_tasks": [43], "total_click": 241241424,"ip":"127.0.0.1"}

x = users_col.insert_one(mydict)
