from pyrogram import Client, filters
from config import *
import asyncio


def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"


async def listaa(c, table, text):
    txx = f"{text}\n"
    ii = 1
    for i in table:
        try:
            x = await c.get_users(i)
            if x.username:
                username = f"@{x.username}"
            else:
                username = i
        except:
            username = i
        txx += f"{ii} - {username} \n"
        ii += 1
    return txx


@Client.on_message(filters.command("زواج$", prefixes=f".") & filters.me & filters.reply)
async def zawg(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انتة شنو ولك تزوج نفسك😂🔥 ؟")
    r.sadd(f"{sudo_id}zwag", msg.reply_to_message.from_user.id)
    txx = f"• تم زواجك من {get_name(msg.reply_to_message)} \n• مبروك"
    await msg.edit(txx)


@Client.on_message(filters.command("طلاق$", prefixes=f".") & filters.me & filters.reply)
async def tlak(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هتطلق نفسك ؟")
    r.srem(f"{sudo_id}zwag", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم طلاقك منه بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح زوجاتي$", prefixes=f".") & filters.me)
async def del_zawgaty(c, msg):
    r.delete(f"{sudo_id}zwag")
    txx = f"• تم مسح زوجاتك بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("زوجاتي$", prefixes=f".") & filters.me)
async def zawgaty(c, msg):
    list1 = r.smembers(f"{sudo_id}zwag")
    txx = await listaa(c, list1, "==== قائمه زوجاتك =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع خول$", prefixes=f".") & filters.me & filters.reply)
async def khwl(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك خول ؟")
    r.sadd(f"{sudo_id}khwlt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه خول بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل خول$", prefixes=f".") & filters.me & filters.reply)
async def unkhwl(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}khwlt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه الخولات بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح الخولات$", prefixes=f".") & filters.me)
async def del_khwlaty(c, msg):
    r.delete(f"{sudo_id}khwlt")
    txx = f"• تم مسح الخولات بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("الخولات$", prefixes=f".") & filters.me)
async def khwlaty(c, msg):
    list1 = r.smembers(f"{sudo_id}khwlt")
    txx = await listaa(c, list1, "==== قائمه الخولات =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع عرص$", prefixes=f".") & filters.me & filters.reply)
async def ars(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك عرص ؟")
    r.sadd(f"{sudo_id}arst", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه عرص بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل عرص$", prefixes=f".") & filters.me & filters.reply)
async def unars(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}arst", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه المعرصين بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح المعرصين$", prefixes=f".") & filters.me)
async def del_arsaty(c, msg):
    r.delete(f"{sudo_id}arst")
    txx = f"• تم مسح المعرصين بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("المعرصين$", prefixes=f".") & filters.me)
async def arsaty(c, msg):
    list1 = r.smembers(f"{sudo_id}arst")
    txx = await listaa(c, list1, "==== قائمه المعرصين =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع كلب$", prefixes=f".") & filters.me & filters.reply)
async def dog(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك كلب ؟")
    r.sadd(f"{sudo_id}dogt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه كلب بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل كلب$", prefixes=f".") & filters.me & filters.reply)
async def undog(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}dogt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه الكلاب بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح الكلاب$", prefixes=f".") & filters.me)
async def del_dogaty(c, msg):
    r.delete(f"{sudo_id}dogt")
    txx = f"• تم مسح الكلاب بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("الكلاب$", prefixes=f".") & filters.me)
async def dogaty(c, msg):
    list1 = r.smembers(f"{sudo_id}dogt")
    txx = await listaa(c, list1, "==== قائمه الكلاب =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع متوحد$", prefixes=f".") & filters.me & filters.reply)
async def motaw(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك متوحد ؟")
    r.sadd(f"{sudo_id}motawt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه متوحد بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل متوحد$", prefixes=f".") & filters.me & filters.reply)
async def unmotaw(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}motawt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه المتوحدين بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح المتوحدين$", prefixes=f".") & filters.me)
async def del_motawaty(c, msg):
    r.delete(f"{sudo_id}motawt")
    txx = f"• تم مسح المتوحدين بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("المتوحدين$", prefixes=f".") & filters.me)
async def motawaty(c, msg):
    list1 = r.smembers(f"{sudo_id}motawt")
    txx = await listaa(c, list1, "==== قائمه المتوحدين =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع حمار$", prefixes=f".") & filters.me & filters.reply)
async def donky(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك حمار ؟")
    r.sadd(f"{sudo_id}donkyt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه حمار بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل حمار$", prefixes=f".") & filters.me & filters.reply)
async def undonky(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}donkyt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه الحمير بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح الحمير$", prefixes=f".") & filters.me)
async def del_donkyaty(c, msg):
    r.delete(f"{sudo_id}donkyt")
    txx = f"• تم مسح الحمير بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("الحمير$", prefixes=f".") & filters.me)
async def donkyaty(c, msg):
    list1 = r.smembers(f"{sudo_id}donkyt")
    txx = await listaa(c, list1, "==== قائمه الحمير =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع بقلبي$", prefixes=f".") & filters.me & filters.reply)
async def kalpy(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك بقلبي ؟")
    r.sadd(f"{sudo_id}kalpyt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه بقلبي بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل بقلبي$", prefixes=f".") & filters.me & filters.reply)
async def unkalpy(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}kalpyt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه القلوب بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح القلوب$", prefixes=f".") & filters.me)
async def del_kalpyaty(c, msg):
    r.delete(f"{sudo_id}kalpyt")
    txx = f"• تم مسح القلوب بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("القلوب$", prefixes=f".") & filters.me)
async def kalpyaty(c, msg):
    list1 = r.smembers(f"{sudo_id}kalpyt")
    txx = await listaa(c, list1, "==== قائمه القلوب =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع شاذ$", prefixes=f".") & filters.me & filters.reply)
async def gay(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك شاذ ؟")
    r.sadd(f"{sudo_id}gayt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه شاذ بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل شاذ$", prefixes=f".") & filters.me & filters.reply)
async def ungay(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}gayt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه الشواذ بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح الشواذ$", prefixes=f".") & filters.me)
async def del_gayaty(c, msg):
    r.delete(f"{sudo_id}gayt")
    txx = f"• تم مسح الشواذ بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("الشواذ$", prefixes=f".") & filters.me)
async def gayaty(c, msg):
    list1 = r.smembers(f"{sudo_id}gayt")
    txx = await listaa(c, list1, "==== قائمه الشواذ =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع ابني$", prefixes=f".") & filters.me & filters.reply)
async def abny(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك ابني ؟")
    r.sadd(f"{sudo_id}abnyt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه ابني بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل ابني$", prefixes=f".") & filters.me & filters.reply)
async def unabny(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}abnyt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه اولادي بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح اولادي$", prefixes=f".") & filters.me)
async def del_abnyaty(c, msg):
    r.delete(f"{sudo_id}abnyt")
    txx = f"• تم مسح اولادي بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("اولادي$", prefixes=f".") & filters.me)
async def abnyaty(c, msg):
    list1 = r.smembers(f"{sudo_id}abnyt")
    txx = await listaa(c, list1, "==== قائمه اولادي =====")
    await msg.edit(txx)


@Client.on_message(filters.command("رفع بنتي$", prefixes=f".") & filters.me & filters.reply)
async def banty(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• انت عبيط عاوز ترفع نفسك بنتي ؟")
    r.sadd(f"{sudo_id}bantyt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم رفعه بنتي بنجاح  "
    await msg.edit(txx)


@Client.on_message(filters.command("تنزيل بنتي$", prefixes=f".") & filters.me & filters.reply)
async def unbanty(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        return await msg.edit("• هاي قناة يخبل ☺️🔥")
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• هترفع نفسك ؟")
    r.srem(f"{sudo_id}bantyt", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم تنزيله من قائمه بناتي بنجاح ✅"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح بناتي$", prefixes=f".") & filters.me)
async def del_bantyaty(c, msg):
    r.delete(f"{sudo_id}bantyt")
    txx = f"• تم مسح بناتي بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("بناتي$", prefixes=f".") & filters.me)
async def bantyaty(c, msg):
    list1 = r.smembers(f"{sudo_id}bantyt")
    txx = await listaa(c, list1, "==== قائمه بناتي =====")
    await msg.edit(txx)
