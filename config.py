# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28549267"))
API_HASH = getenv("API_HASH", "b2526517ed963b1951a811b24bc29a4e")
BOT_TOKEN = getenv("BOT_TOKEN", "7477970001:AAEG6bSxz6oE4U7YPVJmvAkhbElBPsiBebY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8054489757").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Mmanjhu:<db_password>@cluster0.ukzu1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002257814966"))
