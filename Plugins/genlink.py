import re
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, UsernameInvalid, UsernameNotModified
from info import ADMINS, LOG_CHANNEL, FILE_STORE_CHANNEL
from database.ia_filterdb import unpack_new_file_id
from utils import temp
import re
import os
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@Client.on_message(filters.command('link') & filters.user(ADMINS))
async def gen_link_s(bot, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply('Reply to a message to get a shareable link.')
    file_type = replied.media
    if file_type not in ["video", 'audio', 'document']:
        return await message.reply("Reply to a supported media")
    file_id, ref = unpack_new_file_id((getattr(replied, file_type)).file_id)
    await message.reply(f"Here is your Link:\nhttps://t.me/{temp.U_NAME}?start={file_id}")
    
@Client.on_message(filters.command('batch') & filters.private & ~filters.bot)
async def gen_link_batch(bot:Client, message:Message):
    
    user_id = message.from_user.id
    post1:Message = await bot.ask(chat_id=message.chat.id, text="Forward the First Message from Your Channel (with Quotes).. ", timeout=360) 
    if not post1: return
    
    if not post1.forward_from_chat: 
 
        await message.reply_text("Please Forward The Message With Quotes (ie : Forwarded From ...)") 
        return 
 
    f_chat_id = post1.forward_from_chat.id 
    f_msg_id = post1.forward_from_message_id
    
    try:
        chat_id = (await bot.get_chat(f_chat_id)).id
    except ChannelInvalid:
        return await message.reply('<b>This may be a private channel / group. Make me an admin over there to index the files.</b>')
    except Exception as e:
        return await message.reply(f'<b>This may be a private channel / group. Make me an admin over there to index the files.</b>\n\nErrors - {e}')
 

 
    post2 = await bot.ask(chat_id=message.chat.id, text="Now Forward The Last Message From The Same Channel", timeout=360) 
    if not post2 : return 
 
    if not post1.forward_from_chat: 
 
        await message.reply_text("Please Forward The Message With Quotes (ie : Forwarded From ...)") 
        return
    
    l_chat_id = post2.forward_from_chat.id 
    l_msg_id = post2.forward_from_message_id
    
    
    if not f_chat_id==l_chat_id : 
        return await message.reply_text("These Two Messages Arent From The Same Chat") 
    
    try:
        chat_id = (await bot.get_chat(l_chat_id)).id
    except ChannelInvalid:
        return await message.reply('<b>This may be a private channel / group. Make me an admin over there to index the files.</b>')
    except Exception as e:
        return await message.reply(f'<b>This may be a private channel / group. Make me an admin over there to index the files.</b>\n\nErrors - {e}')

    sts = await message.reply("Generating link for your message.\nThis may take time depending upon number of messages")
    if chat_id in FILE_STORE_CHANNEL:
        string = f"{f_msg_id}_{l_msg_id}_{chat_id}"
        b_64 = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
        return await sts.edit(f"Here is your link https://telegram.dog/{temp.U_NAME}?start=DSTORE-{b_64}", disable_web_page_preview=True)

    msgs_list = []
    c_msg = f_msg_id
    
    diff = l_msg_id - f_msg_id
    
    FRMT = "Generating Link...\nTotal Messages: `{total}`\nDone: `{current}`\nRemaining: `{rem}`\nStatus: `{sts}`"
    if diff <= 200:
        msgs = await bot.get_messages(f_chat_id, list(range(f_msg_id, l_msg_id+1)))
        msgs_list += msgs
    else:
        c_msg = f_msg_id
        while True:
            new_diff = l_msg_id - c_msg
            if new_diff > 200:
                new_diff = 200
            elif new_diff <= 0:
                break
            print(new_diff, c_msg)
            msgs = await bot.get_messages(f_chat_id, list(range(c_msg, c_msg+new_diff)))
            msgs_list += msgs
            try:
                await sts.edit(FRMT.format(total=diff, current=(c_msg - f_msg_id), rem=(l_msg_id - c_msg), sts="Fetching Messages"))
            except:
                pass
            c_msg += new_diff

    outlist = []
    
    # file store without db channel
    og_msg = 0
    tot = 0
    for msg in msgs_list:
        tot += 1
        if msg.empty or msg.service:
            continue
        if not msg.media:
            # only media messages supported.
            continue
        try:
            file_type = msg.media
            file = getattr(msg, file_type)
            if file:
                file = {
                    "file_id": file.file_id,
                    "caption": msg.caption,
                    "title": getattr(file, "file_name", ""),
                    "size": file.file_size,
                }
                og_msg +=1
                outlist.append(file)
        except:
            pass
        if not og_msg % 20:
            try:
                await sts.edit(FRMT.format(total=diff, current=tot, rem=(diff - tot), sts="Saving Messages"))
            except:
                pass
    with open(f"batchmode_{message.from_user.id}.json", "w+") as out:
        json.dump(outlist, out)
    post = await bot.send_document(LOG_CHANNEL, f"batchmode_{message.from_user.id}.json", file_name="Batch.json", caption="⚠️Generated for filestore.")
    os.remove(f"batchmode_{message.from_user.id}.json")
    file_id, ref = unpack_new_file_id(post.document.file_id)
    await sts.edit(f"Here is your link\nContains `{og_msg}` files.\nhttps://t.me/{temp.U_NAME}?start=BATCH-{file_id}", disable_web_page_preview=True)
