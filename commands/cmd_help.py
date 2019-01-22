from discord import Embed


async def handle(args, message, client, invoke):
    try:
        em = Embed(
            description="You can use two prefixes for use all commands: '!' or ''",
            colour=0x708DD0
        )
        em.add_field(name='ping', value="Sent to you a private message with your private and public IP", inline=False)
        em.add_field(name='ip', value="Sent to you a private message with your IP, City, and all info with yor trace.", inline=False)
        em.add_field(name='clear [i]', value="Delete last [i] number of messages.", inline=False)
        em.add_field(name='userinfo', value="Show util user info about your discord user", inline=False)
        em.set_footer(text="You can visit us on https://www.estbase.org")
        em.set_author(name="EST Base Discord Bot", icon_url='https://cdn.discordapp.com/avatars/536867877702205450/7a612de5dcce089db07e4d18799b013b.png')
        em.set_thumbnail(url='https://cdn.discordapp.com/avatars/536867877702205450/7a612de5dcce089db07e4d18799b013b.png')
        await client.send_message(message.channel, embed=em)
    except Exception as error:
        print("Some error has been occurred on executing {}. Error: {}".format(invoke, error))
