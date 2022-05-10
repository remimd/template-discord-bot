import asyncio
from typing import Iterable

from aiohttp import ClientSession
from discord import AsyncWebhookAdapter, Webhook


async def send(webhook_url: str, **kwargs):
    async with ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
        await webhook.send(**kwargs)


async def send_to_multiple(webhooks_urls: Iterable[str], **kwargs):
    await asyncio.gather(send(url, **kwargs) for url in webhooks_urls)
