import asyncio
import time
import discord
import random
from Classes.SoundDownloader import SoundDownloader

class BotBehavior:
    def __init__(self, bot, ffmpeg_path):
        self.bot = bot
        self.ffmpeg_path = ffmpeg_path
        self.sound_downloader = SoundDownloader()
        self.last_channel = {}

    def get_largest_voice_channel(self, guild):
        """Find the voice channel with the most members."""
        largest_channel = None
        largest_size = 0
        for channel in guild.voice_channels:
            if len(channel.members) > largest_size:
                largest_channel = channel
                largest_size = len(channel.members)
        return largest_channel

    async def disconnect_all_bots(self, guild):
        if self.bot.voice_clients:
            for vc_bot in self.bot.voice_clients:
                if vc_bot.guild == guild:
                    await vc_bot.disconnect()

    async def play_audio(self, channel, audio_file):
        voice_client = await channel.connect()
        voice_client.play(discord.FFmpegPCMAudio(executable=self.ffmpeg_path, source=audio_file))
        while voice_client.is_playing():
            await asyncio.sleep(.1)
        await voice_client.disconnect()

    async def update_bot_status_once(self):
        if hasattr(self.bot, 'next_download_time'):
            time_left = self.bot.next_download_time - time.time()
            minutes = round(time_left / 60)
            activity = discord.Activity(name=f'an explosion in ~{minutes}m', type=discord.ActivityType.playing)
            await self.bot.change_presence(activity=activity)

    async def update_bot_status(self):
        while True:
            await self.update_bot_status_once()
            await asyncio.sleep(60)

    async def download_sound_periodically(self):
        while True:
            self.sound_downloader.download_sound()
            await asyncio.sleep(1)
            for guild in self.bot.guilds:
                channel = self.get_largest_voice_channel(guild)
                if channel is not None:
                    await self.disconnect_all_bots(guild)
                    await self.play_audio(channel, r"C:\Users\netco\Downloads\random.mp3")
            sleep_time = random.uniform(600, 3600)
            self.bot.next_download_time = time.time() + sleep_time
            await self.update_bot_status_once()
            await asyncio.sleep(sleep_time)
