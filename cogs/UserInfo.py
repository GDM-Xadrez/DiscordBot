from discord.ext import commands
import discord
from . import user_db


class UserInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="User", help="Shows user info.", aliases=["user"])
    async def user(self, message, user):
        
        if user_db.is_user(user):
            embed = discord.Embed(
                title=user,
                color=discord.Colour.gold()
            )

            embed.add_field(name = "xp", value=user_db.get_xp(user))
            embed.add_field(name = "lichess account", value=user_db.get_lichess_acc(user))

            await message.channel.send(embed=embed)

        else: await message.channel.send("Erro. Esse utilizador não existe!")


    @commands.command(name="User-xp", help="Shows user xp.", aliases=["user-xp"])
    async def user_xp(self, message, user):
        
        if user_db.is_user(user):

            await message.channel.send("{} has {} xp!".format(user, user_db.get_xp(user))) 
        
        else: await message.channel.send("Erro. Esse utilizador não existe!")


    @commands.command(name="User-lichess", help="Shows user lichess account.", aliases=["user-lichess"])
    async def user_lichess(self, message, user):
        
        if user_db.is_user(user):

            await message.channel.send(user_db.get_lichess_acc(user)) 
        
        else: await message.channel.send("Erro. Esse utilizador não existe!")



def setup(bot):
    bot.add_cog(UserInfo(bot))
