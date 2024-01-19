from random import randint
from typing import Optional
from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
import asyncio
from pyrogram.types import Message

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.edit(f"{err_msg}")
    return False

@Client.on_message(filters.command("فتح الكول$", prefixes=f".") & filters.me)
async def opengc(c, msg):
    await msg.edit("جاري فتح الكول")
    if (
        group_call := (
            await get_group_call(c, msg, err_msg="الكول مفتوح")
        )
    ):
        await msg.edit("الكول مفتوح اصلا يكينج")
        return
    try:
            await c.invoke(
                CreateGroupCall(
                    peer=(await c.resolve_peer(msg.chat.id)),
                    random_id=randint(10000, 999999999),
                )
            )
            await msg.edit("تم فتح الكول بنجاح.")
    except Exception as e:
        await msg.edit("انتة مو ادمن اصلا")
@Client.on_message(filters.command("قفل الكول$", prefixes=f".") & filters.me)
async def end_vc(c, msg):
    chat_id = msg.chat.id
    if not (
        group_call := (
            await get_group_call(c, msg, err_msg="الكول مقفلول اصلا يكينج")
        )
    ):
        await msg.edit("الكول مقفول اصلا يزمال 😂🔥")
        return
    try:
      await c.invoke(DiscardGroupCall(call=group_call))
      await msg.edit("تم قفل الكول بنجاح.")
    except:
        await msg.edit("انتة مو ادمن اصلا")