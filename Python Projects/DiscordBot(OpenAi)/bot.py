import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA5MTc3MDMyODQ0NDgzNzk5OQ.GM24SZ.WQaW1JRTgW6BntCZYEaFid8kvt4xjHKohBMbOI'
    # intents = discord.Intents.default()
    # intents.message_content = True
    # (intents=intents)

    intents = discord.Intents.all()
    client = discord.Client(command_prefix="-", intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '&':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        elif user_message[0] == '?':
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
