
from curses.ascii import SUB
from config import BOT_TOKEN,CHANNEL_ID,REDDIT_ID,REDDIT_SECRET
from aiogram import Bot, types
import asyncpraw
import asyncio
import random


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)


reddit = asyncpraw.Reddit(
    client_id=REDDIT_ID,
    client_secret=REDDIT_SECRET,
    user_agent="random_reddit_bot/0.0.1",
)

print(reddit)



posted = []
TIMEOUT = 60
SUBREDDIT_NAME = ['wholesomeanimemes','Animemes','anime_irl', 'animenocontext', "goodanimemes"]
POST_LIMIT = 1


async def send_message(channel_id: int, text: str, post_url: str):
    await bot.send_photo(channel_id,post_url, text)



async def main():
    while True:
        await asyncio.sleep(TIMEOUT)
        sub_name = random.choice(SUBREDDIT_NAME)
        memes_submission = await reddit.subreddit(sub_name)
        memes_submission = memes_submission.new(limit=POST_LIMIT)
        item = await memes_submission.__anext__()
        if item.title not in posted:
            posted.append(item.title)
            try:
                await send_message(CHANNEL_ID,item.title, item.url)
            except Exception as err:
                bot.send_message(682382931, err)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
















