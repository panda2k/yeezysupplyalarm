import os
import discord
from discord.ext import commands
from subprocess import Popen
from yeezysupplymonitor import YeezySupplyMonitor
import logging

for key in logging.Logger.manager.loggerDict:
    if key.find('discord') != -1 or key.find('websockets') != -1:
        logging.getLogger(key).setLevel(logging.WARNING)   

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
threads = {}

@bot.event
async def on_ready():
    # connection message
    print(f'{bot.user} has connected to Discord')

@bot.command(name='add-monitor')
async def add_monitor(ctx, product_sku: str):
    # create monitor thread
    if product_sku in threads:
        await ctx.channel.send(f'Already monitoring SKU {product_sku}')
    else:
        threads[product_sku] = YeezySupplyMonitor(product_sku, 60)
        threads[product_sku].start()
        await ctx.channel.send(f'Now monitoring {product_sku}')

@bot.command(name='remove-monitor')
async def remove_monitor(ctx, product_sku: str):
    # remove monitor thread
    try:
        threads[product_sku].stop()
        await ctx.channel.send(f'Stopped monitoring SKU {product_sku}')
    except KeyError as error:
        await ctx.channel.send(f'There is no thread monitoring SKU {product_sku}')
    

@bot.command(name='list-monitors')
async def list_monitors(ctx):
    # list monitors
    skus = ""
    for key in threads.keys():
        skus += key + ", "
    if len(skus) == 0:
        await ctx.channel.send('Not currently monitoring any SKUs')
    else:
        await ctx.channel.send('Currently monitoring these SKUs: ' + skus)

bot.run(TOKEN)
