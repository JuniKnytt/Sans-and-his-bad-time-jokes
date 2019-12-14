import asyncio
import discord
import praw
import random
import ffmpeg
from mutagen.mp3 import MP3
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord.utils import get


client = discord.Client()
memeBot = commands.Bot(command_prefix='.')
memeSound = [
                "sounds/aww_man.mp3",
                "sounds/creeper.mp3",
                "sounds/creeperFuse.mp3",
                "sounds/hoo.mp3"
            ]
@memeBot.event
async def on_ready():
    print("memes!")
    print(len(memeSound))

@memeBot.command()
async def meme(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Hey kid, you're not in a voice channel.")
        return
    voice = get(memeBot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        rngLimit = len(memeSound) - 1
        rngPicker = random.randint(0, rngLimit)
        source = discord.FFmpegPCMAudio(memeSound[rngPicker])
        print(memeSound[rngPicker])
        voice.play(source, after=lambda e: print("Played"))
        audio = MP3(memeSound[rngPicker])
        print(audio.info.length)
        await asyncio.sleep(audio.info.length)
        await voice.disconnect()

@memeBot.command()
async def memePick(ctx, pick):
    pickInt = int(pick) - 1
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Hey kid, you're not in a voice channel.")
        return
    voice = get(memeBot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        if pickInt < 0 or pickInt > len(memeSound)-1:
            await ctx.send("Not Within Range")
            return
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio(memeSound[pickInt])
        print(memeSound[pickInt])
        voice.play(source, after=lambda e: print("Played"))
        audio = MP3(memeSound[pickInt])
        print(audio.info.length)
        await asyncio.sleep(audio.info.length)
        source.cleanup()
        await voice.disconnect()

memeBot.run("NjI5MDY3NzE2MzIxNjA3Njgy.XZUXdg.YBYvqTjEyisrVOUXliTnlxT91GA")

