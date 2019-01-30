from imageManipulation import createMeme
import discord
import random

TOKEN = "[Redacted for security]"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!mock") and len(message.mentions) > 0:
        user = message.mentions[0]
        lastmessage = ""
        async for m in client.logs_from(message.channel):
            if m.author == user:
                lastmessage = m.content
                if not lastmessage.startswith("!mock"):
                   break
        msg = "No recent message by " + user.name
        if lastmessage != "":
            createMeme(user, lastmessage)
            await client.send_file(message.channel, "edited.png")
        else:
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)