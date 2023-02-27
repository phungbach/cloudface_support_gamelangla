import tkinter
import tkinter.messagebox
from tkinter import *
import library.funt as funt
from tkinter.scrolledtext import ScrolledText


def main():
    #Giao dien
    giaodien = tkinter.Tk()
    giaodien.title("Hỗ Trợ Game Làng Lá")
    giaodien.geometry('309x200')
    
    button3 = tkinter.Button(giaodien,text="Mở game",fg="black",width="20",bg="white",command=funt.opengame)
    button3.grid(column=1,row=1,padx=2,pady=1)

    button4 = tkinter.Button(giaodien,text="Mở Tool Nar",fg="black",width="20",bg="white",command=funt.opentool)
    button4.grid(column=1,row=2,padx=2,pady=1)

    button6 = tkinter.Button(giaodien,text="Copy File data",fg="black",width="20",bg="white",command=funt.copyfiledata)
    button6.grid(column=1,row=3,padx=2,pady=1)

    button7 = tkinter.Button(giaodien,text="Phục hồi File data",fg="black",width="20",bg="white",command=funt.phuchoifile)
    button7.grid(column=1,row=4,padx=2,pady=1)

    button9 = tkinter.Button(giaodien,text="Kiểm tra Backup",fg="black",width="20",bg="white",command=funt.show_backup)
    button9.grid(column=1,row=5,padx=2,pady=1)


    button2 = tkinter.Button(giaodien,text="Cài game",fg="black",bg="white",width="20",command=funt.setupgame)
    button2.grid(column=2,row=1,padx=2,pady=1)

    button = tkinter.Button(giaodien,text="Giảm Dung Lượng",fg="black",width="20",bg="white",command=funt.gdl)
    button.grid(column=2,row=2,padx=2,pady=1)

    button1 = tkinter.Button(giaodien,text="Fix lỗi(tùm lum)",fg="black",width="20",bg="white",command=funt.xoafile)
    button1.grid(column=2,row=3,padx=2,pady=1)

    button9 = tkinter.Button(giaodien,text="Update",fg="black",width="20",bg="white",command=funt.update)
    button9.grid(column=2,row=4,padx=2,pady=1)

    button5 = tkinter.Button(giaodien,text="Hướng dẫn sử dụng",fg="black",width="20",bg="white",command=funt.huongdan)
    button5.grid(column=2,row=5,padx=2,pady=1)

    button8 = tkinter.Button(giaodien,text="Thoát",fg="black",width="20",bg="white",command=funt.close)
    button8.grid(column=1,columnspan=2,row=6,padx=2,pady=1)

    label7 = tkinter.Label(giaodien,text="@cloudface Version 1",fg="white",bg="black",width=43,pady=7)
    label7.grid(column=1,columnspan=2,row=7,sticky='e')

    giaodien.resizable(False,False)
    giaodien.mainloop()

main()

