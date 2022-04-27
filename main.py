from api import application
from core.bot import Bot


app = application


@app.after_start
async def after_start(_):
    bot = Bot.get_instance()
    bot.run_in_event_loop()
