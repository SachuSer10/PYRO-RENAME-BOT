"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>ʜᴇʟʟᴏ {} 👋,
    📝This is a Telegram Rename Bot by @NSKBOTS ❤️
    
    📝Please send me any File, I can Rename It As Per Your choices to telegram as File/VideoVideo
                  
      ➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️<b>"""

    ABOUT_TXT = """<b>
      🤖 My Name : {} 
      📕 Library: <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
      ㊙ Language: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
      💾 Database: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
      📊 Version: <a href=ʀᴇɴᴀᴍᴇʀ V3.0.0
      🚸 Powered By: <a href= @NSKBOTS</a></b>"""
 
 






    HELP_TXT = """
    <b>AVAILABLE COMMANDS✅️
    
    👉/start :Check Bot Alive Or Not 🤖
    👉/view_thumb :Check Your Thumbnail📸
    👉/del_thumb  :Delete Your Thumbnail💔
    👉/set_caption  :Set Your Custom Caption
    👉/see_caption  :See Your Caption
    👉/del_caption  :Delete Your Caption</b>"""
    


    
               







  
  
  
  
 
 


     

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """
» </a> """

    PROGRESS_BAR = """<b>\n
╭━━━━[🔅𝗡𝗦𝗞 𝗥𝗘𝗡𝗔𝗠𝗘𝗥🔅]━⍟➣
┣ 🗃️ Size: {1} | {2}
┣ ⚡ Done : {0}%
┣ 🚀 Speed: {3}/s
┣ ⏱️ Eta: {4}
╰━━━━━━━━━━━━━━━━━━━━━⍟➣ </b>"""




