import asyncio
import requests
from bs4 import BeautifulSoup

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import RpcCallFailError
from telethon import functions

from .credentials import API_ID, API_HASH, SESSION_FILE_NAME

async def safe_api_request(coroutine, comment):
    try:
        return await coroutine
    except RpcCallFailError as e:
        print(f"Telegram API error for {comment}: {e}")
    except Exception as e:
        print(f"Unexpected error for {comment}: {e}")

async def get_similar_channels(channel):
    async with TelegramClient(SESSION_FILE_NAME, API_ID, API_HASH) as bot:
        return await safe_api_request(
            bot(functions.channels.GetChannelRecommendationsRequest(channel=channel)),
            'get channels')

# Assuming the Maltego method calls are handled elsewhere in the code:
# response = MaltegoTransform()
# channel_name = "someChannel"

# We create an event loop outside of the function call
loop = asyncio.get_event_loop()
# Now we use the asyncio.run() which handles the event loop lifecycle for us
# Note: This method runs the passed coroutine and closes the loop.
similar_channels = loop.run_until_complete(get_similar_channels(channel_name))

# Further processing would be similar to the original
# You might need to adjust the aspect considering `similar_channels` async retrieval
