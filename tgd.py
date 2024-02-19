from pyrogram import Client
from os.path import exists
from os import remove
from sys import stdout, exit
import array as arr
import os
from pyrogram.errors import FloodWait
import time
from pyrogram.file_id import FileId, FileType, PHOTO_TYPES



configfile = "tgd.txt"

if not exists(configfile):
    api_id = input("\nAPI ID: ")
    api_hash = input("API HASH: ") 
    check = input("Do you have String Session? (y/n): ")
    if check.lower() == "y":
        ss = input("SESSION STRING: ")
    else:
        print()
        with Client("TGD", api_id=api_id, api_hash=api_hash, in_memory=True) as temp:
            ss = temp.export_session_string()
        print()
    with open(configfile,"w") as file:
        file.write(api_id + "\n" + api_hash + "\n" + ss)
else:
    with open(configfile, "r") as file:
        data = file.readlines()
    try:
        api_id, api_hash, ss = data
    except:
        remove(configfile)
        print("Retry...")
        exit(0)
        

acc = Client("myacc" ,api_id=api_id, api_hash=api_hash, session_string=ss)
try:
    with acc:
        me = acc.get_me()
        print("\nLogged in as:", me.id)
except:
    remove(configfile)
    print("\nMaybe Wrong Crenditals...")
    exit(0)
    
    
def progress(current, total, length=50):
    progress_percent = current * 100 / total
    completed = int(length * current / total)
    bar = f"[{'#' * completed}{' ' * (length - completed)}] {progress_percent:.1f}%"
    stdout.write(f"\r{bar}")
    stdout.flush()


print("""
Examples:

    https://t.me/xxxx/1423
    https://t.me/c/xxxx/10
    https://t.me/xxxx/1001-1010
    https://t.me/c/xxxx/101 - 120\n\n""")

#link = input("Enter the link: ")
#https://t.me/c/2131480022/2135
link = "https://t.me/c/2139677102/1051-1066"


print()


if link.startswith("https://t.me/"):
    datas = link.split("/")
    temp = datas[-1].replace("?single","").split("-")
    fromID = int(temp[0].strip())
    try: toID = int(temp[1].strip())
    except: toID = fromID

    if link.startswith("https://t.me/c/"):
        chatid = int("-100" + datas[4])
    else:
        chatid = datas[3]

else:
    print("Not a Telegram Link")
    exit(0)


#custo = arr.array('i', [1736,1737,1738,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1756,1757,1758,1759,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773])


with acc:
    total = toID+1 - fromID
    for msgid in range(fromID, toID+1):
    #for element in custo:
        #msgid=element
        msg = acc.get_messages(chatid, msgid)
        saki = acc.get_messages(chatid, msgid)
        print("Downloding:", msgid, f"({(msgid - fromID + 1)}/{total})")
        try:
            file = acc.download_media(msg, progress=progress)
            print("\nSaved at", file, "\n")
            time.sleep(1)
            if file.endswith(".jpg"):                     
                acc.send_photo("inc333333",r"{}".format(file),progress=progress)
            
            #elif file in (FileType.VIDEO, FileType.ANIMATION, FileType.VIDEO_NOTE):
            elif file.endswith((".mp4")):    
                 acc.send_video("inc333333",r"{}".format(file),progress=progress)
                 time.sleep(1)
            os.remove(r"{}".format(file))     
            #     print("uploading")
            #else:
            #    print("oombi")            
            
            
        except ValueError as e:
            print(e, "\n")
           
            
            
input("Press enter to exit...")
