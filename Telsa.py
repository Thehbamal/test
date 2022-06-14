import os 
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
HB = Client(
    "MSG_DELETING Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)  

START_TEXT = """**HI {}, 
I CAN GENERATE RANDOM  NAMES FOR YOU 
JUST PRESS HELP BUTTON
TO KNOW HOW TO USE ME
MADE BY @TELSABOTS**
"""
HELP_TEXT = """
JUST SENT /NAME 
THEN I WILL SENT  NAMES 

MADE BY @TELSABOTS
"""
ABOUT_TEXT = """
 🤖<b>BOT:NAME GENERATOR 🤖</b>
📢<b>CHANNEL :</b> @TELSA BOTS
🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT
"""


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
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
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
result_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡HOME🏡', callback_data='male'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='female'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
male_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡NEXT🏡', callback_data='nextmale'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='female'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
female_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡NEXT🏡', callback_data='nextfemale'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='female'),
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
    elif update.data == "male":
        await update.message.edit_text(
            text=("**NAME : **" +names.get_first_name(gender ="male")),
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
    elif update.data == "female":
        await update.message.edit_text(
            text=("**NAME : **" +names.get_first_name(gender ="female")),
            disable_web_page_preview=True,
            reply_markup=female_BUTTONS
    elif update.data == "female_BUTTONS":
        await update.message.edit_text(
            text=("**NAME : **" +names.get_first_name(gender ="female")),
            disable_web_page_preview=True,
            reply_markup=female_BUTTONS
    elif update.data == "male_BUTTONS":
        await update.message.edit_text(
            text=("**NAME : **" +names.get_first_name(gender ="male")),
            disable_web_page_preview=True,
            reply_markup=male_BUTTONS
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
    


import names
@HB.on_message(filters.command(["male"]))
async def female(bot, update):
    text = ("**NAME : **" +names.get_first_name(gender ="male"))
    reply_markup =result_BUTTONS 
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )  
@HB.on_message(filters.command(["female"]))
async def female(bot, update):
    text = ("**NAME : **" +names.get_first_name(gender ="female"))
    reply_markup = result_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )  
   

print("hb")
HB.run()




