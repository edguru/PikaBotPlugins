"""Alive Plugin for Pikabot
{i}alive
"""
# Made by @ItzSjDude. All Rights Reserved

import asyncio

from pikabot import *
from pikabot.main_plugs.plug import *
from pikabot.utils import *
from pikabot.utils import get_readable_time as grt


@ItzSjDude(outgoing=True, pattern=r"alive$")
async def _(event):
    pupt = grt((time.time() - UpTime))
    try:
        pic = await pikaa(event, "ALIVE_PIC")
    except:
        pic = apic
    az = await pikaa(event, "ALIVE_NAME")
    await event.delete()
    a = await event.client.send_file(
        event.chat_id, pic, caption=alivestr.format(pupt, az)
    )
    await asyncio.sleep(15)
    await a.delete()
