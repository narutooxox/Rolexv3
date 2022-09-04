class script(object):
    START_TXT = """𝙃𝙚𝙡𝙡𝙤 {},
𝙈𝙮 𝙉𝙖𝙢𝙚 𝙄𝙨 <a href=https://t.me/{}>{}</a>, 𝙄 𝘾𝙖𝙣 𝙋𝙧𝙤𝙫𝙞𝙙𝙚 𝙈𝙤𝙫𝙞𝙚𝙨 𝙏𝙤 𝙔𝙤𝙪𝙧 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 𝘼𝙡𝙨𝙤, 𝙈𝙖𝙠𝙚 𝙈𝙚 𝘼𝙨 𝘼𝙙𝙢𝙞𝙣 𝙄𝙣 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 𝙩𝙤 𝙎𝙚𝙧𝙫𝙚 𝙈𝙤𝙫𝙞𝙚𝙨 𝘿𝙤𝙣𝙚 😁👍🏻"""
    HELP_TXT = """𝙃𝙚𝙮 {}
𝙃𝙚𝙧𝙚 𝙄𝙨 𝙏𝙝𝙚 𝙃𝙚𝙡𝙥 𝙁𝙤𝙧 𝙈𝙮 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨."""
    ABOUT_TXT = """» 𝙈𝙮 𝙉𝙖𝙢𝙚: {}
» 𝘾𝙧𝙚𝙖𝙩𝙤𝙧: <a href=https://t.me/RolexMoviesOX>𝙍𝙤𝙡𝙚𝙭 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮</a>
» 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚: 𝙋𝙔𝙏𝙃𝙊𝙉 
» 𝘿𝙖𝙩𝙖 𝘽𝙖𝙨𝙚: 𝙈𝙊𝙉𝙂𝙊 𝘿𝘽
» 𝘽𝙤𝙩 𝙎𝙚𝙧𝙫𝙚𝙧: 𝙃𝙀𝙍𝙊𝙆𝙐"""
    SOURCE_TXT = """<b>Details:</b>
    
- Anybody Wants This Bot Contact Me @RolexContact_bot"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

<b>Commands:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

<b>Button Commands:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>Details:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
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
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>Commands</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
