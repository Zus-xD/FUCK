from os import getenv

que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ")
BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "PyXen")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AltronChats")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/e22fb003bdbb83a96288c.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e22fb003bdbb83a96288c.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))
