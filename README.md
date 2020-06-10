# Yeezy Supply Alarm
This is a simple script that will monitor a product SKU on Yeezysupply.com. If the product is live and available to purchase, it will play a song on your Google Home. This is all controlled through a discord bot


## Installation
Clone the repository using either Github's web interface or through the command line. To use the command line, type this command: `git clone https://github.com/panda2k/yeezysupplyalarm.git`.


Navigate to the cloned directory and install the dependencies with pip. `pip install -r requirements.txt`


Create a discord token for your bot. For detailed instructions, go to https://discordpy.readthedocs.io/en/latest/discord.html


Once you have your discord bot token, set the system variable `DISCORD_TOKEN` equal to your discord bot token.


## Usage
Run the bot by doing `python wakeupbot.py` The bot will then send a message to #general in your discord server. 


When the bot launches, it'll ask you to input the name of your google home. Input the name of your google home as it appears on the google home app.


### Monitoring a product
To start monitoring for a product, type the command `!add-monitor SKUHERE` into any channel on your discord server. When the product goes live, it will play a song on your google home. 


### Stop monitoring a product
Type the command `!remove-monitor SKUHERE` into any channel on your discord server. If this is successful, the discord bot will say it stopped monitoring that SKU. 


### List all monitors
Type `!list-monitors` into any channel and the bot will respond with the SKUs currently being monitored.


### Future Development
This project is not being currently developed and it may not work in the future due to changing endpoints on Yeezysupply. 


#### Contributing
If you want to contribute to this project, open a pull request.


#### Reporting Issues
To report issues, open a issue thread. If it is an endpoint related problem, I will likely not work on fixing it since this project is not in active development. However, if you have an issue setting up, I'll be happy to help you. 
