# Discord Imports
import discord
from discord.ext import commands

# Time Imports
from datetime import date
import time

# Other Imports
import random
import inspect
import os


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def who(self, ctx):
        e = discord.Embed(
            title=f"Hi, I'm {self.bot.user}", description=f"You can find the privacy policy at [this](https://greendiscord.github.io/TransHelper-Source/resources.html \"privacy policy\") link!", color=discord.Colour.from_hsv(random.random(), 1, 1))
        await ctx.send(embed=e)

    @commands.command()
    async def vote(self, ctx):
        e = discord.Embed(title=f"Hi, You can vote for me using the link below!",
                          description=f"[Click Here!](https://top.gg/bot/787820448913686539/vote \"Vote\")", color=discord.Colour.from_hsv(random.random(), 1, 1))
        await ctx.send(embed=e)

    @commands.command()
    async def ping(self, ctx):
        starttime = time.time()
        msg = await ctx.send("Ping...")
        e = discord.Embed(title="Pong!", description=f"Heartbeat : {round(self.bot.latency * 1000, 2)} ms")
        endtime = time.time()
        difference = round(int(starttime - endtime * 1))
        e.add_field(name="Script Speed", value=f"{difference}ms")
        await msg.edit(content="", embed=e)

    @commands.command()
    async def source(self, ctx):
        """ Displays source code """
        source_url = 'https://github.com/GreenDiscord/TransHelper-Source'
        e = discord.Embed(title="You didn't provide a command (because you cant), so here's the source!",
                          description=f"[Source]({source_url})")
        await ctx.send(embed=e)

    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, *, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        user = user or ctx.author
        e = discord.Embed(title=f"Avatar for {user.name}")
        e.set_image(url=user.avatar_url)
        await ctx.send(embed=e)

    # @commands.command()
    # @commands.guild_only()
    # async def roles(self, ctx):
    #  """ Get all roles in current server """
     #   allroles = ""

       # for num, role in enumerate(sorted(ctx.guild.roles, reverse=True), start=1):
       #     allroles += f"[{str(num).zfill(2)}] {role.id}\t{role.name}\t[ Users: {len(role.members)} ]\r\n"

       # data = BytesIO(allroles.encode('utf-8'))
       # await ctx.send(content=f"Roles in **{ctx.guild.name}**", file=discord.File(data, filename=f"Roles"))

    @commands.command()
    @commands.guild_only()
    async def joinedat(self, ctx, *, user: discord.Member = None):
        """ Check when a user joined the current server """
        if user is None:
            user = ctx.author

        embed = discord.Embed(
            title=f'**{user}**', description=f'{user} joined **{ctx.guild.name}** at \n{user.joined_at}')
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.group()
    @commands.guild_only()
    async def server(self, ctx):
        """ Check info about current server """
        if ctx.invoked_subcommand is None:
            find_bots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed(
                title=f"ℹ information about **{ctx.guild.name}**", description=None)

            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon_url)
            if ctx.guild.banner:
                embed.set_image(url=ctx.guild.banner_url_as(format="png"))

            embed.add_field(name="Server Name",
                            value=ctx.guild.name, inline=True)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
            embed.add_field(
                name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=find_bots, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            await ctx.send(embed=embed)

    @server.command(name="server_icon", aliases=["icon"])
    @commands.guild_only()
    async def server_icon(self, ctx):
        """ Get the current server icon """
        if not ctx.guild.icon:
            return await ctx.send("This server does not have a avatar...")
        await ctx.send(f"Avatar of **{ctx.guild.name}**\n{ctx.guild.icon_url_as(size=1024)}")

    @server.command(name="banner")
    @commands.guild_only()
    async def server_banner(self, ctx):
        """ Get the current banner image """
        if not ctx.guild.banner:
            return await ctx.send("This server does not have a banner...")
        e = discord.Embed(title=f"ℹ Banner for {ctx.guild}")
        e.set_image(url=ctx.guild.banner_url_as(format='png'))
        await ctx.send(embed=e)

    @commands.command()
    @commands.guild_only()
    async def user(self, ctx, *, user: discord.Member = None):
        """ Get user information """
        user = user or ctx.author

        show_roles = ', '.join(
            [f"<@&{x.id}>" for x in sorted(user.roles, key=lambda x: x.position,
                                           reverse=True) if x.id != ctx.guild.default_role.id]
        ) if len(user.roles) > 1 else 'None'
        content2 = f"ℹ About **{user.id}**"
        embed = discord.Embed(
            title=content2, colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Full name", value=user, inline=True)
        embed.add_field(name="Nickname", value=user.nick if hasattr(
            user, "nick") else "None", inline=True)
        embed.add_field(name="Roles", value=show_roles, inline=False)
        embed.add_field(name="Joined?", value=f"{user.joined_at}")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
