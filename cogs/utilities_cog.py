import discord as dc
from discord.ext import commands

class UtilitiesCog(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    # Mensagem de boas vindas para membro novo
    @commands.Cog.listener()
    async def on_member_join(member):
        welcome_channel = dc.utils.get(member.guild.text_channels, name='Boas-Vindas')
        embed = dc.Embed()
        embed.title = "Bem-vindo!"
        embed.description = f"Olá {member.name}, bem-vindo ao servidor!"
        embed.set_thumbnail(url=member.avatar.url)
        if welcome_channel:
            await welcome_channel.send(embed=embed)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.reply("Pong!")

    @commands.command(name='profile') 
    async def avatar_profile(self, ctx: commands.Context):
        pfp = ctx.author.avatar.url
        embed = dc.Embed(title=f"Avatar de {ctx.author.display_name}")
        embed.set_image(url=pfp)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(UtilitiesCog(bot))