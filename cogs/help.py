from discord.ext import commands


class Help:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pong(self):
        await self.client.say('Ping!')


def setup(client):
    client.add_cog(Help(client))
