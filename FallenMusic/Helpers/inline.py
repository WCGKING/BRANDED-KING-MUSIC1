# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)
def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    fall = math.floor(percentage)
    if 0 < fall <= 10:
        bar = "✪𝓑𝓡𝓐𝓝𝓓𝓔𝓓 𝓚𝓘𝓝𝓖✪—————————"
    elif 10 < fall < 20:
        bar = "—✪𝓑𝓡𝓐𝓝𝓓𝓔𝓓 𝓦𝓞𝓡𝓛𝓓✪————————"
    elif 20 <= fall < 30:
        bar = "——✪𝓑𝓡𝓐𝓝𝓓𝓡𝓓_𝓑𝓞𝓣✪———————"
    elif 30 <= fall < 40:
        bar = "———✪𝓑𝓡𝓐𝓝𝓓𝓔𝓓 𝓚𝓘𝓝𝓖✪——————"
    elif 40 <= fall < 50:
        bar = "————✪𝓑𝓡𝓐𝓝𝓓𝓔𝓓 𝓦𝓞𝓡𝓛𝓓✪—————"
    elif 50 <= fall < 60:
        bar = "—————✪𝓑𝓡𝓐𝓝𝓓𝓡𝓓_𝓑𝓞𝓣✪————"
    elif 60 <= fall < 70:
        bar = "——————✪𝓑𝓡𝓐𝓝𝓓𝓔𝓓 𝓚𝓘𝓝𝓖✪———"
    

                                 
buttons = InlineKeyboardMarkup(
 [
        [
            InlineKeyboardButton(text="🦋",callback_data=f"ADMIN Resume|{chat_id}",
            InlineKeyboardButton(text="🥰", callback_data=f"ADMIN Pause|{chat_id}",
        ],
        [  
            InlineKeyboardButton(text="❤️", callback_data=f"add_playlist {videoid}",
            InlineKeyboardButton(text="💫", callback_data=f"ADMIN Skip|{chat_id}",
        ],
        [
            InlineKeyboardButton(text="🙈", callback_data=f"ADMIN Stop|{chat_id}",
            InlineKeyboardButton(text="🌹", url=config.SUPPORT_CHANNEL),
        [
            InlineKeyboardButton(text="🕹️ Rᴇsᴜᴍᴇ 🕹️", callback_data="resume_cb"),
            InlineKeyboardButton(text="🕹️ Pᴀᴜsᴇ 🕹️", callback_data="pause_cb"),
        ], 
        [
            InlineKeyboardButton(text="🕹️ Sᴋɪᴘ 🕹️", callback_data="skip_cb"),
            InlineKeyboardButton(text="🕹️ Eɴᴅ 🕹️", callback_data="end_cb"), 
        ], 
        [
            InlineKeyboardButton(text="👑 ʙʀᴀɴᴅᴇᴅ 👑", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="🔥 sᴜᴩᴩᴏʀᴛ 🔥 ", url=config.SUPPORT_CHAT),
        ],
    ]
)

    


pm_buttons = [
    [
        InlineKeyboardButton(
            text="🌹 ᴀᴅᴅ ʏᴏᴜʀ ɢʀᴘ ʀᴀᴅʜᴇ ʀᴀᴅʜᴇ 🥀 ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="🌹ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs🦋", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="🌹 ᴄʜᴀɴɴᴇʟ🦋 ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text=" 🌹 sᴜᴩᴩᴏʀᴛ 🦋", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="🌹 sᴏᴜʀᴄᴇ 🦋", url="https://te.legra.ph/file/3d0d7d23d3a7fb86b442e.jpg"
        ),
        InlineKeyboardButton(text="🌹 ʙʀᴀɴᴅᴇᴅ 🦋 ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="🌹 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🥀",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="🌹 ᴄʜᴀɴɴᴇʟ 🦋 ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text=" 🌹 sᴜᴩᴩᴏʀᴛ 🦋 ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="🌹 sᴏᴜʀᴄᴇ 🦋 ", url="https://te.legra.ph/file/3d0d7d23d3a7fb86b442e.jpg"
        ),
        InlineKeyboardButton(text="🌹 ʙʀᴀɴᴅᴇᴅ 🦋 ", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="ᴇᴠᴇʀʏᴏɴᴇ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="🌹 sᴜᴅᴏ 🦋", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="🌹 ᴏᴡɴᴇʀ 🦋", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="🌹 ʙᴀᴄᴋ 🦋", callback_data="fallen_home"),
        InlineKeyboardButton(text="🌹 ᴄʟᴏsᴇ 🦋", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text=" 🌹 sᴜᴩᴩᴏʀᴛ 🦋 ", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="🌹 ʙᴀᴄᴋ 🦋", callback_data="fallen_help"),
        InlineKeyboardButton(text="🌹 ᴄʟᴏsᴇ 🦋", callback_data="close"),
    ],
]
