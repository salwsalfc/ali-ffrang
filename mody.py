import os


class Mody(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 25281175))

    API_HASH = os.environ.get("API_HASH", "6d99cb2b60a2c519fc1f99bd19565730")
    
    USER_NAME = os.environ.get("USER_NAME", "")
    
    SESSION = os.environ.get("SESSION", "")

    BOT_USER = os.environ.get("BOT_USER", "")

    VIA_USER = os.environ.get("VIA_USER", "")

    MENTION = os.environ.get("MENTION", "")
