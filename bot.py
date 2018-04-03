import discord

TOKEN = "NDMwNzQ4Nzg2NDIwMDg4ODQy.DaUt4Q.lPd71aYiHRfjNY-cmEmNLNeUPUw"

client = discord.Client()

@client.event
async def on_message(message):
    #comment for spacing
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)