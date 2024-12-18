# Discord Public IP Publisher 

A small public IP publisher for Discord.

Based on https://discordpy.readthedocs.io and https://api.ipify.org/

## Installation

- Install uv: https://docs.astral.sh/uv/
- Clone the project: ...
- `cd discord-public-ip-publisher`
- `uv sync`

## Create a bot account

See https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro.

Only permission needed is `text:send_messages`

Enable privileged intent: https://discordpy.readthedocs.io/en/stable/intents.html#privileged-intents

Reset your bot token to allow to copy it (yes reset it).
Create a file '.discord_token' and copy the token into it.

## Run

In the project directory (discord-public-ip-publisher)

`uv run discord-public-ip-publisher`

If everything is correctly setup, the bot should say hello on the general channel of the server.

## Usage

Now when typing '\server_ip', the bot should respond with its public IP.

You can also DM (direct message) the bot andit should respond you. 
