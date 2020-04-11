import os
import discord

TOKEN = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord')

client = CustomClient()
client.run(TOKEN)
