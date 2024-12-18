import logging

import discord
from discord import DMChannel, TextChannel

from discord_public_ip_publisher.ipify import get_public_ip

_LOGGER = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True  # Need "privileged access" ...

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    _LOGGER.info(f'We have logged in as {client.user}')
    public_ip = await get_public_ip()
    for guild in client.guilds:
        for channel in guild.channels:
            if isinstance(channel, TextChannel) and channel.position == 0:
                await channel.send(f"Hello, my server IP is {public_ip}.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    _LOGGER.info(f'Received message: "{message.content}" ({message}).')
    if message.content.lower().startswith('hello'):
        await message.channel.send("Hello =)")
        return

    public_ip = await get_public_ip()
    if message.content == '/server_ip':
        await message.channel.send(f"My public IP is {public_ip}.")
    elif isinstance(message.channel, DMChannel):
        await message.channel.send(f"I do not know what you mean. But here is my IP: {public_ip}.")


def start_bot():
    with open('.discord_token') as token_file:
        token = token_file.read()
    client.run(token)
