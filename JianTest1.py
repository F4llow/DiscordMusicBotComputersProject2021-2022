#import random to use for later commands
import random

#import the pypartpicker api
from pypartpicker import Scraper

#makes it easier, less characters to type
sc = Scraper()

#takes the google api client
from googleapiclient.discovery import build

#google api key
api_key = "AIzaSyBxk7rriyZRroJRcVbykCQa2rdArP-hC_4"

#set the api requirements as the youtube variable
youtube = build("youtube", "v3", developerKey = api_key)

#requests the channel stats of forUsername
request = youtube.channels().list(
        part = "statistics",
        forUsername = "sentdex"
    )

#executes the request above
response = request.execute()

#print that request
#print(response)

#gets the videoId from the query
#query = "bloody stream piano"
#result = youtube.search().list(q = query, part = "snippet", type = "video", maxResults = 1)
#response2 = result.execute()
#for i in response2["items"]:
#    videoId = i["id"]["videoId"]
#    link = "https://www.youtube.com/watch?v=" + str(videoId)
#    print(link)

################################################################################

#import discord and commands
import discord

from discord.ext import commands

from discord.utils import get

#this is it boys
#this is where the fun begins...
from discord import FFmpegPCMAudio

from youtube_dl import YoutubeDL

#set the command prefix
client = commands.Bot(command_prefix = "!")

#must include @client.event
#must include async
#on_ready() makes the bot online and up and running
@client.event
async def on_ready():
    print("The Bot is now live.")

#prints when a member has joined a server (incomplete)
#@client.event
#async def on_member_join(member):
#    print(f"{member} has joined this server.")

#prints when a member has left a server (incomplete)
#@client.event
#async def on_member_remove(member):
#    print(f"{member} has left this server.")

#test command that sends that they are gay
@client.command()
async def im(ctx):
    await ctx.send("gay")
    print("the gay command worked")

#test command which sends the funny number in letters
@client.command()
async def sixnine(ctx):
    await ctx.send(sixnine)
    print("the sixnine command worked")

#test command that tests the aliases
@client.command(aliases = ["69", "funnynumber"])
async def _69(ctx):
    await ctx.send("69")
    print("the 69 command worked")

#test command which sends sentdex's channel stats
@client.command()
async def channel(ctx):
    await ctx.send(response)
    print("the channel stats worked")

#test command which sends gud night
@client.command()
async def gn(ctx):
    await ctx.send("gud night everyone")
    print("the gn command worked")

#test command to demonstrate to nicholas how it works
@client.command()
async def nicholas(ctx):
    await ctx.send("Hello, Nicholas I made this command for you.")
    print("nicholas' command worked")

#test command to practice inputs
#@client.command()
#async def var(ctx):

#test command which sends link
@client.command()
async def linktest(ctx):
    await ctx.send("https://www.op.gg/champion/diana/statistics/mid/")
    print("the link command worked")

#test command that sends the bot's ping in ms
@client.command()
async def ping(ctx):
    await ctx.send("This bot's ping is: " + str(round(client.latency) * 1000) + " ms")
    print("the ping command worked")

#any string in the alias list will work for calling the command
#test command that answers your yes or no question
@client.command(aliases = ["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send("Question: " + str(question))
    await ctx.send("Answer: " + str(random.choice(responses)))
    print("the 8ball command worked")

#test command that deletes that past 5
#pass_context = True is super helpful if u follow up with a has_role
@client.command(pass_context = True)
@commands.has_role("Just the Two of Us")
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)
    print("the clear command works")

#test command that sends a number between 0 and 200
@client.command()
async def myiq(ctx):
    await ctx.send("Your IQ is " + str(random.randint(0, 200)) + ".")
    print("the iq command works")

#test command that assigns 1-5 people league of legends roles
@client.command()
async def role(ctx, rolenum):
    rolenum = int(rolenum)
    roles = ["Top Lane", "Jungle", "Mid Lane", "Bot Lane", "Support"]
    await ctx.send(random.sample(roles, rolenum))
    print("the role command worked")

#test command that assigns 1-5 people league of legends roles and takes no args
#@client.command()
#async def blankrole(ctx, rolenum, *, blank = none):
#    rolenum = int(rolenum)
#    roles = ["Top Lane", "Jungle", "Mid Lane", "Bot Lane", "Support"]
#    await ctx.send(random.sample(roles, rolenum))
#    print("the role command worked")

#test command that makes your op.gg link with champion and role
@client.command()
async def champion(ctx, champion, role):
    link = "https://www.op.gg/champion/" + str(champion) + "/statistics/" + str(role)
    await ctx.send(link)
    print("the champion command worked")

#test command taht kicks a member
@client.command(pass_context = True)
@commands.has_role("Just the Two of Us")
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    print("the kick command worked")

#test command that bans a member
@client.command(pass_context = True)
@commands.has_role("Just the Two of Us")
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send("The user" + str(user.mention) + "has been banned.")
    print("the ban command worked")

#test command that unbans a member
@client.command(pass_context = True)
@commands.has_role("Just the Two of Us")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("The user" + str(user.mention) + "has been unbanned.")
            print("the unban command has worked")
            return

@client.command()
async def lp1(ctx):
    await ctx.send("‏‏‎ ‎‏‏‎ ‏‏‎ ‎‎‏‏‎ ‎╭━━━━╮\n╭┫▕▎▕▎┣╮Special delivery\n╰┓┳╰╯┳┏╯ For You\n╭┛╰━━╯┗━━━╮\n┃┃    ┏━╭╰╯╮\n┃┃    ┃┏┻━ ━┻┓\n╰┫ ╭╮ ┃┃ - 15LP ‏‏‎‏‏‎ ‏‏‎ ‎‎ ‎‏‏‎ ‎┃\n ┃ ┃┃ ┃╰━━ ━━╯\n╭┛ ┃┃ ┗╮\n╰━━╯╰━━╯\nGG EZ ( ͡⚆ ͜ʖ ͡⚆)╭∩╮")
    print("the lp1 command worked")

@client.command()
async def lp2(ctx):
    await ctx.send("╭━━━━━╮\n╰┃ ┣▇━▇\n ┃ ┃  ╰━▅╮\n ╰┳╯ ╰━━┳╯ BRUV KEK\n  ╰╮ ┳━━╯ SUPER EASY\n ▕▔▋ ╰╮╭━╮ NICE TUTORIAL\n╱▔╲▋╰━┻┻╮╲╱▔▔▔╲\n▏  ▔▔▔▔▔▔▔  O O┃\n╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n ▏╳▕▇▇▕ ▏╳▕▇▇ ▕\n ╲▂╱╲▂╱ ╲▂╱ ╲▂╱")
    print("the lp2 command worked")

#test command that tests *
@client.command()
async def asterisk(ctx, *, context):
    await ctx.send(context[1:-1])
    print(context[1:-1])
    print("the asterisk command worked")

#test command that puts each word into a list and prints the last one
@client.command()
async def lastword(ctx, *, context):
    allwords = context.split()
    await ctx.send(allwords[-1])
    print("the lastword command worked")

#command that takes your youtube search and makes a link of the first result
@client.command()
async def link(ctx, *, query):
    result = youtube.search().list(q = query, part = "snippet", type = "video", maxResults = 1)
    response2 = result.execute()
    for i in response2["items"]:
        videoId = i["id"]["videoId"]
        link = "https://www.youtube.com/watch?v=" + str(videoId)
        await ctx.send(link)
        print("the link function worked")

#command that takes your youtube search and makes a link of quantity * results
@client.command()
async def qlink(ctx, quantity, *, query):
    result = youtube.search().list(q = query, part = "snippet", type = "video", maxResults = quantity)
    response2 = result.execute()
    for i in response2["items"]:
        videoId = i["id"]["videoId"]
        link = "https://www.youtube.com/watch?v=" + str(videoId)
        await ctx.send(link)
        print("the qlink function worked")

################################################################################
#testing pypartpicker
#aka my prefered unofficial pcpartpicker api

#test command that gets first result from pcpartpicker search
#it returns the name, url, type, price, and image link
#the type returns none regardless of the product
#im pretty sure it is something on the unofficial api creator's end
#returns error saying that something is wrong with the http request since it cannot send an empty message
@client.command()
async def pcpartpicker(ctx, *, query):
    result = sc.part_search(query, limit = 1, region = "us")
    firstProductName = result[0].name
    firstProductPrice = result[0].price
#    firstProductType = result[0].type
    firstProductUrl = result[0].url
    firstProductImage = result[0].image
    await ctx.send("The product name is: " + firstProductName)
    await ctx.send("It costs this much: " + firstProductPrice)
#    await ctx.send("This is a " + firstProductType)
    await ctx.send("The url can be found it here: " + firstProductUrl)
    await ctx.send("The image link can be found here: " + firstProductImage)
    print("the pcpartpicker command worked")

################################################################################

#wish me luck
queueList = []

@client.command()
async def join(ctx):
    voice_state = ctx.author.voice
    if voice_state is None:
        await ctx.send("You are not in a voice channel.")
        return print("the join command worked but they are not in a voice channel")
    else:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("I have joined your voice channel.")
        return print("the join command worked and i joined a voice channel")

@client.command()
async def leave(ctx):
    #if returns an error then ctx.send("there is nothing for me to leave")
    await ctx.voice_client.disconnect()
    await ctx.send("I have left your voice channel.")
    print("The leave command has worked")

#command that combines play and playurl so it will take either search or url
@client.command()
async def play(ctx, *, qurl):
    linkstart = "https://www.youtube.com/"
    if linkstart in qurl:
        url = qurl
        queueList.append(url)
        FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
        voice = get(client.voice_clients, guild = ctx.guild)
        if not voice.is_playing():
            ydl_opts = {"format": "bestaudio"}
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download = False)
            URL = info["formats"][0]["url"]
            voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await ctx.send("Your song is now playing.")
            print("the playurl command worked")
        else:
            queueList.append(url)
            await ctx.send("Your song has been added to queue which is in development.")
            print("the play command added the url to queue")
            return
    else:
        query = qurl
        result = youtube.search().list(q = query, part = "snippet", type = "video", maxResults = 1)
        response2 = result.execute()
        for i in response2["items"]:
            videoId = i["id"]["videoId"]
            link = "https://www.youtube.com/watch?v=" + str(videoId)
            url = link
            queueList.append(url)
            FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
            voice = get(client.voice_clients, guild = ctx.guild)
            if not voice.is_playing():
                ydl_opts = {"format": "bestaudio"}
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download = False)
                URL = info["formats"][0]["url"]
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                voice.is_playing()
                await ctx.send(str(url) + " is now playing.")
                print("the play command worked")
            else:
                queueList.append(url)
                await ctx.send("Your song has been added to queue which is in development.")
                print("the play command your song to the queue")
                return

@client.command()
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.pause()
    await ctx.send("the music has been paused")
    print("the pause command worked")

@client.command()
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.resume()
    await ctx.send("the music has been resumed")
    print("the resume command worked")

@client.command()
async def isplaying(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    bool = voice_channel.is_playing()
    await ctx.send(bool)
    print("the isplaing command works")

@client.command()
async def ispaused(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    bool = voice_channel.is_paused()
    await ctx.send(bool)
    print("the ispaused command works")

@client.command()
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()
    await ctx.send("the song has now stopped")
    print("the stop command has worked")

@client.command()
async def addtoqueue(ctx, *, query):
    result = youtube.search().list(q = query, part = "snippet", type = "video", maxResults = 1)
    response2 = result.execute()
    for i in response2["items"]:
        videoId = i["id"]["videoId"]
        link = "https://www.youtube.com/watch?v=" + str(videoId)
        url = link
        queueList.append(url)
        await ctx.send("Your song has been added to queue.")
        print("the addtoqueue command worked")

@client.command()
async def queue(ctx):
    await ctx.send(queueList)
    print("the queue command worked")

@client.command()
async def clearqueue(ctx):
    queuelist.clear()
    await ctx.send("the queue has been cleared")
    print("the clearqueue worked")

# @client.command()
# async def play(ctx, *, query):
#     result = youtube.search().list(q = query, part = "snippet", type = "video", maxResults = 1)
#     response2 = result.execute()
#     for i in response2["items"]:
#         videoId = i["id"]["videoId"]
#         link = "https://www.youtube.com/watch?v=" + str(videoId)
#         url = link
#         FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
#         voice = get(client.voice_clients, guild = ctx.guild)
#         if not voice.is_playing():
#             ydl_opts = {"format": "bestaudio"}
#             with YoutubeDL(ydl_opts) as ydl:
#                 info = ydl.extract_info(url, download = False)
#             URL = info["formats"][0]["url"]
#             voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#             voice.is_playing()
#             await ctx.send(str(url) + " is now playing.")
#             print("the play command worked")
#         else:
#             await ctx.send("A song is already playing.")
#             print("the play command worked but a song is already playing")
#             return

# command that sends plays youtube video using link
# @client.command()
# async def playurl(ctx, url):
#     FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
#     voice = get(client.voice_clients, guild = ctx.guild)
#     if not voice.is_playing():
#         ydl_opts = {"format": "bestaudio"}
#         with YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download = False)
#         URL = info["formats"][0]["url"]
#         voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#         voice.is_playing()
#         await ctx.send("Your song is now playing.")
#         print("the playurl command worked")
#     else:
#         await ctx.send("A song is already playing and the queue is currently in development.")
#         print("the playurl command worked but a song is already playing")
#         return

#checking to see if the bot is in a call, if it not then join a call
# @client.command()
# async def joinandplay(ctx):
#     userChannel = ctx.author.voice
#     botChannel = ctx.voice_client
#     await ctx.send(userChannel)
#     await ctx.send(botChannel)

# command that sends plays youtube playlist using link
# @client.command()
# async def playlist(ctx, url):
#     FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
#     voice = get(client.voice_clients, guild = ctx.guild)
#     if not voice.is_playing():
#         ydl_opts = {"format": "bestaudio"}
#         with YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download = False)
#         URL = info["formats"][0]["url"]
#         voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#         voice.is_playing()
#         await ctx.send("Your song is now playing.")
#         print("the playurl command worked")
#     else:
#         await ctx.send("A song is already playing.")
#         print("the playurl command worked")
#         return

#run the bot
client.run("ODg3ODYxNDkzMDQ2MDY3MjMy.YUKTcw.f6xHdRiYUz01pOJ25i42ihQ-HLs")
