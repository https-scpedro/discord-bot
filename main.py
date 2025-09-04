import os
from dotenv import load_dotenv
import discord as dc
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = dc.Intents.all()
bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event
async def on_ready():
    print("Bot inicializado!")                              # Printa no terminal
    channel = await bot.fetch_channel(1111427627190861855)  # Busca o canal na API do Discord
    await channel.send("Bot online!")                       # Envia mensagem no canal

@bot.event
async def on_member_join(member:dc.Member):
    embed = dc.Embed()
    embed.title = "Bem-vindo(a)!"
    embed.description = f"Olá {member.mention}, seja bem-vindo(a) ao servidor!"
    channel = await bot.fetch_channel(1412958840214913145)
    await channel.send(embed=embed)  

@bot.command()
async def ping(ctx:commands.Context):
    await ctx.reply("Pong!")

@bot.command()
async def ola(ctx:commands.Context):
    await ctx.reply("Olá, como vai?")

@bot.command()
async def profile(ctx:commands.Context):
    pfp = ctx.author.avatar.url
    embed = dc.Embed(title=f"Avatar de {ctx.author.display_name}")
    embed.set_image(url=pfp)
    await ctx.reply(embed=embed)

@bot.command()
async def teste(ctx):
    await ctx.send("Funcionando!")

bot.run(TOKEN)