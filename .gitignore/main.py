import _json
# on importe le module discord.py
import discord


from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands

# une commmande
# !regles =regles #regles

# créer le bot
bot = commands.Bot(command_prefix='!')
warnings = {}



# détecter quand le bot est pret ("allumé")
@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.idle,
            activity=discord.Game("coder By Marisson"))

# créer la commande !5
@bot.command()
async def Turbo(ctx):
    await ctx.send("La Renault 5 Turbo : Son prix de location sera de : 3 500  €  et elle sera disponible à la location ")



# créer la commande !508
@bot.command()
async def peugot508(ctx):
    await ctx.send("La Peugot 508 : Son prix de location sera de : 600.65 €  et elle sera disponible à la location ")

# créer la commande !Leaf
@bot.command()
async def Leaf(ctx):
    await ctx.send("La Nissan New Life : Son prix de location sera de : 150 €  et elle sera disponible à la location ")


# créer la commande !MercedestC35
@bot.command()
async def jeep(ctx):
    await ctx.send("La Jeep : Son prix de location sera de : 250 € et elle sera disponible à la location ")

# créer la commande !AudiS5
@bot.command()
async def AudiS5(ctx):
    await ctx.send("La Jeep : Son prix de location sera de : 150 € et elle sera disponible à la location ")

# créer la commande !AudiTT
@bot.command()
async def AudiTT(ctx):
    await ctx.send("La AudiTT : Son prix de location sera de : 250 € et elle sera disponible à la location ")
# créer la commande !Sprinter
@bot.command()
async def sprinter(ctx):
    await ctx.send("Le Sprinter : Son prix de location sera de : 450 € et elle sera disponible à la location ")
# créer la commande !CLassV
@bot.command()
async def ClassV(ctx):
    await ctx.send("La Mercedest Class V: Son prix de location sera de : 550 €  et elle sera disponible à la location ")

# créer la commande !Ferrari512
@bot.command()
async def Ferrari512(ctx):
    await ctx.send("La Ferrari 512 : Son prix de location sera de : 450 € et elle sera disponible à la location ")

# créer la commande !class45
@bot.command()
async def class45(ctx):
    await ctx.send("La Mercedest Class 45 AMG : Son prix de location sera de : 140 € et elle sera disponible à la location ")

# créer la commande !Lambo
@bot.command()
async def lambo(ctx):
    await ctx.send("La Lambogini : Son prix de location sera de : 1 500.00 € et elle sera disponible à la location https://drive.google.com/file/d/1HDKH5s-jops0sJYbXn90AUIuoMYiTTNj/view?usp=sharing")


# créer la commande !jeep
@bot.command()
async def jeep1(ctx):
    await ctx.send("La jeep : Son prix de location sera de : 140 € et elle est disponible à la location")





# créer la commande !regles
@bot.command()
async def regles(ctx):
    await ctx.send("Les règles:\n1. Pas d'insultes\n2. Pas de double compte\n3. Pas de spam")








# phrase
print("Lancement du bot...")

# connecter au serveur
bot.run("process.env.TOKEN")
