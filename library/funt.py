import library.connect_data as connect_data
import shutil
import library.path as path
import tkinter
import os
import urllib
import glob
from datetime import datetime
import requests


connect = connect_data.getConnection()
cursor = connect.cursor()

def gdl():
    tkinter.messagebox.showinfo("Thông báo","Thành Công. Vui lòng tắt bật lại game")
    shutil.copyfile(path.src_gdl,path.dst_gdl)

def setupgame():
    try:
        tkinter.messagebox.showinfo("Thông báo","Vui lòng đợi")
        os.startfile(path.src_setupGame)
        gdl()
    except:
        pass
    
def xoafile():
    try:
        shutil.rmtree(path.src_deleteGame)

        files = glob.glob(path.src_deleteFile, recursive=True)
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))

        setupgame()
        gdl()
        tkinter.messagebox.showinfo("Thông báo","Thành Công!")
    except:
        tkinter.messagebox.showinfo("Thông báo","Thất bại, vui lòng tắt tab game đang bật rồi thử lại!")

def opengame():
    try:
        os.startfile(path.src_openGame)
    except:
        tkinter.messagebox.showinfo("Thông báo","Thất bại, vui lòng cài lại game rồi thử lại!")

def opentool():
    try:
        os.startfile(path.src_openTool)
    except:
        tkinter.messagebox.showinfo("Thông báo","Thất bại, vui lòng cài lại game rồi thử lại!")

def huongdan():
    os.startfile(path.src_huongdan)

def copyfiledata():
    tkinter.messagebox.showinfo("Thông báo","Thành Công!")
    shutil.copyfile(path.src_filedata,path.dst_filedata)
    save_backup()

def phuchoifile():
    tkinter.messagebox.showinfo("Thông báo","Thành Công!")
    shutil.copyfile(path.dst_filedata,path.src_filedata)

def close():
    exit()

def show_backup():
    with open('.\library\logBackup.txt',encoding="utf-8") as rf:
        content = rf.read()
    tkinter.messagebox.showinfo("Thông báo",content)

def save_backup():
    now = datetime.now()
    _now = now.strftime("%d/%m/%Y %H:%M:%S")
    nd = "Backup cuối cùng vào: " + str(_now)
    with open('.\library\logBackup.txt', "w", encoding="utf-8") as f:
        f.write(nd)
    
def update():
    query = "SELECT * FROM thongbao"
    cursor.execute(query)
    records = cursor.fetchall()

    for record in records:
        if record[1] == "0":
            tkinter.messagebox.showinfo("Thông báo","Không có bản Update")
        elif record[1] == "1":
            answer = tkinter.messagebox.askyesno("Thông báo","Hiện tại đã có phiên bản update, bạn có chắc chắn muốn Update")
            if answer:
                import urllib.request
                import shutil
                
                url = "https://cloudface.vn/dowloads/hotrolangla"

                with urllib.request.urlopen(url) as response, open("hotrolangla.exe", 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)





        