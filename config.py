from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/ebcf5d6354a44ff833cc7.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/ebf34649780915d5951fe.jpg")

SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BRANDED_WORLD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BRANDED_KHUSHI")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "FirstOwner82_bot")  

FAILED = "https://te.legra.ph/file/6a4ac076ff159bdcf9656.jpg"
