import discord, asyncio, json

from discord.ext import commands

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
pizza_delay = config.get('use_pizza_delay')

bot = commands.Bot(command_prefix=config.get('prefix'), self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Successfully Authorised as: " + bot.user.name + " UID: (" + str(bot.user.id) + ")")
    print('Use $pizza [amount] in any channel to begin! ')

@bot.command()
async def pizza(ctx, amount: int):
    await ctx.message.delete()
    for i in range(0,amount):
        async with ctx.typing():
            await asyncio.sleep(amount)
        await ctx.send("pls use pizza")
        await asyncio.sleep(1)

bot.run(token, bot=False)

