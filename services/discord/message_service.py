def mention_role(discord_role_id: int) -> str:
    return f"<@&{discord_role_id}>"


def mention_user(discord_user_id: int) -> str:
    return f"<@{discord_user_id}>"
