import discord as dc
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = dc.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot online')
    print('------')

async def load_cogs():
    cogs_path = 'cogs'
    for filename in os.listdir(cogs_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            await bot.load_extension(f'{cogs_path}.{filename[:-3]}')
            print(f'Cog "{filename[:-3]}" carregada!')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
