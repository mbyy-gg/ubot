import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "5676072619").split()))

API_ID = int(os.getenv("API_ID", "35555805"))

API_HASH = os.getenv("API_HASH", "2036d87324df9b0b88eb1959098e1525")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8171611549:AAFKHz0nBIhJ1ZNqmBf0gqNj1S2j5zJxPjk")

OWNER_ID = int(os.getenv("OWNER_ID", "5676072619"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "11aacacf-aed3-467d-a907-ec110f69412a")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://supermby:supermby@cluster0.qbtexy8.mongodb.net/?appName=Cluster0")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4628173231"))
