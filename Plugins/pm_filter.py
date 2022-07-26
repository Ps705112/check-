#Kanged From @TroJanZheX | 
import asyncio
import re
import ast
import json

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty, MessageEmpty
from Script import script
from assets.picture import *
from assets.Quote import quote
import pyrogram
import pyshorteners
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB, SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_name
from database.users_chats_db import db
from plugins.heroku import *
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.instareddb import add_inst_filter, remove_inst, get_ids
from database.filters_mdb import(
   del_all,
   find_filter,
   get_filters,
)
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

url_shortener = pyshorteners.Shortener()

BUTTONS = {}
SPELL_CHECK = {}

@Client.on_message(filters.text & filters.private & filters.incoming)
async def pm_filter(client, message):
    if message.text.startswith("/"):
        return  
    await pm_auto_filter(client, message)

@Client.on_message(filters.group & filters.text & ~filters.edited & filters.incoming)
async def give_filter(client,message):
    name = message.text
    k = await manual_filters(client, message)
    if k == False:
        await auto_filter(client, message)

    if ('stranger' and 'things') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('English', callback_data='stranger_things_E'),
                InlineKeyboardButton('Hindi', callback_data='stranger_things_H')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=STRANGER_THINGS_PIC,
            caption=quote.STRANGER_THINGS_1,
            reply_markup=reply_markup,
            parse_mode='html'
         )
    if 'maradona' in name.lower():
         buttons = [
            [
                InlineKeyboardButton('English', callback_data='Maradona_E')
            ],
            [
               InlineKeyboardButton('Multi Audio', callback_data='Maradona_M')
            ]

         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=MARADONA_PIC,
            caption=quote.MARADONA_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
         )
    if ('money' and 'heist') in name.lower() or name.lower() == 'la casa de papel':
        buttons = [
           [
               InlineKeyboardButton('English', callback_data='money_heist_E'),
               InlineKeyboardButton('Spanish', callback_data='money_heist_S')
           ],
           [
               InlineKeyboardButton('Hindi', callback_data='money_heist_H'),
               InlineKeyboardButton('Telugu', callback_data='money_heist_Te')
           ],
           [
               InlineKeyboardButton('Tamil', callback_data='money_heist_Ta')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
           photo=MONEY_HEIST_PIC,
           caption=quote.MONEY_HEIST_TXT_1,
           reply_markup=reply_markup,
           parse_mode='html'
        )
    if name.lower() == 'you':
         buttons = [
            [
                InlineKeyboardButton('720p', callback_data='you_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='you_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=YOU_PIC,
            caption=quote.YOU_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )
    if ('cobra' and 'kai') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('480p', callback_data='cobra_kai_480p'),
                InlineKeyboardButton('720p', callback_data='cobra_kai_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='cobra_kai_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=COBRA_KAI_PIC,
            caption=quote.COBRA_KAI_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if ('all' and 'of' and 'us' and 'are') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('480p', callback_data='AOUAD_480p'),
                InlineKeyboardButton('720p', callback_data='AOUAD_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='AOUAD_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=AOUAD_PIC,
            caption=quote.AOUAD_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if ('ted' and 'lasso') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('Season 1', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7AUAAlJvKFUrQOLh90ZucBYE'),
                InlineKeyboardButton('Season 2', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7QUAAlJvKFXIau5zyFpLXRYE')
            ],
            [
                InlineKeyboardButton('Close', callback_data='cls')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=TED_LASSO_PIC,
            caption=script.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if 'witcher' in name.lower():
         buttons = [
            [
                InlineKeyboardButton('480p', callback_data='witcher_480p'),
                InlineKeyboardButton('720p', callback_data='witcher_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='witcher_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=WITCHER_PIC,
            caption=quote.WITCHER_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if ('peaky' and 'blinders') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('720p', callback_data='peaky_blinders_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='peaky_blinders_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=PEAKY_BLINDERS_PIC,
            caption=quote.PEAKY_BLINDERS ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if 'vikings' in name.lower() or 'viking' in name.lower():
         buttons = [
            [
                InlineKeyboardButton('480p', callback_data='vikings_480p'),
                InlineKeyboardButton('720p', callback_data='vikings_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='vikings_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=VIKINGS_PIC,
            caption=quote.VIKINGS_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):

    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer("It's Not For You...", show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    if not search:
        await query.answer("You are using one of my old messages, please send the request again.",show_alert=True)
        return

    files, n_offset, total = await get_search_results(search, offset=offset, filter=True)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0

    if not files:
        return
    fileids = [file.file_id for file in files]
    dbid = fileids[0]
    fileids = "L_I_N_K".join(fileids)
    await add_inst_filter(dbid, fileids)
    if SINGLE_BUTTON:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}┆{get_name(file.file_name)}", url=url_shortener.tinyurl.short(f'https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/{temp.U_NAME}?start={dbid}')
                ),
            ]
            for file in files
        ]

    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}", callback_data=f'files#{file.file_id}'
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'files_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if 0 < offset <= 10:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - 10
    if n_offset == 0:
        btn.append(
            [InlineKeyboardButton("《", callback_data=f"next_{req}_{key}_{off_set}"),
             InlineKeyboardButton("📨",
                                  url ='https://t.me/HB_Suzan_bot')]
        )
        btn.append(
            [
                InlineKeyboardButton(
                    text="🔰 How To Download 🔰", url="https://t.me/+HGEf8Vy3YW02ODM1"
                )
            ]
        )
        
    elif off_set is None:
        btn.append(
           [
              InlineKeyboardButton(
                 f"📃 {round(offset / 10) + 1} / {round(total/10)}",
                 callback_data="pages",
              ),
              InlineKeyboardButton(
                 text="📨", url ='https://t.me/HB_Suzan_bot'
              ), 
              InlineKeyboardButton(
                 "》", callback_data=f"next_{req}_{key}_{n_offset}"
               ),
           ]
        )
        btn.append(
            [
                InlineKeyboardButton(
                    text="🔰 How To Download 🔰", url="https://t.me/+HGEf8Vy3YW02ODM1"
                )
            ]
        )

    else:
        btn.append(
           [
              InlineKeyboardButton("《", callback_data=f"next_{req}_{key}_{off_set}"),
              InlineKeyboardButton(
                 f" 📃 {round(offset / 10) + 1} / {round(total/10)}  ",
                 url='https://t.me/HB_Suzan_bot',
              ),
              InlineKeyboardButton("》", callback_data=f"next_{req}_{key}_{n_offset}")
           ],
        )
        btn.append(
            [
                InlineKeyboardButton(
                    text="🔰 How To Download 🔰", url="https://t.me/+HGEf8Vy3YW02ODM1"
                )
            ]
        )

    try:
        await query.edit_message_reply_markup( 
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()

@Client.on_callback_query(filters.regex(r"^spolling"))
async def advantage_spoll_choker(bot, query):
    _, user, movie_ = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer("It's Not For You 😈", show_alert=True)
    if movie_  == "close_spellcheck":
        return await query.message.delete()
    movies = SPELL_CHECK.get(query.message.reply_to_message.message_id)
    if not movies:
        return await query.answer("You are clicking on an old button which is expired.", show_alert=True)
    movie = movies[(int(movie_))]
    await query.answer('Checking for Movie in database...')
    files, offset, total_results = await get_search_results(movie, offset=0, filter=True)
    if files:
        k = (movie, files, offset, total_results)
        await auto_filter(bot, query, k)
    else:
        k = await query.message.edit('♻️ This Movie Not Uploaded Yet You can **Request to Admin** 👉👉 @Reqyourmovies_bot')
        await asyncio.sleep(10)
        await k.delete()


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    
    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            grpid  = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("Make sure I'm present in your group!!", quote=True)
                    return
            else:
                await query.message.edit_text(
                    "I'm not connected to any groups!\nCheck /connections or connect to any groups",
                    quote=True
                )
                return

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == "creator") or (str(userid) in ADMINS):    
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("You need to be Group Owner or an Auth User to do that!",show_alert=True)

    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == "creator") or (str(userid) in ADMINS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("Thats not for you!!",show_alert=True)


    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        act = query.data.split(":")[3]
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}:{title}"),
                InlineKeyboardButton("DELETE", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("BACK", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Group Name : **{title}**\nGroup ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode="md"
        )
        return

    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"Connected to **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif "disconnect" in query.data:
        await query.answer()

        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"Disconnected from **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "Successfully deleted connection"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "There are no active connections!! Connect to some groups first.",
            )
            return
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                act = " - ACTIVE" if active else ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Your connected group details ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert,show_alert=True)

    if query.data.startswith("file"):
        ident, fileid, offset = query.data.split("#")
        
        urllink = f'https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/{temp.U_NAME}?start={fileid}_{offset}'
        urllink = url_shortener.tinyurl.short(urllink)
      
        buttons = [[
           InlineKeyboardButton('💠 Verify 💠', url=urllink)
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        k = await client.send_message(
           chat_id=query.from_user.id,
           text='<b>Please verify your identity within 1 Mints.This is Protects the bot from spammers</b>',
           reply_markup=reply_markup,
        )
        #if chat_type in ["group", "supergroup"]:
        await query.answer('I have sent a message to You', show_alert=True)
         
        await asyncio.sleep(60)
        await k.delete()
         
        
#        except UserIsBlocked:
#             await query.answer('You Blocked Me!!. Start Me In privet chat and try Again.',show_alert = True)
#        except PeerIdInvalid:
#             await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
#        except Exception as e:
#             await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
      
#             if AUTH_CHANNEL and not await is_subscribed(client, query):
#                 await query.answer(url=f"https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/{temp.U_NAME}?start={file_id}")
#                 return
#             elif P_TTI_SHOW_OFF:
#                 await query.answer(url=f"https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/{temp.U_NAME}?start={file_id}")
#                 return
#             else:
#                 await client.send_cached_media(
#                     chat_id=query.from_user.id,
#                     file_id=file_id,
#                     caption=f_caption
#                     )
#                 await query.answer('Check My Privet Chat, I have sent files to You')
#         except UserIsBlocked:
#             await query.answer('You Blocked Me!!. Start Me In privet chat and try Again.',show_alert = True)
#         except PeerIdInvalid:
#             await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
#         except Exception as e:
#             await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
            
    elif query.data.startswith("checksub"):
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
            return
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('No such file exist.')
        files = files_[0]
        title = files.file_name
        size=get_size(files.file_size)
        f_caption=files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
            except Exception as e:
                logger.exception(e)
                f_caption=f_caption
        if f_caption is None:
            f_caption = f"{title}"
        await query.answer()
        await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_id,
            caption=f_caption
            )

    elif query.data == "pages":
        await query.answer()
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton('➕ Add Me To Your Groups ➕', url='http://t.me/hb_suzen_bot?startgroup=true')
            ],[
            InlineKeyboardButton('🔍 Search', switch_inline_query_current_chat=''),
            InlineKeyboardButton('🤖 Official Group', url='https://t.me/yourmoviesreq')
            ],[
            InlineKeyboardButton('🛠️Tools', callback_data='help'),
            InlineKeyboardButton('♻️About', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('Manual', callback_data='manuelfilter'),
            InlineKeyboardButton('Auto', callback_data='autofilter')
            ],[
            InlineKeyboardButton('Connection', callback_data='coct'),
            InlineKeyboardButton('Admin', callback_data='admin')
            ],[
            InlineKeyboardButton('《', callback_data='lftp'),
            InlineKeyboardButton('Close', callback_data='cls'),
            InlineKeyboardButton('》', callback_data='rigp')
            ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔮 Status', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "lftp":
        buttons = [[
            InlineKeyboardButton('IMDb', callback_data='imdb'),
            InlineKeyboardButton('Search', callback_data='search')
            ],[
            InlineKeyboardButton('ID', callback_data='id'),
            InlineKeyboardButton('Info', callback_data='info')
            ],[
            InlineKeyboardButton('《', callback_data='rigp'),
            InlineKeyboardButton('Close', callback_data='cls'),
            InlineKeyboardButton('》', callback_data='help')
            ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔮 Status', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
        
     
    elif query.data == "rigp":
        buttons = [[
            InlineKeyboardButton('Batch', callback_data='batch'),
            InlineKeyboardButton('link', callback_data='genlink')
            ],[
            InlineKeyboardButton('Spell Check', callback_data='spell'),
            InlineKeyboardButton('Info', callback_data='info')
            ],[
            InlineKeyboardButton('《', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='cls'),
            InlineKeyboardButton('》', callback_data='lftp')
            ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔮 Status', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
   
   
    elif query.data == "about":
        buttons= [[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔐 Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
   
    elif query.data == "you_720p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='you_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi', callback_data='you_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.YOU_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "cobra_kai_720p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='cobra_kai_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi', callback_data='cobra_kai_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.COBRA_KAI_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_720p":
        buttons= [
           [
              InlineKeyboardButton('Korean', callback_data='AOUAD_K_720p'),
              InlineKeyboardButton('English', callback_data='AOUAD_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi', callback_data='AOUAD_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.AOUAD_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_1080p":
        buttons= [
           [
              InlineKeyboardButton('Korean', callback_data='AOUAD_K_1080p'),
              InlineKeyboardButton('English', callback_data='AOUAD_E_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.AOUAD_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "witcher_720p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='witcher_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi | English', callback_data='witcher_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.WITCHER_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_480p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='vikings_E_480p')
           ],
           [
              InlineKeyboardButton('Hindi | English', callback_data='vikings_H_480p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.VIKINGS_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "vikings_720p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='vikings_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi | English', callback_data='vikings_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.VIKINGS_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "peaky_blinders_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7gUAAlJvKFVTwf35Ilt9aBYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7wUAAlJvKFWIHTDMPTAQ2xYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8AUAAlJvKFXFT8O_3e63IxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8AUAAlJvKFXFT8O_3e63IxYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8QUAAlJvKFX5Rmr1YNkgIhYE'),
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "peaky_blinders_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8gUAAlJvKFWKY2G9xxqwOhYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8wUAAlJvKFXICybxmTaDBxYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD9AUAAlJvKFUdMx3MhM3vIxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD9QUAAlJvKFXIcg3hsCXpWhYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD-AUAAlJvKFUrLkp3Kmuq0xYE'),
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
    elif query.data == "AOUAD_E_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD-wUAAlJvKFU3Qqfj4s2bWxYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_K_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD_QUAAlJvKFW7x_DH9gj2exYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "AOUAD_H_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD_wUAAlJvKFWxdKItMHKiYBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_E_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADDAYAAlJvKFXQG9Z2bLzN4RYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_K_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD6QUAAlJvKFUNHFHk2FA8XxYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "AOUAD_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD6gUAAlJvKFVggBDNv97MVBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "vikings_E_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADEAYAAlJvKFXkfsCjf-JkdRYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADEQYAAlJvKFU4ddhrhq21_RYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADEgYAAlJvKFU3uB0sCzPqtBYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADHAYAAlJvKFVTfWkoGI01XRYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADIAYAAlJvKFX3wYmCTLxddRYE'),
            InlineKeyboardButton('Season 06', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://t.me/HB_Suzan_bot?start=BATCH-BQADBQADIQYAAlJvKFV_fV6TJFId4BYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "cobra_kai_E_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADJQYAAlJvKFUh7LwrgANC8BYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADJgYAAlJvKFUtrBOxYO5B_BYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADJwYAAlJvKFXddCrEO6hKQRYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADKAYAAlJvKFWBYHbXctg4HxYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "cobra_kai_H_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADKQYAAlJvKFVTygmAp_sovhYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADKgYAAlJvKFUcMP3KSmaSkxYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADKwYAAlJvKFX3Q9vzq6prMhYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADLAYAAlJvKFVEMBm1GRC7iBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "cobra_kai_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADLQYAAlJvKFV1Vrd74cjKWhYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADLgYAAlJvKFUGJppz1QW0_RYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADLwYAAlJvKFW-aT1SYsKUWBYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADMAYAAlJvKFVKH9tqDlvoEhYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "cobra_kai_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADMQYAAlJvKFXjvd4YqGzVeBYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADMgYAAlJvKFX_5KI2j7BnCBYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADMwYAAlJvKFW89YwAAfv2DaIWBA'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADNAYAAlJvKFVMdcUmOLAaFBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_E_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7QgAAt67KFV6WKU3vSJjDBYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7QgAAt67KFV6WKU3vSJjDBYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7ggAAt67KFUU3cjRrkE1ohYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7wgAAt67KFVjBiHcodULnBYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8AgAAt67KFXMsIh0KaT02RYE'),
            InlineKeyboardButton('Season 06', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8QgAAt67KFVUUbvIuQABbz4WBA')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8ggAAt67KFV8pow6nF-XQhYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8wgAAt67KFUUukyCEFK-fBYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD9AgAAt67KFWbVOsBDAOK9hYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD9ggAAt67KFVOi-F9AvbbORYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD9wgAAt67KFW3PWz_10vqPhYE'),
            InlineKeyboardButton('Season 06', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD-QgAAt67KFVy3FswcbX7SRYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_H_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD-ggAAt67KFWgZAhAtUN0ghYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD-wgAAt67KFXsg_ZGTd2sghYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD_AgAAt67KFW8oA9SLSHRwxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD_QgAAt67KFUaEgzrhtydWhYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD_ggAAt67KFVE9yXy-Z2-ixYE'),
            InlineKeyboardButton('Season 06', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD_wgAAt67KFXK_48_yxEZJBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_H_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAECQAC3rsoVW2-bm0SgxzbFgQ'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADAQkAAt67KFXRBbeZJbbhhRYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADAgkAAt67KFUR7yG50LJtHxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADAwkAAt67KFVu36YaivLQVxYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADBAkAAt67KFWAONI2aauj9hYE'),
            InlineKeyboardButton('Season 06', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADBQkAAt67KFUq0zkKc726NBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "stranger_things_H":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='stranger_things_H_480p')
           ],
           [
              InlineKeyboardButton('720p', callback_data='stranger_things_H_720p')
           ],
           [
              InlineKeyboardButton('720p', callback_data='stranger_things_H_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.STRANGER_THINGS_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "stranger_things_E":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='stranger_things_E_480p'),
              InlineKeyboardButton('720p', callback_data='stranger_things_E_720p')
           ],
           [
              InlineKeyboardButton('1080p', callback_data='stranger_things_E_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.STRANGER_THINGS_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "you_E_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADBgkAAt67KFXumOH0cLxeMBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADBwkAAt67KFVLoLJ9fM-LthYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADCAkAAt67KFUIWCEkXXUQQhYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "you_1080p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADCQkAAt67KFVuefL2RsIGPBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADCgkAAt67KFXHsiPW8UHZkRYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADCwkAAt67KFWyuHog_hhKRhYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "you_H_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADDAkAAt67KFX8e0WYz035JxYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADDQkAAt67KFUGBHUgAkinYBYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADDgkAAt67KFVWnLrYOS04MhYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "stranger_things_H_480p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADEAkAAt67KFWmKSh28hWHRBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADEQkAAt67KFXtP2QZfCjSuxYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADEgkAAt67KFUv3ubtIHXYrhYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "stranger_things_H_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADEwkAAt67KFVvDOyL-7xjpBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADFAkAAt67KFVG5xBHzIbo5RYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADFQkAAt67KFXbM0-AlcZkaBYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "stranger_things_E_480p":
        buttons= [
           [
              InlineKeyboardButton('S01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADFgkAAt67KFWRc3_W_pulPBYE'),
              InlineKeyboardButton('S02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADFwkAAt67KFXqul78N4rcHxYE')
           ],
           [
              InlineKeyboardButton('S03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADbQUAApxOcFY91eDywt3xMxYE'),
              InlineKeyboardButton('S04 V1-V2', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADeAUAApxOcFZ3iWDo9XR9tRYE')
           ],
           [  
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
    elif query.data == "stranger_things_E_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADGQkAAt67KFX0TcLmsYjG0BYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADGgkAAt67KFV-v9DJVAEF6hYE')
           ],
           [
              InlineKeyboardButton('S03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADdgUAApxOcFbFzAY5y3jW1RYE'),
              InlineKeyboardButton('S04 V1-V2', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADdQUAApxOcFZMcj426amTZBYE')
           ],
           [  
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
         
    elif query.data == "stranger_things_E_1080p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADHAkAAt67KFXuqryQhRmZ5xYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADBQoAAt67KFVpTrLMOkqwaBYE')
           ],
           [
              InlineKeyboardButton('S03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADewUAApxOcFZWtMjR5fW8axYE'),
              InlineKeyboardButton('S04 V1-V2', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADfAUAApxOcFaz8poknYyMJhYE')
           ],
           [  
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "money_heist_E":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='money_heist_E_480p'),
              InlineKeyboardButton('720p', callback_data='money_heist_E_720p')
           ],
           [
              InlineKeyboardButton('1080p', callback_data='money_heist_E_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
         
    elif query.data == "money_heist_E_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADPwkAAt67KFUqhSMjJgf6tBYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADQAkAAt67KFXB9ub4k_mINhYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADQQkAAt67KFXHeqUHuQ8_4hYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADQgkAAt67KFUOhma6La3gARYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADQwkAAt67KFWVCtEe8zO2GhYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADRAkAAt67KFVeirpIm7TNLxYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_E_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADpAUAAt67MFW_RXEUZuqLyRYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADpgUAAt67MFUe8d1bS9sY8hYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADpwUAAt67MFW_OKfBg_mqIxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADqAUAAt67MFVY4ovKyI0P1RYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADqQUAAt67MFXvdxzyB7TEfhYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADqgUAAt67MFU7HdmIU-tlVBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_E_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADqwUAAt67MFUWvPxVx0AtqRYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADrAUAAt67MFU7utBiGx9IPRYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADygUAAt67OFUVi6G-eJy1DBYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADywUAAt67OFW_PZ_NlTsGEhYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADzAUAAt67OFWfRNyrT6djUBYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADzQUAAt67OFWwJZbJyjshCBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_S":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='money_heist_S_480p'),
              InlineKeyboardButton('720p', callback_data='money_heist_E_720p')
           ],
           [
              InlineKeyboardButton('1080p', callback_data='money_heist_E_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_S_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADzgUAAt67OFXHJ7lgVESj4xYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQADzwUAAt67OFW_aC2Xh-Bd6hYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD0QUAAt67OFVPgnANdbQE6RYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD0gUAAt67OFWGE1Qu0zc62xYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_H":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='money_heist_H_480p'),
              InlineKeyboardButton('720p', callback_data='money_heist_H_720p')
           ],
           [
              InlineKeyboardButton('1080p', callback_data='money_heist_H_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_H_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD0wUAAt67OFXtnqNNbdjudhYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD1AUAAt67OFXcs-1NrGqcjxYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD1QUAAt67OFXoejTdM4_UTRYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD1gUAAt67OFWV81QR-VR7MhYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD1wUAAt67OFX_IeFCl7RDjBYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD2AUAAt67OFVPZ8JJDZ7eQxYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_H_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD2QUAAt67OFVZINdl6ZB5_hYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://t.me/HB_Suzan_bot?start=BATCH-BQADBQAD2gUAAt67OFXRLTDQlb3quBYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD2wUAAt67OFUHXZDph2SHwxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD3AUAAt67OFXCLlICs3PqdBYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD3QUAAt67OFXtEf3Ix2GydBYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD3wUAAt67OFXDYuPxdyZ-iBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_H_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD4AUAAt67OFWMlIorcqLDTBYE'),
            InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD4QUAAt67OFWsu4vgMeucbhYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD4gUAAt67OFV8My0V2rFzhhYE'),
            InlineKeyboardButton('Season 04', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD4wUAAt67OFUJkkbk3_lmsxYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD5QUAAt67OFWzsn9mLeBmXRYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD5gUAAt67OFU7C9a6ccDWERYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_Te":
        buttons= [[
            InlineKeyboardButton('720p', callback_data='money_heist_H_720p'),
            InlineKeyboardButton('1080p', callback_data='money_heist_H_1080p')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "money_heist_Ta":
        buttons= [[
            InlineKeyboardButton('720p', callback_data='money_heist_H_720p'),
            InlineKeyboardButton('1080p', callback_data='money_heist_H_1080p')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "Maradona_E":
        buttons= [[
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD5wUAAt67OFVW5tpZLE3uUxYE'),
            InlineKeyboardButton('Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )     
   
    elif query.data == "witcher_480p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD6AUAAt67OFVr3wf0Aq8SOBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD6QUAAt67OFUu7tkJPxzn2BYE')
           ],
           [
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "witcher_E_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD6gUAAt67OFUhrZa4aIFBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7AUAAt67OFUVfcPYEJe6-hYE')
           ],
           [
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "witcher_H_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7QUAAt67OFVZBFWgOJ005xYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD7wUAAt67OFWEbriAZzptqRYE')
           ],
           [
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "witcher_1080p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8QUAAt67OFVUJryIiz_ZsRYE'),
              InlineKeyboardButton('Season 02', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8gUAAt67OFXRuYs8BqU4nxYE')
           ],
           [
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "Maradona_M":
        buttons= [[
            InlineKeyboardButton('Season 01', url='https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/HB_Suzan_bot?start=BATCH-BQADBQAD8wUAAt67OFUnLYdhsveqShYE'),
            InlineKeyboardButton('Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton('Buttons', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='manuelfilter'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "spell":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SPELL_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "id":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ID_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "search":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SEARCH_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "imdb":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.IMDB_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "genlink":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GENLINK_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "batch":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BATCH_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "info":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.INFO_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton('Admin', callback_data='admin')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "stats":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        timeleft = dyno
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.STATUS_TXT.format(total, users, chats, monsize, free, timeleft),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "cls":
        await query.message.delete()
 
async def pm_auto_filter(client, msg, spoll=False):  
    if not spoll:
        message = msg
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
            return
        if not 2 < len(message.text) < 100:
            return
        try:
           search = message.text
           files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)
        except MessageEmpty:
           pass

        if not files:
            if SPELL_CHECK_REPLY:
                return await advantage_spell_chok(msg)
            else:
                return
    else:
        message = msg.message.reply_to_message # msg will be callback query
        search, files, offset, total_results = spoll
    
    fileids = [file.file_id for file in files]
    dbid = fileids[0]
    fileids = "L_I_N_K".join(fileids)
    await add_inst_filter(dbid, fileids)
    if SINGLE_BUTTON:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}┆{get_name(file.file_name)}", url=url_shortener.tinyurl.short(f'https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/{temp.U_NAME}?start={dbid}')
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}",
                    callback_data=f'files#{file.file_id}',
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'files_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if offset != "":
        key = f"{message.chat.id}-{message.message_id}"
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append(
            [
               InlineKeyboardButton(text=f"📃 1/{round(int(total_results)/10)}",callback_data="pages"),  
               InlineKeyboardButton(text="》",callback_data=f"next_{req}_{key}_{offset}")
            ]
        )
        btn.append(
           [InlineKeyboardButton(text="🔰 How To Download 🔰", url="https://t.me/+HGEf8Vy3YW02ODM1")]
        )
         
    else:
        btn.append(
            [
               InlineKeyboardButton(text="📃 1/1",callback_data="pages")
            ]
        )
        btn.append(
           [InlineKeyboardButton(text="💫 Update Channel 💫", url="https://t.me/+75wweakw-EM3OTI9")]
        )
        btn.append(
           [
              InlineKeyboardButton(text="💥 Backup Channel 💥", url="https://t.me/+E6-tbNQW6WszYmY1"),
              InlineKeyboardButton(text="🔞 +18 🔞 ", url="https://t.me/+YV8waQ-u4ywyMDBl")
           ]
        )
    imdb = await get_poster(search, file=(files[0]).file_name) if IMDB else None
    if imdb:
        cap = IMDB_TEMPLATE.format(
            query = search,
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url']
        )

    if imdb and imdb.get('poster'):
        try:
            await message.reply_photo(photo=imdb.get('poster'), caption=cap[:1024], reply_markup=InlineKeyboardMarkup(btn))

        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await message.reply_photo(photo=poster, caption=cap[:1024], reply_markup=InlineKeyboardMarkup(btn))

        except Exception as e:
            logger.exception(e)
            cap = f"Here is what i found for your Request {search}"
            await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    else:
        cap = f"Here is what i found for your Request {search}"
        await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    if spoll:
        await msg.message.delete()


async def auto_filter(client, msg, spoll=False):  
    if not spoll:
        message = msg
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
            return
        if not 2 < len(message.text) < 100:
            return
        try:
           search = message.text
           files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)
        except MessageEmpty:
           pass

        if not files:
            if SPELL_CHECK_REPLY:
                return await advantage_spell_chok(msg)
            else:
                return
    else:
        message = msg.message.reply_to_message # msg will be callback query
        search, files, offset, total_results = spoll

    fileids = [file.file_id for file in files]
    dbid = fileids[0]
    fileids = "L_I_N_K".join(fileids)
    await add_inst_filter(dbid, fileids)
    if SINGLE_BUTTON:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}┆{get_name(file.file_name)}", url=url_shortener.tinyurl.short(f'https://shorturljatt.xyz/st?api=aa45122a191ce482113a565a3c268ddc8f18525b&url=https://telegram.dog/{temp.U_NAME}?start={dbid}')
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}",
                    callback_data=f'files#{file.file_id}',
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'files_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if offset != "":
        key = f"{message.chat.id}-{message.message_id}"
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append(
            [
               InlineKeyboardButton(text=f"📃 1/{round(int(total_results)/10)}",callback_data="pages"),
               InlineKeyboardButton(text="📨", url ='https://t.me/HB_Suzan_bot'),  
               InlineKeyboardButton(text="》",callback_data=f"next_{req}_{key}_{offset}")
            ]
        )
        btn.append( 
        [
            InlineKeyboardButton(text="💫 Update Channel 💫", url="https://t.me/+75wweakw-EM3OTI9")
            ]
        )
        btn.append(
           [
              InlineKeyboardButton(text="💥 Backup Channel 💥", url="https://t.me/+E6-tbNQW6WszYmY1"),
              InlineKeyboardButton(text="🔞 +18 🔞", url="https://t.me/+YV8waQ-u4ywyMDBl")
           ]
        )
        btn.append(
           [InlineKeyboardButton(text="🔰 How To Download 🔰", url="https://t.me/+HGEf8Vy3YW02ODM1")]
        )
         
    else:
        btn.append(
            [
               InlineKeyboardButton(text="📃 1/1",callback_data="pages"),
               InlineKeyboardButton(text="📨", url ='https://t.me/HB_Suzan_bot')
            ]
        )
        btn.append(
            [InlineKeyboardButton(text="💫 Update Channel 💫", url="https://t.me/+75wweakw-EM3OTI9")]
        )
        btn.append(
           [
              InlineKeyboardButton(text="💥 Backup Channel 💥", url="https://t.me/+E6-tbNQW6WszYmY1"),
              InlineKeyboardButton(text="🔞 +18 🔞", url="https://t.me/+YV8waQ-u4ywyMDBl")
           ]
        )
        btn.append(
           [InlineKeyboardButton(text="🔰 How To Download 🔰", url="https://t.me/+HGEf8Vy3YW02ODM1")]
        )
    imdb = await get_poster(search, file=(files[0]).file_name) if IMDB else None
    if imdb:
        cap = IMDB_TEMPLATE.format(
            query = search,
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url']
        )

    if imdb and imdb.get('poster'):
        try:
            await message.reply_photo(photo=imdb.get('poster'), caption=cap[:1024], reply_markup=InlineKeyboardMarkup(btn))

        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await message.reply_photo(photo=poster, caption=cap[:1024], reply_markup=InlineKeyboardMarkup(btn))

        except Exception as e:
            logger.exception(e)
            cap = f"Here is what i found for your Request {search}"
            await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    else:
        cap = f"Here is what i found for your Request {search}"
        await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    if spoll:
        await msg.message.delete()
        

async def advantage_spell_chok(msg):
    query = re.sub(r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|br((o|u)h?)*|^h(e)?(l)*(o)*|mal(ayalam)?|tamil|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|thar(o)*w?|kittum(o)*|aya(k)*(um(o)*)?|full\smovie|any(one)|with\ssubtitle)", "", msg.text, flags=re.IGNORECASE) # plis contribute some common words 
    query = f"{query.strip()} movie"
    g_s = await search_gagala(query)
    g_s += await search_gagala(msg.text)
    gs_parsed = []
    if not g_s:
        k = await msg.reply("I couldn't find any movie in that name.")
        await asyncio.sleep(8)
        await k.delete()
        return
    regex = re.compile(r".*(imdb|wikipedia).*", re.IGNORECASE) # look for imdb / wiki results
    gs = list(filter(regex.match, g_s))
    gs_parsed = [re.sub(r'\b(\-([a-zA-Z-\s])\-\simdb|(\-\s)?imdb|(\-\s)?wikipedia|\(|\)|\-|reviews|full|all|episode(s)?|film|movie|series)', '', i, flags=re.IGNORECASE) for i in gs]
    if not gs_parsed:
        reg = re.compile(r"watch(\s[a-zA-Z0-9_\s\-\(\)]*)*\|.*", re.IGNORECASE) # match something like Watch Niram | Amazon Prime 
        for mv in g_s:
            if match := reg.match(mv):
                gs_parsed.append(match.group(1))
    user = msg.from_user.id if msg.from_user else 0
    movielist = []
    gs_parsed = list(dict.fromkeys(gs_parsed)) # removing duplicates https://stackoverflow.com/a/7961425
    if len(gs_parsed) > 3:
        gs_parsed = gs_parsed[:3]
    if gs_parsed:
        for mov in gs_parsed:
            imdb_s = await get_poster(mov.strip(), bulk=True) # searching each keyword in imdb
            if imdb_s:
                movielist += [movie.get('title') for movie in imdb_s]
    movielist += [(re.sub(r'(\-|\(|\)|_)', '', i, flags=re.IGNORECASE)).strip() for i in gs_parsed]
    movielist = list(dict.fromkeys(movielist)) # removing duplicates
    if not movielist:
        k = await msg.reply("I couldn't find anything related to that. Check your spelling")
        await asyncio.sleep(8)
        await k.delete()
        return
    SPELL_CHECK[msg.message_id] = movielist
    btn = [[
                InlineKeyboardButton(
                    text=movie.strip(),
                    callback_data=f"spolling#{user}#{k}",
                )
            ] for k, movie in enumerate(movielist)]
    btn.append([InlineKeyboardButton(text="Close", callback_data=f'spolling#{user}#close_spellcheck')])
    m = await msg.reply("𝐒𝐄𝐋𝐄𝐂𝐓 𝐘𝐎𝐔𝐑 𝐌𝐎𝐕𝐈𝐄 𝐂𝐋𝐈𝐂𝐊 𝐎𝐍 𝐌𝐎𝐕𝐈𝐄 𝐍𝐀𝐌𝐄  👇👇👇", reply_markup=InlineKeyboardMarkup(btn))
    await asyncio.sleep(10)
    await k.delete()
    return
      
async def manual_filters(client, message, text=False):
    group_id = message.chat.id
    name = text or message.text
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await client.send_message(group_id, reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await client.send_message(
                                group_id, 
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button),
                                reply_to_message_id = reply_id
                            )
                    elif btn == "[]":
                        await client.send_cached_media(
                            group_id,
                            fileid,
                            caption=reply_text or "",
                            reply_to_message_id = reply_id
                        )
                    else:
                        button = eval(btn) 
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button),
                            reply_to_message_id = reply_id
                        )
                except Exception as e:
                    logger.exception(e)
                break
    else:
        return False
