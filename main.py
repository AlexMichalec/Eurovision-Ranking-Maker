from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import countries as c
import random
import datetime

def keydown():
    counter = 2
    def inner(e):
        nonlocal counter
        match e.char:
            case '1':
                countries_list[counter-2][3] += 5
                countries_list[counter-1][3] += 0
            case '2':
                countries_list[counter - 2][3] += 3
                countries_list[counter - 1][3] += 1
            case '3':
                countries_list[counter - 2][3] += 1
                countries_list[counter - 1][3] += 1
            case '4':
                countries_list[counter - 2][3] += 1
                countries_list[counter - 1][3] += 3
            case '5':
                countries_list[counter - 2][3] += 0
                countries_list[counter - 1][3] += 5
            case _:
                return 0
        if counter == 0:
            countries_list.sort(key=(lambda a:a[3]),reverse=True)
        c1 = countries_list[counter]
        c2 = countries_list[counter+1]
        labCountry1['text'] = c1[0]
        labCountry2['text'] = c2[0]
        labArtist1['text'] = c1[1]
        labArtist2['text'] = c2[1]
        labSong1['text'] = c1[2]
        labSong2['text'] = c2[2]
        counter+=2
        if counter >= len(countries_list):
            counter=0
    return inner

def up (x):
    def inner():
        countries_list[x-1],countries_list[x]=countries_list[x],countries_list[x-1]
        countries_list[x - 1][3], countries_list[x][3] = countries_list[x][3], countries_list[x - 1][3]
        show_results()
    return inner

def down (x):
    def inner():
        countries_list[x+1],countries_list[x]=countries_list[x],countries_list[x+1]
        countries_list[x + 1][3], countries_list[x][3] = countries_list[x][3], countries_list[x + 1][3]
        show_results()
    return inner

def save(text):
    def inner():
        filename = filedialog.asksaveasfilename(filetypes=[("Plik tekstowy","*.txt")], defaultextension = "*.txt") # wywołanie okna dialogowego save file
        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(text)
    return inner

def show_results():
    countries_list.sort(key=(lambda a: a[3]), reverse=True)
    c1 = countries_list[0]
    c2 = countries_list[1]
    labCountry1['text'] = c1[0]
    labCountry2['text'] = c2[0]
    labArtist1['text'] = c1[1]
    labArtist2['text'] = c2[1]
    labSong1['text'] = c1[2]
    labSong2['text'] = c2[2]

    text= str(datetime.date.today()) + "\nMy Eurovision Ranking\n"
    for widget in frame4.winfo_children():
        widget.destroy()

    labYour = Label(text="Your List: ", font=("Calibri", 16), master=frame4)
    labYour.grid(column=5,row=0)
    for i,c in enumerate(countries_list):
        lab = Label(text=str(i+1)+". %s"%c[0],font=("Calibri",12),master=frame4)
        text+=str(i+1)+". %s"%c[0]+"\n"
        if i!=0:
            butUp = Button(text=" ▲",foreground='green',master=frame4,borderwidth=0,command=up(i))
            butUp.grid(column=3*(i//10),row=1+i%10,pady=0,sticky='e')
        if i!=len(countries_list)-1:
            butUp = Button(text="▼",foreground='red',master=frame4,borderwidth=0,command=down(i))
            butUp.grid(column=3*(i//10)+1,row=1+i%10,pady=0,sticky='w')
        lab.grid(column=3*(i//10)+2,row=1+i%10,pady=0,sticky='w')


    frame4['pady']=10
    frame4.grid(column=1, row=1, pady=10, rowspan=3,padx=50)
    for w in frame6.winfo_children():
        w.destroy()
    butSave = Button(master=frame6, text="SAVE IT!", font=('calibri', 16), padx=10,
                     background="midnight blue", foreground='white', borderwidth=4, command=save(text))
    butSave.pack()
    for w in frame5.winfo_children():
        w.destroy()
    labTitle = Label(master=frame5, text="You can now adjust positions of songs manually:", font=("Calibri", 18), background=BG_COL)
    labTitle.pack()


keydown=keydown()
countries_list = c.LIST
random.shuffle(countries_list)
for i,c in enumerate(countries_list):
    c[3]+=i/100
BG_COL = "light blue"
root = Tk()
root.title("Create your own Eurovision ranking ^^")
root.configure(background=BG_COL)

frame0 = Frame(root,background=BG_COL)
imgEuro = Image.open("logo.png")
imgEuro = imgEuro.resize((400,200))
imgEuro = ImageTk.PhotoImage(imgEuro)
labImg = Label(image=imgEuro,master=frame0,background=BG_COL)
labImg.pack()

frame = Frame(root,background=BG_COL)

labCountry1 = Label(master=frame,text=countries_list[0][0],font=("Calibri",22),width=17,background=BG_COL)
labCountry2 = Label(master=frame,text=countries_list[1][0],font=("Calibri",22),width=17,background=BG_COL)
labArtist1 = Label(master=frame,text=countries_list[0][1],font=("Calibri",10),width=30,background=BG_COL)
labArtist2 = Label(master=frame,text=countries_list[1][1],font=("Calibri",10),width=30,background=BG_COL)
labSong1 = Label(master=frame,text=countries_list[0][2],font=("Calibri",14),width=25,background=BG_COL)
labSong2 = Label(master=frame,text=countries_list[1][2],font=("Calibri",14),width=25,background=BG_COL)
labVS = Label(master=frame,text="VS",font=("Calibri",14),background=BG_COL)

labCountry1.grid(column=0,row=0)
labCountry2.grid(column=2,row=0)
labArtist1.grid(column=0,row=1)
labArtist2.grid(column=2,row=1)
labSong1.grid(column=0,row=2)
labSong2.grid(column=2,row=2)
labVS.grid(column=1,row=1)

frame2 = Frame(master=root,background=BG_COL)
lab21 = Label(master=frame2,text="Choose which one do you like more:",font=("Calibri",15),background=BG_COL)
labc0 = Label(master=frame2,text="Press:",font=("Calibri",16),background=BG_COL)
labc1 = Label(master=frame2,text="↖1↖",font=("Calibri",16),background=BG_COL)
labc2 = Label(master=frame2,text="↖2",font=("Calibri",16),background=BG_COL)
labc3 = Label(master=frame2,text="?3?",font=("Calibri",16),background=BG_COL)
labc4 = Label(master=frame2,text="4↗",font=("Calibri",16),background=BG_COL)
labc5 = Label(master=frame2,text="↗5↗",font=("Calibri",16),background=BG_COL)
labc6 = Label(master=frame2,text=" ",font=("Calibri",16),background=BG_COL)

lab21.pack()
labc0.pack(side='left',padx=4)
labc1.pack(side='left',padx=16)
labc2.pack(side='left',padx=16)
labc3.pack(side='left',padx=16)
labc4.pack(side='left',padx=16)
labc5.pack(side='left',padx=16)
labc6.pack(side='left',padx=20)


frame3 = Frame(root,background=BG_COL)

butTest = Button(master=frame3,text="SHOW RESULTS",font=('calibri',16),command=show_results,padx=10,
                 background="midnight blue",foreground='white',borderwidth=4)
butTest.pack()

frame4 = Frame(root,relief="solid",borderwidth=2,padx=10,pady=10)

frame5 = Frame(root,background=BG_COL)
frame6 = Frame(root,background=BG_COL)


frame0.grid(column=0,row=0,rowspan=2,pady=10)
frame.bind("<KeyPress>", keydown)
frame.grid(column=0,row=2,pady=10)
frame2.grid(column=0,row=3,pady=10)
frame3.grid(column=0,row=4,pady=10)
frame5.grid(column=1,row=0,pady=10,sticky='s')
frame4.grid(column=1,row=1,pady=10,rowspan=3)
frame6.grid(column=1,row=4,pady=10)

frame.focus_set()
root.mainloop()