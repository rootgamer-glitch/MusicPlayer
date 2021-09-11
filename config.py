#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://eu10.fastcast4u.com/clubfmuae")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '969602163')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '6235351'))
    CHAT = int(os.environ.get("CHAT", "-1001251594119"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001500581255")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "GKSRZD-DYNBIF-CGCAKE-ZYWUDK-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "f68fde1378da8f85a243f2ae57f2fcf9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1970049643:AAGWHMdfK0831gl8MB8_-L3Krws2hwIxaK4") 
    SESSION = os.environ.get("SESSION_STRING", "1BQANOTEuMTA4LjU2LjEzMAG7eDcUB54pE6j7RxkJ7Ogc2J39GAyGtY9MfQRB0hwtcHi7N/jK4v1Kg5CfxeZBke5L9V/MrFknbfJhpbqG5Ph8x67vwvkI2MAG/euPRaRt1HYHoVROGTnRV16VP0CASS9g7g7WIz5sWWUoL2kpxEklzuEB3pJl1qeBAvxUqHR6UhyD2MauPsHDIdQEXS7PPvOgCxfqcX+HAKIerCPwZy6b9Er6NYiMmGhUCzpOc81IiYe1oZpboHW87B9QRocP+X8foi8IRas6Z4GwXaTQdlJICu2jZPxlD8MuehaqEXfBeM0cAv5XLgx/yJPxaB7vb11irQqm+CEoJl6Mo1Zl/p9MOg==")
    playlist=[]
    msg = {}
