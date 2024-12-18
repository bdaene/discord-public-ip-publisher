import logging

import httpx

_LOGGER = logging.getLogger(__name__)


async def get_public_ip():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.ipify.org/')
    public_ip = response.text
    _LOGGER.info(f"Public IP is: {public_ip}")
    return public_ip
