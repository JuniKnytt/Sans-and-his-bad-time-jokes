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

print("Booting...")
client = discord.Client()
sansBot = commands.Bot(command_prefix='.')
print("Bot Initiated...")
sansSound = [
            "sans_noises/sans_ah1.mp3",
            "sans_noises/sans_ah2.mp3",
            "sans_noises/sans_ah3.mp3",
            "sans_noises/sans_ah4.mp3",
            "sans_noises/sans_ah5.mp3",
            "sans_noises/sans_ah6.mp3",
            "sans_noises/sans_ah7.mp3",
            "sans_noises/sans_ah8.mp3",
            "sans_noises/sans_ah9.mp3",
            "sans_noises/sans_ah10.mp3",
            "sans_noises/sans_ah11.mp3",
            "sans_noises/sans_ah12.mp3",
            "sans_noises/sans_ah13.mp3",
            "sans_noises/sans_ah14.mp3",
            "sans_noises/sans_ah15.mp3",
            "sans_noises/sans_ah16.mp3",
            "sans_noises/sans_dance.mp3",
            "sans_noises/sans_sess.mp3",
            "sans_noises/sans_call.mp3",
            "sans_noises/sans_discord.mp3",
            "sans_noises/sans_scout.mp3",
            "sans_noises/sans_christ.mp3",
            "sans_noises/sans_avgn.mp3",
            "sans_noises/sans_sonic.mp3",
            "sans_noises/sans_simpsons.mp3",
            "sans_noises/sans_mister.mp3",
            "sans_noises/sans_spy.mp3",
            "sans_noises/sans_heavy.mp3",
            "sans_noises/sans_joseph.mp3",
    "sans_noises/sans_goose.mp3"
            ]
print("Sounds Loaded...")
@sansBot.event
async def on_ready():
    print("Sans AHHHHH!")
    print(len(sansSound))


@sansBot.command()
async def sans(ctx):
    print("connecting...")



    if ctx.message.author.voice.channel is None:
        channel = 0
        print("Its indeed a channel")
    else:
        channel = ctx.message.author.voice.channel

    if not channel:
        await ctx.send("Hey kid, you're not in a voice channel.")
        return
    voice = get(sansBot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        print("Connection establishing")
        voice = await channel.connect()
        print("picking")
        rngLimit = len(sansSound) - 1
        rngPicker = random.randint(0, rngLimit)
        print("playing")
        source = discord.FFmpegPCMAudio(sansSound[rngPicker])
        print(sansSound[rngPicker])
        voice.play(source, after=lambda e: print("Done"))
        audio = MP3(sansSound[rngPicker])
        print(audio.info.length)
        await asyncio.sleep(audio.info.length)
        await voice.disconnect()

@sansBot.command()
async def sansPing(ctx):
    ping_ = sansBot.latency
    ping =  round(ping_ * 1000)
    await ctx.send(f"my ping is {ping}ms")

@sansBot.command()
async def sansPick(ctx, pick):
    print("connecting")
    pickInt = int(pick) - 1
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Hey kid, you're not in a voice channel.")
        return
    voice = get(sansBot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        print("sending")
        if pickInt < 0 or pickInt > len(sansSound)-1:
            await ctx.send("wut")
            return
        print("picked")
        voice = await channel.connect()
        print("About to play")
        source = discord.FFmpegPCMAudio(sansSound[pickInt])
        print(sansSound[pickInt])
        print("going to play")
        voice.play(source, after=lambda e: print("Done!"))
        audio = MP3(sansSound[pickInt])
        print(audio.info.length)
        await asyncio.sleep(audio.info.length)
        source.cleanup()
        await voice.disconnect()
token = "NjI4MDc2ODI1MzY4NTkyNDAz.XavwTA.d3ZarY4XU48UW6jleueBkL1xQNs"
sansBot.run(token)

