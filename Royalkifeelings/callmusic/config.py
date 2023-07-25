from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME: str = getenv("SESSION_NAME", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
BOT_USERNAME = getenv("BOT_USERNAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/new_devil_world")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/sukoonkepal")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5977523092").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5977523092").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "12000"))
PMPERMIT = getenv("PMPERMIT", "ENABLE")
BOT_NAME = getenv("BOT_NAME","Kaal")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://graph.org/file/1c68560c186299b24ff8d.jpg"
)
