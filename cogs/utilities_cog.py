import discord as dc
from discord.ext import commands

class UtilitiesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Mensagem de boas vindas para membro novo
    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = dc.utils.get(member.guild.text_channels, name='Boas-Vindas')
        embed = dc.Embed()
        embed.title = "Bem-vindo!"
        embed.description = f"Olá {member.name}, bem-vindo ao servidor!"
        embed.set_thumbnail(url=member.avatar.url)
        if welcome_channel:
            await welcome_channel.send(embed=embed)

    # Ping
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.reply("Pong!")

    # Avatar
    @commands.command(name='profile') 
    async def avatar_profile(self, ctx: commands.Context):
        pfp = ctx.author.avatar.url
        embed = dc.Embed(title=f"Avatar de {ctx.author.display_name}")
        embed.set_image(url=pfp)
        await ctx.reply(embed=embed)
    
    # Comandos Git
    @commands.command()
    async def git(self, ctx: commands.Context):
        embed = dc.Embed()
        embed.title = "Principais comandos do Git"
        embed.description = (
            "**⚙️ Configurações iniciais**:\n"
            "`git init` - Cria um novo repositório Git\n"
            "`git clone <url>` - Baixa uma cópia de um repositório remoto\n\n"

            "**🏃 Comandos do dia a dia** :\n"
            "`git status` - Mostra o estado atual do repositório: quais arquivos foram modificados, quais estão prontos para commit, etc...\n"
            "`git add <arquivo>` - Adiciona um arquivo específico à área de stage\n"
            "`git add .` - Adiciona todos os arquivos modificados à área de stage\n"
            "`git commit -m 'mensagem'` - Cria um commit com os arquivos na área de stage\n"
            "`git push` - Envia os commits locais para o repositório remoto\n"
            "`git pull` - Atualiza o repositório local com as mudanças do repositório remoto\n\n"

            "**🌿 Trabalhando com branches** :\n"
            "`git branch` - Lista todas as branches no repositório\n"
            "`git branch <nome-da-branch>` - Cria uma nova branch\n"
            "`git checkout <nome-da-branch>` - Muda para a branch especificada\n"
            "`git merge <nome-da-branch>` - Mescla a branch especificada na branch atual\n"
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(UtilitiesCog(bot))