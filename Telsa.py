import os 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
import random


HB = Client(
    "MSG_DELETING Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)  
Username = "THOR_online"



START_TEXT = """HI {}, 
I CAN PROVIDE MOVIES 
MADE BY @TELSABOTS
"""
HELP_TEXT = """
JIUST SENT ANY MOVIE NAME 
❌DONT SENT YEAR 
❌ DONT SENT LANGAUGES 
✅ONLY SENT MOVIE NAME 
eg:- KGF2 

MADE BY @TELSABOTS
"""
ABOUT_TEXT = """
 🤖<b>BOT:DISCUSS UNPIN🤖</b>
 
📢<b>CHANNEL :</b> ❤️ <a href='https://t.me/telsabots'>TELSA BOTS❤️</a>

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

 
🤩<b>SOURCE :</b> 🤩 <a href='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'>CLICK HERE❤️</a>

"""
feedback_text ="""**😍DUDE YOU CAN REQUEST \n MOVIE THROUGH HERE \n\n😉JUST SENT MOVIE NAME\n\neg:-/feedback kgf2**"""
SOURCE_TEXT = """</b>PRESS SOURCE BUTTON FOR SOURCE 
AND WATCH TOTOURIAL VIDEO IF YOU WANT ANY HELP</b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/watch?v=sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🤩SOURCE🤩', url='https://youtu.be/sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

close_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )




@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await update.message.delete()

 
@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     

WELCOME_MESSAGE_BUTTONS = [
    [
        InlineKeyboardButton('📢CHANNEL📢', url="https://t.me/+UZzc1ZqHvYXaLeNf"),
        InlineKeyboardButton('📢NEW MOVIES📢', url="https://t.me/+b31QfnWFdmcwYzVl")
        ],[
            InlineKeyboardButton('🧑‍💻DEV🧑‍💻', url="https://t.me/alluaddict"),
            InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]
]

import names
@HB.on_message(filters.command(["female"]))
async def female(bot, update):
    text = ("NAME =" +names.get_first_name(gender ="male") )
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )  
   

print("hb")
HB.run()




