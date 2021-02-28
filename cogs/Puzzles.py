from discord.ext import commands
import csv
import random
import discord
import pandas as pd

def get_puzzle():
    puzzle_db = pd.read_csv(r'C:\Users\jeron\Documents\Programacao\Projetos\XadrezDiscordBot\cogs\db\puzzle_db.csv')

    puzzle_db = puzzle_db["mateIn1" in puzzle_db[7]]
    puzzle = puzzle_db[random.randint(0, len(puzzle_db)-1)]
    print(puzzle)
    FEN = puzzle[1]
    sol = puzzle[2][:5]

    return FEN, sol

class Puzzles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Desafio", pass_context=True)
    async def desafio(self, ctx):
        guild = ctx.guild
        FEN, sol = get_puzzle()
        print(FEN, sol)
        print("https://chessboardimage.com/{}.png".format(FEN.replace(" ","%20")))

        if "b" in FEN:
            description = "Brancas a jogar"
        else: description = "Pretas a jogar"
        embed = discord.Embed(
                title="Puzzle",
                color=discord.Colour.gold(), 
                description=description
            )

        embed.set_image(url="https://chessboardimage.com/{}.png".format(FEN.replace(" ","%20")))

        await ctx.channel.send(embed=embed)

        answer = await self.bot.wait_for("message")    
        print(answer.content, sol, sol == answer.content)
        if answer.content == sol:
            await ctx.channel.send("Correct.")

        else: await ctx.channel.send("Wrong.")    


def setup(bot):
    bot.add_cog(Puzzles(bot))