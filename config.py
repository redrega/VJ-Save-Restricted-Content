import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7886646790:AAFtBA3by5MEQ4hksYPn8MEsdZX5Pr56JMc")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23453035"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7b6e03119294dcfdea301c5a415cb569")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1197919535"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://random345789:oyllrkfaQTyTsmcO@cluster0.ctuus.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
