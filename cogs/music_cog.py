import discord as dc
from discord.ext import commands
import yt_dlp
import asyncio

YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.disconnect_timer = None

    async def disconnect_after_delay(self, ctx):
        await asyncio.sleep(300) # 5 minutos
        voice_client = ctx.voice_client
        if voice_client and not voice_client.is_playing():
            await voice_client.disconnect()
            await ctx.send("Desconectado do canal de voz por inatividade.")

    def on_song_end(self, ctx, error):
        if error:
            print(f'Player error: {error}')
            return
        # Inicia o temporizador de desconexão quando a música termina
        self.disconnect_timer = self.bot.loop.create_task(self.disconnect_after_delay(ctx))

    @commands.command(name='play', aliases=['p'], help='Toca uma música (URL ou nome)')
    async def play(self, ctx, *, query: str):
        if not ctx.author.voice:
            await ctx.send("Você precisa estar em um canal de voz para usar este comando.")
            return
        
        channel = ctx.author.voice.channel
        if ctx.voice_client and ctx.voice_client.channel != channel:
            await ctx.send("Já estou em um canal de voz.")
            return
        
        if ctx.voice_client is None:
            await channel.connect(self_deaf=True)
        else:
            await ctx.voice_client.move_to(channel)

        # Cancela qualquer temporizador de desconexão pendente, pois uma nova música vai tocar
        if self.disconnect_timer:
            self.disconnect_timer.cancel()
            self.disconnect_timer = None

        loading_message = await ctx.send(f"Procurando `{query}`...")

        try:
            loop = asyncio.get_event_loop()
            with yt_dlp.YoutubeDL(YTDL_OPTIONS) as ydl:
                info = await loop.run_in_executor(None, lambda: ydl.extract_info(query, download=False))
            
            entry = info['entries'][0] if 'entries' in info else info
            url = entry['url']
            title = entry.get('title', 'Título Desconhecido')

            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()
            
            source = dc.FFmpegPCMAudio(url, **FFMPEG_OPTIONS)
            ctx.voice_client.play(source, after=lambda e: self.on_song_end(ctx, e))

            await loading_message.edit(content=f"Tocando agora: **{title}**")

        except Exception as e:
            await loading_message.edit(content=f"Ocorreu um erro ao tentar tocar a música: {str(e)}")
            print(f'Erro no comando play: {e}')
    
    @commands.command(name='leave', aliases=['l'], help='Desconecta o bot do canal de voz')
    async def leave(self, ctx):
        if ctx.voice_client:
            if self.disconnect_timer:
                self.disconnect_timer.cancel()
                self.disconnect_timer = None
            await ctx.voice_client.disconnect()
            await ctx.send("Desconectado do canal de voz")
        else:
            await ctx.send("Não estou num canal de voz")

async def setup(bot):
    await bot.add_cog(MusicCog(bot))

