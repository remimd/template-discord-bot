from blacksheep.client import ClientSession
from discord import Webhook, AsyncWebhookAdapter


async def send(webhook_url: str, **kwargs):
    async with ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
        await webhook.send(**kwargs)
