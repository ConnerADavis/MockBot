from PIL import ImageDraw, ImageFont, Image
import discord
import random


def createMeme(user, message):
    top = user.name + ": " + message
    bottom = "Me: " + changeCases(message)
    font = ImageFont.truetype("FreeMono", 28)
    image = Image.open("template.png")
    draw = ImageDraw.Draw(image)
    draw.text((1, 1), top, (0, 0, 0), font)
    draw.text((1, 75), bottom, (0, 0, 0), font)
    image.save("edited.png", "PNG")


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