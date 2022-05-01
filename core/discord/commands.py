from discord_slash import SlashContext

from core.discord.bot import Bot


bot = Bot.get_instance()


@bot.slash.slash(name="ping", description='Display "Pong" with latency.')
async def _ping(ctx: SlashContext):
    bot.check_disable()
    await ctx.send(content=f"Pong! `{round(ctx.bot.latency*1000)}ms`")
