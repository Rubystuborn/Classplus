import os

API_ID = API_ID = 22263567

API_HASH = os.environ.get("API_HASH", "258fb6f6cdfa8220b74a4a6753b2ece6")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6529951387:AAHplnSk8yO0mSeS36q9Lsn5MUA7ZIFN55k")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6446062004))

LOG = -1001833358236

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1311808931").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


