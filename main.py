import logging
import asyncio
import configparser
from pyrogram import Client, filters, idle, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger(__name__)

configuration_file = "working_dir/config.ini"
config = configparser.ConfigParser()
config.read(configuration_file)

token = config.get("bot", "token")
admin_group = int(config.get("bot", "admin_group"))
dest_chan = int(config.get("bot", "dest_chan"))

review_rep_resp = "As a reply to this message send me the final confession to be posted."

bot = Client(
    session_name="confessionmvbot",
    workers=200,
    workdir="working_dir",
    bot_token=token,
    config_file=configuration_file
)


@bot.on_message(~filters.chat(admin_group) & ~filters.command("start") & filters.private)
async def new_confessions_handler(_, m: Message):
    fd_msg = await m.forward(admin_group)
    await fd_msg.reply_text(
        f"<i>Confession by user <a href=tg://user?id={m.from_user.id}>{m.from_user.first_name}</a></i>",
        reply_to_message_id=fd_msg.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text=f"{emoji.MEMO} Review", callback_data="review"),
                    InlineKeyboardButton(text=f"{emoji.CHECK_MARK} Approve", callback_data="approve")
                ]
            ]
        )
    )


@bot.on_callback_query(filters.regex("review"))
async def review_callback_handler(_, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_reply_markup()
    await cb.message.reply_text(
        review_rep_resp
    )


@bot.on_callback_query(filters.regex("approve"))
async def approve_callback_handler(_, cb: CallbackQuery):
    await cb.message.reply_to_message.copy(dest_chan)
    await cb.edit_message_reply_markup()
    await cb.answer("Confession has been posted!", show_alert=True)


@bot.on_message(filters.reply & filters.chat(admin_group))
async def review_reply_handler(_, m: Message):
    if m.reply_to_message.text == review_rep_resp:
        await m.copy(dest_chan)
        await m.reply_to_message.edit_text(
            "<i>This confession has been reviewed and Posted!</i>"
        )


@bot.on_message(filters.command("start"))
async def start_command_handler(_, m: Message):
    await m.reply_text(
        "Send me your confession and on behalf of you I will submit them to admin's for approval."
    )


async def main():
    await bot.start()
    await idle()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
