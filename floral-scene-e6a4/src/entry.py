import asyncio
from os import getenv

from dotenv import load_dotenv
from twitchAPI.twitch import Twitch

load_dotenv()


async def twitch_example():

    twitch: Twitch = await Twitch(getenv("CLIENT_ID"), getenv("CLIENT_SECRET"))
    token =  twitch.get_app_token()
    return token
# run this example
asyncio.run(twitch_example())
