import discord
import asyncio


async def handle(args, message, client, invoke):
    try:
        amount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(),
                                                                       descrition="Please enter a valid value for message ammount!"))
        return

    # SLOW ONE:
    # cleared = 0
    # failed = 0
    #
    # async for m in client.logs_from(message.channel, limit=amount):
    #     try:
    #         await client.delete_message(m)
    #         cleared += 1
    #     except:
    #         failed += 1
    #         pass
    #
    # failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""
    # returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(),
    #                                                                            description="Cleared %s message(s).%s" % (
    #                                                                                cleared, failed_str)))
    # await asyncio.sleep(4)
    # await client.delete_message(returnmsg)

    # QUICK ALTERNATIVE:
    messages = []
    async for m in client.logs_from(message.channel, limit=amount):
        messages.append(m)
    await client.delete_messages(messages)
    return_msg = await client.send_message(message.channel, embed=discord.Embed(colour=0x708DD0,
                                                                                description="Successfully cleared `%s message(s)`." % (
                                                                                    amount-1)))
    await asyncio.sleep(5)
    await client.delete_message(return_msg)
