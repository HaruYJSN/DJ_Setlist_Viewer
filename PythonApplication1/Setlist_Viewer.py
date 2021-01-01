i=1
ii=1
now=1
last=10
hyouji=[[""]*3]*1000
#print(hyouji)
#hyouji[0][0]=""
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
#row=cur.execute("SELECT * FROM items")

#for row in cur:
    #global last
#    last=last+1
#conn.commit()

import tkinter as tk
from tkinter import messagebox

win=tk.Tk()
win.title("セトリ表示")
win.geometry("500x300")


def button2_click():
    global now
    if now==1:
        sethyouji
    else:
        now=now-1
        sethyouji

def button3_click():
    cur.execute("SELECT * FROM items")
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
    #os.system("python .\Setlist_Viewer.py")

def sethyouji():
    global now
    cur.execute("SELECT * FROM items")
    global hyouji
    global i
    global output_order_label
    for row in cur:
    #print(i)
        print(row)
        #print(str(row[0]) + "," + str(row[1]))
        i=i+1
        hyouji[i][0]=row[0]
        hyouji[i][1]=row[1]
        hyouji[i][2]=row[2]
    output_order_label=tk.Label(text="NowPlaying...\n"+str(hyouji[now][2])+","+str(hyouji[now][0]) + "," + str(hyouji[now][1]))
    output_order_label.grid(row=2, column=1, padx=10,)
    #hoge = now
    #cur.execute(
    #   "SELECT * FROM items WHERE bangou ==?", str(now)
    #)
    #fr_list = cur.fetchall()
    #for fr in fr_list:
    #    print(fr)
    ##frame=tk.Frame()
    ##frame.grid(row=1,sticky="we")
    #output_order_label=tk.Label(text="NowPlaying...\n"+str(cur(1)+","+str(cur(2))))
    #output_order_label.grid(row=7, column=1, padx=10,)

def button4_click():
    sethyouji


    

#セトリ表示部
button2 = tk.Button(text="前へ",command=button2_click)
button2.grid(row=1, column=1)
button4 = tk.Button(text="次へ",command=button3_click)
button4.grid(row=1, column=2)
button3 = tk.Button(text="reload",command=button4_click)
button3.grid(row=5,column=3)
#print(str(row[2])+","+str(row[0]) + "," + str(row[1]))
for row in cur:
    print(i)
    print(row)
    print(str(row[0]) + "," + str(row[1]))
    i=i+1
    hyouji[i][0]=row[0]
    hyouji[i][1]=row[1]
    hyouji[i][2]=row[2]

output_order_label=tk.Label(text="NowPlaying...\n"+str(hyouji[i][2])+","+str(hyouji[i][0]) + "," + str(hyouji[i][1]))
output_order_label.grid(row=2, column=1, padx=10,)


win.mainloop()


