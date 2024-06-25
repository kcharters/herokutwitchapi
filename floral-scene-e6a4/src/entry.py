from twitchAPI.twitch import Twitch
import asyncio


async def twitch_example():

    twitch = await Twitch(env.CLIENT_ID, env.CLIENT_SECRET)

# run this example
asyncio.run(twitch_example())
