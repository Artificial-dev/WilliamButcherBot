HEROKU = False  # NOTE Make it false if you're not deploying on heroku.

if HEROKU:
    from os import environ

    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    API_ID = int(environ.get("API_ID", 6))
    API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION_STRING = environ.get("SESSION_STRING", None)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", None)
    SUDO_USERS_ID = list(int(x) for x in environ.get("SUDO_USERS_ID", "").split())
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
    FERNET_ENCRYPTION_KEY = environ.get("FERNET_ENCRYPTION_KEY", None)
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
    MONGO_DB_URI = environ.get("MONGO_DB_URI", None)
    ARQ_API_URL = environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
else:
    BOT_TOKEN = "2057510429:AAHztwMDNuKL0lKKCm4r8kYI8TjjuFv3EPE"
    API_ID = 8675599
    API_HASH = "fbb92e01e221f45920e63eb7000e4e38"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+919172303300"  # Need for Helper Userbot
    SUDO_USERS_ID = [
        2037016301,
        1734774195,
    ]  # Sudo users have full access to everythin, don't trust anyone
    LOG_GROUP_ID = -100791465910
    GBAN_LOG_GROUP_ID = -100791465910
    MESSAGE_DUMP_CHAT = -100659497913
    FERNET_ENCRYPTION_KEY = (
        "iKMq0WZMnJKjMQxZWKtv-cplMuF_LoyshXj0XbTGGWM="  # Leave this as it is
    )
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_DB_URI = "mongodb+srv://Artificialuser1:Artificialuser1@cluster0.xbnnc.mongodb.net/cluster0?retryWrites=true&w=majority"
    ARQ_API_KEY = "XAWHVD-NETMAO-CXXKCG-WNNVUP-ARQ"
    # NOTE Don't make changes below this line
    ARQ_API_URL = "http://thearq.tech"
