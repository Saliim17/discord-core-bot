import random
from asyncio import sleep
from discord.utils import get
from discord import Client

from .messages import algorithm, ac, paco_ailajas, suspender, mejor, ayuda, bot
from .reply import starter_ac, starter_paco, starter_algorithms


class Own_client(Client):

    async def on_ready(self):
        print('{0} is UP!'.format(self.get_user(916302218997694505)))

    async def message_reaction(self, msg):
        msg1 = await msg.channel.send("Select language")
        await msg1.add_reaction("🇪🇸")
        await msg1.add_reaction("🇺🇸")

        cache_msg = get(self.cached_messages, id=msg1.id)
        await sleep(10)
        reaction = cache_msg.reactions

        for r in reaction:
            # https://discordpy.readthedocs.io/en/stable/api.html?highlight=add_reaction#discord.AsyncIterator
            async for u in r.users():
                print(type(u))
                # error con:
                # discord.errors.HTTPException: 400 Bad Request (error code: 50007): Cannot send messages to this user
                if r.emoji == "🇪🇸":
                    await u.send(content="Buenos dias puto gilipollas")

                if r.emoji == "🇺🇸":
                    await u.send(content="Buenos dias puto gilipollas en ingles :D")

    async def on_message(self, message):
        # If the author of the message is bot, we do nothing.
        if message.author == Client.user:
            return

        msg = message.content
        # if msg.startswith(''):
        #   await message.channel.send('Hello!')

        if any(word in msg for word in ayuda) or any(word in msg for word in bot):
            await self.message_reaction(message)

        if any(word in msg for word in algorithm) and any(word in msg for word in suspender):
            await message.channel.send(random.choice(starter_algorithms))

        if any(word in msg for word in ac) and any(word in msg for word in suspender):
            await message.channel.send(random.choice(starter_ac))

        if any(word in msg for word in paco_ailajas) and any(word in msg for word in mejor):
            await message.channel.send(random.choice(starter_paco))
