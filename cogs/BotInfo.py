from discord.ext import commands
import discord
import os

class BotInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="Version", help="Shows bot version.", aliases=["v", "V"])
    async def on_message(self, message):
    
        response = os.getenv("VERSION")
        await message.channel.send(response)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        await channel.send(f"{member} has arrived!")


    @commands.command(name="Zoom", help="Zoom link", aliases=["zoom"])
    async def zoom(self, ctx):

        url = "https://us04web.zoom.us/j/78012351547?pwd=TFU3bWtSc01QYmFoUldtSmtUUmoyQT09"
        embed = discord.Embed(
            title="Clica aqui para ir para a reunião",
            color=discord.Colour.gold(),
            url=url
        )
        
        await ctx.channel.send(embed=embed)


    @commands.command(name="Decode", help="Decode info", aliases=["decode"])
    async def decode(self, ctx):

        url = "https://decodechess.com"
        embed = discord.Embed(
            title="Decode",
            color=discord.Colour.gold(),
            url=url,
            description="Permite analisar jogos com AI a explicar as jogadas."
        )

        embed.add_field(name = "username", value="gdmxadrez@gmail.com")
        embed.add_field(name = "password", value="Ricardo48")

        await ctx.channel.send(embed=embed)   


    @commands.command(name="Livros", help="box com livros", aliases=["livros"])
    async def livros(self, ctx):

        url = "https://mega.nz/folder/WDpiAIxI"
        embed = discord.Embed(
            title="Livros",
            color=discord.Colour.gold(),
            url=url,
            description="Box com livros para download."
        )

        embed.add_field(name = "password", value="FpINV5x1Zna3yvB50UQHpg")

        await ctx.channel.send(embed=embed)


    @commands.command(name="Programas", help="box com programas", aliases=["programas"])
    async def programas(self, ctx):

        url = "https://mega.nz/folder/aKwiUCSL"
        embed = discord.Embed(
            title="Programas",
            color=discord.Colour.gold(),
            url=url,
            description="Box com programas para download."
        )

        embed.add_field(name = "password", value="uLwhxDTgoR5tEO-VUAWCzw")

        await ctx.channel.send(embed=embed)


    @commands.command(name="Videos", help="box com videos", aliases=["videos"])
    async def videos(self, ctx):

        url = "https://mega.nz/folder/OXoiGLxY"
        embed = discord.Embed(
            title="Videos",
            color=discord.Colour.gold(),
            url=url,
            description="Box com videos para download."
        )

        embed.add_field(name = "password", value="EqlZGEYaqOwYdnJ0FycDEQ")

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(BotInfo(bot))