# Edit By @pikyus1

from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.thanks(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "╔══╦╗────╔╗─╔╗╔╗\n"
                     "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
                     "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
                     "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")


@register(outgoing=True, pattern='^.malam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╔═╦═╦╗╔═╦══╦═╦══╗\n"
                     "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
                     "╠═║═╣╚╣║║║║║║║║║\n"
                     "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
                     "╔══╦═╦╗╔═╦══╗\n"
                     "║║║║╬║║║╬║║║║\n"
                     "║║║║║║╚╣║║║║║\n"
                     "╚╩╩╩╩╩═╩╩╩╩╩╝")


@register(outgoing=True, pattern='^.rumah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAMBAR RUMAH**\n"
                     "╱◥◣\n"
                     "│∩ │◥███◣ ╱◥███◣\n"
                     "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
                     "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
                     "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
                     "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑")

CMD_HELP.update({
    "animasi6":
    "`.rumah` ; `.malam` ; `.teks`\
    \nUsage: liat aja."
})