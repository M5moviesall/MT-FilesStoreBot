# (c) @MRK_YT

from configs import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="**Sorry Sir😔**, **You are Banned to use me. Contact my** [Support Group](https://t.me/Mo_Tech_Group).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**സിനിമ വേണമെങ്കിൽ ആദ്യമേ ഞങ്ങളുടെ യൂട്യൂബ് ചാനലിലെ സബ്സ്ക്രൈബ് ബട്ടണിൽ  ഒരു ചെറിയ കൈക്രിയ നടത്തണം അതിനുശേഷം ഞങ്ങളുടെ മെയിൻ ചാനലിലും ഒരു ചെറിയ കൈക്രിയ നടത്തണം എങ്കിലേ സിനിമ കിട്ടത്തുള്ളൂ എന്ന് പറഞ്ഞു തലൈവർ കടുംവെട്ട് അമ്മച്ചി 😁😁🤣\nജോയിൻ ചെയ്ത ശേഷം ' 🔁 REFRESH 🔁 ' ബട്ടൺ ക്ലിക്ക് ചെയ്യൂ 😊**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔊 𝐉𝐨𝐢𝐧 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🔊", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🎉 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞𝐫𝐬 𝐘𝐓 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🎉", url="https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ")
                    ],
                    [
                        InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡 🔄", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/Mo_Tech_Group).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
