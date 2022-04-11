# Thanks Full To Team Ultroid
# Ported By Vcky @VckyouuBitch + @MaafGausahSokap
# Copyright (c) 2021 Geez - Projects
# Geez - Projects https://github.com/Vckyou/Geez-UserBot
# RAM - UBOT https://github.com/ramadhani892/RAM-UBOT
# Ini Belum Ke Fix Ya Bg :')
# Ambil aja gapapa tp Gaguna kaya hidup lu Woakkakaka


from telethon.utils import get_display_name
from telethon.tl import types

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HELP
from userbot.events import register as tod
from userbot.utils import edit_delete, edit_or_reply

NO_ADMIN = "`LU BUKAN ADMIN NGENTOT!!`"

def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(komtol):
    rambot = await komtol.client(getchat(komtol.chat_id))
    rama = await komtol.client(getvc(rambot.full_chat.call, limit=1))
    return rama.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@tod(outgoing=True, pattern="^\.startvc$")
async def start_voice(c):
    await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, "**LO BUKAN ADMIN ANJINGGG!!!!!!**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`OBROLAN SUARA DI NYALAKAN, YANG ONCAM LO NGENTOT!!`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@tod(outgoing=True, pattern="^\.stopvc$")
async def stop_voice(c):
    await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, "**lo bukan admin ngentoootttttt!!!**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`OBROLAN SUARA DI MATIKAN, TYPING AJA YA BABI!!!!`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@tod(outgoing=True, pattern="^\.vcinvite")
async def _(c):
    xxnx = await edit_or_reply(c, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botman = list(user_list(users, 6))
    for p in botman:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await xxnx.edit(f"`{z}` **Orang Berhasil diundang ke VCG**")


@tod(outgoing=True, pattern="^\.vctitle(?: |$)(.*)")
async def change_title(e):
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")


CMD_HELP.update(
    {
        "vcg": f"**Plugin : **`vcg`\
        \n\n  •  **Syntax :** `.startvc`\
        \n  •  **Function : **Untuk Memulai voice chat group\
        \n\n  •  **Syntax :** `.stopvc`\
        \n  •  **Function : **Untuk Memberhentikan voice chat group\
        \n\n  •  **Syntax :** `.vctitle` <title vcg>\
        \n  •  **Function : **Untuk Mengubah title/judul voice chat group\
        \n\n  •  **Syntax :** `.vcinvite`\
        \n  •  **Function : **Mengundang Member group ke voice chat group\
        \n\n  • **Syntax  :** `.joinvc`\
        \n  •  **Function : **Naik ke Obrolan Suara Palsu\
        \n\n  • **Syntax  :** `.leavevc`\
        \n  •  **Function : **Turun Dari Obrolan Suara Palsu\
    "
    }
)
