import os
import discord
from discord.ext import commands
from subprocess import Popen

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
subprocess_list = []

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')

@bot.command(name='add-monitor')
async def add_monitor(ctx, product_sku: str):
    monitor_process = Popen(f'python -c "from yeezysupplymonitor import YeezySupplyMonitor; monitor = YeezySupplyMonitor(); monitor.monitor_site(\\"{product_sku}\\", 60)"', shell=True)
    subprocess_list.append((product_sku, monitor_process))
    await ctx.channel.send(f'Started monitor task with PID {monitor_process.pid}')
    await ctx.channel.send(f'Now monitoring {product_sku}')


@bot.command(name='remove-monitor')
async def remove_monitor(ctx, product_sku: str):
    for monitor in subprocess_list:
        if monitor[0] == product_sku:
            monitor[1].kill()
            subprocess_list.remove(monitor)
            await ctx.channel.send(f'Stopped monitoring {product_sku}')
            return
    await ctx.channel.send('There is no process monitoring SKU ' + product_sku)
    

@bot.command(name='list-monitors')
async def list_monitors(ctx):
    skus = ""
    for monitor in subprocess_list:
        skus += monitor[0]
    if len(skus) == 0:
        await ctx.channel.send('Not currently monitoring any SKUs')
    else:
        await ctx.channel.send('Currently monitoring these SKUs: ' + skus)

bot.run(TOKEN)
