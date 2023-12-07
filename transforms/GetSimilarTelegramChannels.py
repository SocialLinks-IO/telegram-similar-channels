from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform

import asyncio
import requests

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import RpcCallFailError
from telethon import functions
from bs4 import BeautifulSoup

from .credentials import API_ID, API_HASH, SESSION_FILE_NAME

async def safe_api_request(coroutine, comment):
    result = None
    try:
        result = await coroutine
    except RpcCallFailError as e:
        print(f"Telegram API error, {comment}: {str(e)}")
    except Exception as e:
        print(f"Some error, {comment}: {str(e)}")
    return result


def get_similar_channels(channel):
    loop = asyncio.get_event_loop()
    bot = TelegramClient(SESSION_FILE_NAME, API_ID, API_HASH)

    with bot:
        result = loop.run_until_complete(safe_api_request(bot(functions.channels.GetChannelRecommendationsRequest(channel=channel)), 'get user photos'))
        return result


class GetSimilarTelegramChannels(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        channel_name = request.getProperty("alias")

        channels = get_similar_channels(channel_name).chats

        # print(channels)


        # Iterate through all returned Yellow Notices
        for ch in channels:
            channel = response.addEntity("maltego.telegram.channel")
            channel.addProperty("alias", value=ch.username)
            channel.addProperty("name", value=ch.title)
            channel.addProperty("channel_id", value=ch.id)

            image_page = requests.get(f'https://t.me/{ch.username}')
            soup = BeautifulSoup(image_page.text, 'html.parser')

            img_page = soup.find_all("img", class_="tgme_page_photo_image")

            if img_page:
                try:
                    image = img_page[0]['src']
                    channel.addProperty("profile-image", value=image)
                except:
                    pass

            # print(channel)
