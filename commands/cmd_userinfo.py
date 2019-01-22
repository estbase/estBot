from discord import Embed


async def handle(args, message, client, invoke):
    try:
        user = message.author
        em = Embed(
            title="Your Discord profile info",
            description="You can view your actual user information on discord",
            colour=0x708DD0
        )
        em.add_field(name='User ID', value=user.id, inline=True)
        em.add_field(name='Nick', value=user, inline=True)
        em.add_field(name='Status', value=user.status, inline=True)
        em.add_field(name='Highest Role', value=user.top_role.name, inline=True)
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.set_footer(text="You can visit us on https://www.estbase.org")
        em.set_author(name="EST Base Discord Bot", icon_url='https://cdn.discordapp.com/avatars/536867877702205450/7a612de5dcce089db07e4d18799b013b.png')
        em.set_thumbnail(url='https://cdn.discordapp.com/avatars/536867877702205450/7a612de5dcce089db07e4d18799b013b.png')
        await client.send_message(message.channel, embed=em)
    except Exception as error:
        print("Some error has been occurred on executing {}. Error: {}".format(invoke, error))
