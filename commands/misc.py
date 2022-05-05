import discord
from discord.ext import commands
from core.bot import Pokecord

import datetime

class Misc(commands.Cog):
    def __init__(self, bot: Pokecord):
        self.bot = bot

    @commands.command()
    # @decorators.is_not_disabled()
    async def stats(self, ctx):
        """Display stats about the bot"""
        embed = self.bot.PinkEmbed(
            title=f"{self.bot.user.name}"
        )
        embed.add_field(
            name="Author/Owner :writing_hand:",
            value="`WiperR#5571`, `Ariz#0001`,  `Valentín#1080`"
        )
        embed.add_field(name="Default Prefix", value="`p!`")
        embed.add_field(name="Library :books:", value="`discord.py 1.6.1`")
        # embed.add_field(
        #     name="Bot Count", value=f"`Servers : {await self.bot.mongo.db.guilds.estimated_document_count()}`\n`Users : {await self.bot.mongo.db.member.estimated_document_count()}`")
        embed.add_field(name="Total Channels", value=f"'e`")
        embed.set_author(
            name=f"{self.bot.user.name}",
            icon_url=self.bot.user.avatar_url
        )
        embed.set_footer(
            text=f"Websocket Ping {str(round(self.bot.latency * 250))}ms")
        embed.add_field(
            name="Uptime", value=f"e"
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Misc(bot))