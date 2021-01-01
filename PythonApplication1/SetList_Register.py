i=1
now=1
last=10
import os
import sqlite3
filepath="test.sqlite"
conn=sqlite3.connect(filepath)
cur = conn.cursor()
#cur.execute("DROP TABLE IF EXISTS items")

#cur.execute("""CREATE TABLE items(
#    songname NONE,
#    artistname NONE,
#    bangou INTEGER
#)""")
conn.commit()

import tkinter as tk
from tkinter import messagebox

def sethyouji():
    global now
    #hoge = now
    #cur.execute(
    #   "SELECT * FROM items WHERE bangou ==?", str(now)
    #)
    #fr_list = cur.fetchall()
    #for fr in fr_list:
    #    print(fr)
    ##frame=tk.Frame()
    ##frame.grid(row=1,sticky="we")
    cur.execute("SELECT * FROM items")
    for row in range(1,cur):
        global last
        last=last+1
    output_order_label=tk.Label(text="NowPlaying...\n"+str(cur(1)+","+str(cur(2))))
    output_order_label.grid(row=7, column=1, padx=10,)


def button_click():
    touroku=0
    input_song_value = input_songname.get()
    input_artist_value=input_artistname.get()
    input_order_value=input_order.get()
    if str.isdecimal(input_order_value)==False:
        messagebox.showerror("エラー","数値を入力してください")
    else:
        cur.execute("SELECT * FROM items")
        print(cur)
        for row in cur:
            print(str(row[2])+","+str(row[0]) + "," + str(row[1]))
            numb=int(row[2])
            print("登録ナンバー"+str(numb))
            print(input_order_value)
            if numb==int(input_order_value):
                messagebox.showerror("エラー","曲順が重複しています")
                touroku=0
                print("error")
                break
            else:
                touroku=1
        #touroku=1
        if touroku==1:
            show_message="登録しました\n"+input_order_value+"曲目:"+input_song_value+"\nアーティスト名:"+input_artist_value
            cur.execute('INSERT INTO items (bangou , songname , artistname) VALUES (?,?,?)',(input_order_value , input_song_value, input_artist_value ))
            conn.commit()
            print(show_message)
            messagebox.showinfo("入力内容",show_message)


def button1_click():
    cur.execute("SELECT bangou, songname, artistname FROM items")
   # cur.execute("SELECT bangou FROM items")
    items_list = cur.fetchall()
    print(items_list)
    messagebox.showinfo("DB内容表示",items_list)

def button2_click():
    global now
    if now==1:
        sethyouji
    else:
        now=now-1
        sethyouji

def button3_click():
    last=1
    global now
    for row in cur:
        last=last+1
    if now==last:
        sethyouji
    else:
        now=now+1
        sethyouji

def button4_click():
    global now
    os.system("python .\Setlist_Viewer.py")
    

def button5_click():
    cur.execute("DROP TABLE IF EXISTS items")
    cur.execute("""CREATE TABLE items(
    songname NONE,
    artistname NONE,
    bangou INTEGER
)""")
    cur.execute('INSERT INTO items (bangou , songname , artistname) VALUES (?,?,?)',(0 , 0, 0 ))
    messagebox.showinfo("完了","削除しました")

#frame_button=tk.Frame()
#frame_button.grid(row=1,sticky="we")

win=tk.Tk()
win.title("セトリ登録")
win.geometry("500x300")
input_order_label=tk.Label(text="順番")
input_order_label.grid(row=1, column=1, padx=10,)
input_order=tk.Entry(width=5)
input_order.grid(row=1,column=2)

input_songname_label=tk.Label(text="曲名")
input_songname_label.grid(row=2, column=1, padx=10,)
input_songname=tk.Entry(width=40)
input_songname.grid(row=2,column=2)

input_artistname_label=tk.Label(text="アーティスト名")
input_artistname_label.grid(row=3, column=1, padx=10,)
input_artistname=tk.Entry(width=40)
input_artistname.grid(row=3,column=2)

button = tk.Button(text="登録!",command=button_click)
button.grid(row=4, column=1)

button1 = tk.Button(text="DB内容表示",command=button1_click)
button1.grid(row=4, column=2)
button5 = tk.Button(text="DB内容全削除",command=button5_click)
button5.grid(row=4,column=3)

list_value=tk.StringVar()
items_list = cur.fetchall()
print(items_list)
list_value.set(items_list)
listbox=tk.Listbox(y=130,height=8,listvariable=list_value,selectmode="single")
#listbox.pack()

#セトリ表示部
button2 = tk.Button(text="前へ",command=button2_click)
button2.grid(row=5, column=1)
button4 = tk.Button(text="次へ",command=button3_click)
button4.grid(row=5, column=2)
button3 = tk.Button(text="なうぷれ表示",command=button4_click)
button3.grid(row=5,column=3)





win.mainloop()

