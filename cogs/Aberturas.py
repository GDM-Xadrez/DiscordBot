from discord.ext import commands
import discord

class Aberturas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="CaroKhan", help="Caro khan sucks.")
    async def carosucks(self, message):
        mention = message.author.mention
        response = "Caro Khan sucks! {}".format(mention)

        await message.channel.send(response)


    @commands.command(name="Defesa_Francesa")
    async def francesa(self, message):
        embed = discord.Embed(
            title="Defesa Francesa",
            description="Defesa contra e4.",
            color=discord.Colour.gold(),
            url="https://www.youtube.com/watch?v=5pec-u6PSvA"
        )

        embed.set_image(url="https://cdn1.ichess.net/wp-content/uploads/2011/12/French-Defense-Exchange-Variation.jpg")

        await message.channel.send(embed=embed)

    @commands.command(name="Caro_Khan")
    async def carokhan(self, message):
        embed = discord.Embed(
            title="Caro Khan",
            description="Defesa contra e4.",
            color=discord.Colour.gold(),
        )
        await message.channel.send("https://www.youtube.com/watch?v=rmbU97iftC8")
        await message.channel.send(embed=embed)


    
def setup(bot):
    bot.add_cog(Aberturas(bot))