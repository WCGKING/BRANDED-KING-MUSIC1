from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/9db6ae360e0a7b833abff.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/3d0d7d23d3a7fb86b442e.jpg")

SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BRANDED_WORLD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BRANDRD_BOT")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "KHUSHI_MUSIC76_BOT")  
YOUTUBE_IMG_URL:"assets/Youtube.jpeg":
