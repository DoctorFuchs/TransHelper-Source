# Discord Imports
import discord
from discord.ext import commands

# Other Imports
import mystbin
import random


class MystbinApi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.mystbin_client = bot.mystbin_client

    @commands.command(aliases=["myst"])
    async def mystbin(self, ctx, *, text):
        paste = await self.bot.mystbin_client.post(f"{text}", syntax="python")
        e = discord.Embed(title="I have created a mystbin link for you!",
                          description=f"[Click Here]({paste.url})")
        await ctx.send(embed=e)

    @commands.command(aliases=["getmyst"])
    async def getmystbin(self, ctx, id):
        try:
            get_paste = await self.bot.mystbin_client.get(f"https://mystb.in/{id}")
            lis = ["awesome", "bad", "good"]
            content = get_paste.content
            lencontent = len(content)
            if lencontent > 1080:
                e = discord.Embed(title=f"I have found this, but the content is to big!",
                                  description=f"The content is shown here:  [Link]({get_paste.url})")
                await ctx.send(embed=e)
            else:
                e2 = discord.Embed(
                    title=f"I have found this, is it {random.choice(lis)}?", description=f"{content}")
                await ctx.send(embed=e2)
        except mystbin.BadPasteID:
            await ctx.send(f"Hmmm.. id : {id} isn't found, try again?")


def setup(bot):
    bot.add_cog(MystbinApi(bot))
