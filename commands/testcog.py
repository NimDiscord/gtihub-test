import discord
from discord.ext import commands
from core.bot import Pokecord
import constants.constants as constants
import constants.config as config
import asyncio


class Test(commands.Cog):
    def __init__(self, bot: Pokecord):
        self.bot = bot

# import constants

    # @commands.Cog.listener()
    # async def on_guild_join(self, guild: discord.Guild):

    #     if guild.member_count < config.MINIMUM_MEMBER_COUNT:

    #         priority_channels = []
    #         channels = []
    #         for channel in guild.channels:
    #             if channel == guild.system_channel or any(x in channel.name for x in constants.GENERAL_CHANNEL_NAMES):

    #                 priority_channels.append(channel)
    #             else:
    #                 channels.append(channel)
    #         channels = priority_channels + channels

    #         channel = next(
    #             x for x in channels if isinstance(x, discord.TextChannel) and x.permissions_for(guild.me).send_messages
    #         )
    #         await channel.send("I will leave this server after a minute lol")
    #         await asyncio.sleep(60)
    #         await guild.leave()

    #     else:
    #         
    

    @commands.command()
    async def pp(self, ctx):
        embed = self.bot.PinkEmbed(title="eee")
        await ctx.send(embed=embed)

    @commands.command()
    async def ppp(self, ctx):
        embed = self.bot.PinkEmbed(title="eeesfdse")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Test(bot))
