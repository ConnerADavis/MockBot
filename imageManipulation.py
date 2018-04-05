from PIL import ImageDraw, ImageFont, Image
import discord
import random


def createMeme(user, message):
    top = user.name + ": " + message
    bottom = "Me: " + changeCases(message)
    if len(top) > 40 or len(bottom) > 40:
        createMemeComplex(top, bottom)
    else:
        createMemeSimple(top, bottom)


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

def createMemeSimple(top, bottom):
    font = ImageFont.truetype("DejaVuSansMono", 28)
    image = Image.open("template.png")
    draw = ImageDraw.Draw(image)
    draw.text((1, 1), top, (0, 0, 0), font)
    draw.text((1, 74), bottom, (0, 0, 0), font)
    image.save("edited.png", "PNG")


def createMemeComplex(top, bottom):
    font = ImageFont.truetype("DejaVuSansMono", 28)
    image = Image.open("template.png")
    draw = ImageDraw.Draw(image)
    topOne = ""
    topTwo = ""
    top = top.split()
    for t in top:
        if len(topOne) + len(t) < 40:
            topOne += " "
            topOne += t
        elif len(topTwo) + len(t) < 40:
            topTwo += " "
            topTwo += t
        else:
            topTwo += "..."
            break
    bottomOne = ""
    bottomTwo = ""
    bottom = bottom.split()
    for b in bottom:
        if len(bottomOne) + len(b) < 40:
            bottomOne += " "
            bottomOne += b
        elif len(bottomTwo) + len(b) < 40:
            bottomTwo += " "
            bottomTwo += b
        else:
            bottomTwo += "..."
            break
    draw.text((1, 0), topOne, (0, 0, 0), font)
    draw.text((1, 37), topTwo, (0, 0, 0), font)
    draw.text((1, 74), bottomOne, (0, 0, 0), font)
    draw.text((1, 111), bottomTwo, (0, 0, 0), font)
    image.save("edited.png", "PNG")