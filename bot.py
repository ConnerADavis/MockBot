from imageManipulation import createMeme
import discord
import random

TOKEN = "NDMwNzQ4Nzg2NDIwMDg4ODQy.DaUt4Q.lPd71aYiHRfjNY-cmEmNLNeUPUw"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!mock"):
        user = message.mentions[0]
        found = False
        async for m in client.logs_from(message.channel):
            if m.author == user:
                lastmessage = m.content
                found = True
                break
        msg = "No recent message by " + user.name
        if found and lastmessage != "":
            # msg = changeCases(lastmessage)
            # msg = createMeme(user, lastmessage)
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


def changeCases(original):  # CHANGE CASES!
    msg = ""
    characters = list(original)
    for c in characters:
        tmp = c
        if c.isalpha():
            if random.randint(0, 10) < 5:
                tmp = tmp.upper()
            else:
                tmp = tmp.lower()
        msg += tmp
    return msg

client.run(TOKEN)