TOKEN = "OTY5ODY2OTMwMjcxOTUyOTA2.Ymzo9w.8NlPBwW6svm-D0tBE5oAROGWWbI"

PREFIX = "p!"

DATABASE_NAME = None
DATABASE_URL = None

OWNERS = [948472049221914675]
ADMINS = [948472049221914675]

import discord
INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.presences = True
INTENTS.members = True

import os
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"

MINIMUM_MEMBER_COUNT = 30


