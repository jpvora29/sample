import random
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from pygame import mixer
from PIL import ImageTk, Image
#Creating GUI
from pygame.event import wait

rm = Tk()
rm.config(bg='purple')
Questionans__window_width=600
Questionans__window_height=400
Screen_width=rm.winfo_screenwidth()
Screen_height=rm.winfo_screenheight()
x=(Screen_width/2)-(Questionans__window_width/2)
y=(Screen_height/2)-(Questionans__window_height/2)
rm.geometry("%dx%d+%d+%d"%(Questionans__window_width,Questionans__window_height,x,y))
rm.resizable(width=FALSE,height=FALSE)
mixer.init()

img = ImageTk.PhotoImage(Image.open("kbc image.jpg"))
image = Label(rm, image=img, width=301, height=167)
image.image = img
image.place(x=5, y=5)
rm.title('CONTACT US')
frame1 = Frame(rm, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=320, height=600,bd=0)
frame1.place_configure(x=0, y=250)
frame2 = Frame(rm, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=320, height=600, bd=0)
frame2.place_configure(x=0, y=210)
l1 = Label(frame2, text='CONTACT US', bg='red', relief="raised", fg='white', width=20,
          font=('Helvetica', 14))
l1.pack(side=TOP)
t = Text(frame1, bg='burlywood1', relief="raised", fg='black', width=100,
          font=('Helvetica', 14))
t.pack(side=TOP, fill=BOTH)
t.insert(END,'JASH VORA-9819557269')
t.insert(END,'\nANOOJ SARVANKAR-9594162665')
t.insert(END,'\nDEEPAK YADAV-9082952272')
t.insert(END,'\nPRATHAMESH SHERKAR-9594028631')
t.insert(END,'\n\nwww.pythug.com')
t.tag_add("start", "6.0", "6.40")
t.tag_config("start", background="DarkSeaGreen1",foreground="black")

frame3 = Frame(rm, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=100, height=100,bd=0)
frame3.place_configure(x=350, y=50)
l2 = Label(frame3, text='PLAY TO WIN', bg='turquoise3', relief="raised", fg='black', width=20,
          font=('Helvetica', 14))
l2.pack(side=TOP)

img = ImageTk.PhotoImage(Image.open("KBCcon.png"))
image = Label(rm, image=img, width=225, height=55)
image.image = img
image.place(x=350, y=100)
rm.mainloop()
