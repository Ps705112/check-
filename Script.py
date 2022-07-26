class script(object):
    START_TXT = """𝙷𝚎𝚕𝚕𝚘 {}, 𝙸'𝚊𝚖 <a href='https://t.me/HB_Suzan_bot'>Suzen</a>

𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙰𝚞𝚝𝚘 𝙵𝚒𝚕𝚝𝚎𝚛 + 𝙼𝚘𝚟𝚒𝚎 𝚂𝚎𝚊𝚛𝚌𝚑 + 𝙼𝚊𝚗𝚞𝚊𝚕 𝙵𝚒𝚕𝚝𝚎𝚛 + 𝙵𝚒𝚕𝚎 𝚂𝚝𝚘𝚛𝚎 𝙱𝚘𝚝.  
𝙹𝚞𝚜𝚝 𝙰𝚍𝚍 𝙼𝚎 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙 𝙰𝚗𝚍 𝙴𝚗𝚓𝚘𝚢
"""
    HELP_TXT = """𝙷𝚎𝚢 {}, 
𝚃𝚊𝚔𝚎 𝙰 𝙼𝚒𝚗𝚞𝚝𝚎 𝙰𝚗𝚍 𝚁𝚎𝚊𝚍 𝙲𝚊𝚛𝚎𝚏𝚞𝚕𝚕𝚢"""
    
    
    ABOUT_TXT = """
✯ 𝙼𝚢 𝙽𝚊𝚖𝚎 : <a href='https://t.me/HB_Suzan_bot'>Suzan</a>
✯ 𝙻𝚒𝚋𝚛𝚊𝚛𝚢 : <a href='https://docs.pyrogram.org/'>𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖 v𝟷.𝟸.𝟸𝟶</a>
✯ 𝚂𝚎𝚛𝚟𝚎𝚛 : <a href='https://dashboard.heroku.com/'>𝙷𝚎𝚛𝚘𝚔𝚞</a>
✯ 𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎 : <a href='https://docs.python.org/3/'>𝙿𝚢𝚝𝚑𝚘𝚗 𝟹.𝟿.𝟿</a>
✯ 𝙳𝚊𝚝𝚊𝙱𝚊𝚜𝚎 : <a href='https://mongodb.com/'>𝙼𝚘𝚗𝚐𝚘𝙳𝙱</a>
✯ 𝙱𝚊𝚜𝚎 𝚂𝚘𝚞𝚛𝚌𝚎 𝙲𝚘𝚍𝚎 : <a href='https://github.com/EvamariaTG/EvaMaria'>𝙴𝚟𝚊 𝙼𝚊𝚛𝚒𝚊</a>
✯ Official Group : <a href='https://t.me/yourmoviesreq'>𝙲𝚕𝚒𝚌𝚔 𝙷𝚎𝚛𝚎</a>
✯ 𝙼𝚊𝚒𝚗𝚝𝚎𝚗𝚊𝚗𝚌𝚎 : <a href='https://t.me/HBMoviesGod'>HBMoviesGod</a>
"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and suzy will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bae Suzy supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/HB_Suzan_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    
    
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    
    
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    
    
    SEARCH_TXT = """Help: <b>Search Engine</b>
A Module To Get Info From Google

<b>Commands and Usage:</b>
• /search  - <code>get the film information from various sources.</code>"""
    
    SPELL_TXT = """Help: <b>Check Speeling</b>
A Module To Check Spelling From Google

<b>Usage:</b>
• If you'r searching with wrong speeling, bot will check your spelling and get correct results</code>"""
    
    
    ID_TXT = """Help: <b>Chat/User Id <b>
A Module To Fetch Telegram Chat ID & User ID

<b>Commands and Usage:</b>
• /id  - <code>Use privart for user id and send to group for get chat id.</code>"""
    
    
    IMDB_TXT = """Help: <b>IMDb Info <b>
A Module To Get Movie/Tv Series Info

<b>Commands and Usage:</b>
• /imdb  - <code>get the movie/tv series information from IMDb source.</code>"""
    
    
    INFO_TXT ="""Help: <b>User Info<b>
A Module To Fetch Telegram User Info
   
<b>Commands and Usage:</b>
• /info  - <code>get information about a user.</code>"""
    GENLINK_TXT ="""Help: <b>Batch Link<b>
A Module To Genarte Link To post
   
<b>Commands and Usage:</b>
• /link  - <code>Send As reply</code>"""


    BATCH_TXT ="""Help: <b>Batch Link<b>
A Module To Genarte Link To Batch Files
   
<b>Commands and Usage:</b>
• /batch  - <code>Foewad First And Last Messeages And Get Link</code>
 
<b>NOTE:
• If Your File Sharing Channel is privet Channel, make bae Suzy Admin in That Channel Before Forward"""
    
    
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    
    STATUS_TXT = """
★ 𝚃𝚘𝚝𝚊𝚕 𝙵𝚒𝚕𝚎𝚜: <code>{}</code>
★ 𝙰𝚌𝚝𝚒𝚟𝚎 𝚄𝚜𝚎𝚛𝚜: <code>{}</code>
★ 𝚃𝚘𝚝𝚊𝚕 𝙶𝚛𝚘𝚞𝚙𝚜: <code>{}</code>
★ 𝙳𝚒𝚜𝚔 𝚂𝚝𝚘𝚛𝚊𝚐𝚎: <code>{}</code> 
★ 𝙵𝚛𝚎𝚎 𝚂𝚝𝚘𝚛𝚊𝚐𝚎: <code>{}</code>
★ 𝙷𝚎𝚛𝚘𝚔𝚞 𝚃𝚒𝚖𝚎 𝙻𝚎𝚏𝚝: <code>{}</code> 
"""
    
    LOG_TEXT_G = """#NewGroup #BSB
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    
    LOG_TEXT_P = """#NewUser #BSB
ID - <code>{}</code>
Name - {}
"""
    
    LANG_TEXT = """
○ Title: {}
○ Year: {}
○ Language: {}
○ Season: Season {}
○ Quality: {}
    
Choose the language you want..
"""
    
    QUALITY_TEXT = """
○ Title: {}
○ Year: {}
○ Language: {}
○ Season: Season {}
○ Quality: {}
    
Choose the Quality you want..
"""
    
    RESULT_TXT = """
○ Here Is Result For Your Request
"""
