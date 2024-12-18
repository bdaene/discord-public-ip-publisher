import asyncio
import logging

from discord_public_ip_publisher.discord_bot import start_bot
from discord_public_ip_publisher.ipify import get_public_ip


def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(get_public_ip())
    start_bot()


if __name__ == "__main__":
    main()
