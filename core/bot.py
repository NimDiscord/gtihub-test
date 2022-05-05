from datetime import datetime
import discord
from discord.ext import commands

import constants.config as config
import constants.constants as constants
import constants.colors as colors
import os



class Pokecord(commands.AutoShardedBot):
    def __init__(self):

        allowed_mentions = discord.AllowedMentions(
            roles=False, everyone=False, users=True)


        super().__init__(command_prefix="p!", case_insensitive=True, strip_after_prefix=True,
                         activity=discord.Game(name="p!help | v2.0.0"), intents=config.INTENTS, owner_ids=config.OWNERS, allowed_mentions=allowed_mentions)  # add help commmand NONe here

        # Load Extensions

    # async def get_prefix(self):
    #     pass

    async def start(self) -> None:
        await super().start(config.TOKEN, reconnect=True)

    async def on_shard_ready(self, shard_id: int):
        print(f"Discord version {discord.__version__}")
        print(f"Shard {shard_id} is ready")  # add logger and shard name here
        print(self.uptime)

    async def on_shard_resume(self, shard_id: int):
        # add logger and log the errors somewhere
        print(f"Shard {shard_id} has resumed")

    # Load Extensions
    async def setup_hook(self):
        other_extensions = ["jishaku", "cog_reloader"]
        # add for loop for loading otherextneions!
        await self.load_extension("jishaku")
        try:
            for filename in os.listdir("./commands"):
                if filename.endswith(".py"):

                    await self.load_extension(f"commands.{filename[:-3]}")
        except Exception as e:
            # add error logging here
            print(f"Failed to load extension {filename}")
            print(e)

        self.uptime =  datetime.utcnow()
        


    async def close(self):
        print("Pokecord is shutting down")  # add logging here
        await super().close()

    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            await self.process_commands(message)

    async def on_message_edit(self, before, after):
        if after.content != before.content:
            await self.process_commands(after)

    class PinkEmbed(discord.Embed):
        def __init__(self, **kwargs):
            color = kwargs.pop("color", colors.PINK)
            super().__init__(**kwargs, color=color)

    
