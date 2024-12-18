import logging

import discord

from discord_public_ip_publisher.ipify import get_public_ip

_LOGGER = logging.getLogger(__name__)

intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    logging.info(f'Received message: "{message.content}" ({message}).')
    public_ip = await get_public_ip()
    if message.content == '/server_ip':
        await message.channel.send(public_ip)
    else:
        await message.channel.send(f"I do not know what you mean. But here is my IP: {public_ip}.")


def start_bot():
    with open('.discord_token') as token_file:
        token = token_file.read()
    client.run(token)
