import random
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from pygame import mixer
from PIL import ImageTk, Image
#Creating GUI
from pygame.event import wait

r = Tk()
Questionans__window_width=570
Questionans__window_height=470
Screen_width=r.winfo_screenwidth()
Screen_height=r.winfo_screenheight()
x=(Screen_width/2)-(Questionans__window_width/2)
y=(Screen_height/2)-(Questionans__window_height/2)
r.geometry("%dx%d+%d+%d"%(Questionans__window_width,Questionans__window_height,x,y))
r.resizable(width=FALSE,height=FALSE)
mixer.init()
r.title('RULES')

frame2 = Frame(r, highlightbackground="black", highlightcolor="black", highlightthickness=1,height=50, width=400,bd=0)
frame2.pack(side=TOP, fill=BOTH)
l1 = Label(frame2, text='RULES', bg='gold', relief="groove", fg='Black', width=28,font=('Helvetica', 14))
l1.pack(side=TOP,fill=BOTH)

frame1 = Frame(r, highlightbackground="black", highlightcolor="black", highlightthickness=1,height=500, width=600,bd=0)
frame1.pack(side=TOP, fill=BOTH)

t = Text(frame1, bg='black', relief="raised", fg='white', width=50,font=('Helvetica', 14,'bold italic'))
t.pack(side=TOP, fill=BOTH)
t.insert(END,'RULE NO 1: THERE ARE 10 QUESTIONS STARTING FROM \n\t1 LAKH AND GOES UPTO 10 LAKHS\n\nRULE NO 2:THERE ARE THREE LIFELINES FOR YOUR HELP\n\n')
t.insert(END,'\t1.50-50:TWO WRONG OPTIONS WILL BE\n\t ELIMINATED')
t.insert(END,'\n\n\t2.CHANGE QSNT:CURRENT QUESTION WILL\n\t BE CHANGED')
t.insert(END,'\n\n\t3.EXPERT ADVICE:EXPERT WILL GUIDE YOU')
t.insert(END,'\n\nRULE NO 3:THERE IS QUIT OPTION IN CASE YOU ARE NOT \n\tSURE WITH THE ANSWER')
t.insert(END,'\n\nRULE NO 4:ONCE YOU CROSS 5 LAKH YOU WILL ATLEAST \n\tWIN 5 LAKH')

t.tag_add("start", "1.0", "1.10")
t.tag_config("start", background="white",foreground="black")
t.tag_add("start", "4.0", "4.10")
t.tag_config("start", background="white", foreground="black")
t.tag_add("start", "14.0", "14.10")
t.tag_config("start", background="white", foreground="black")
t.tag_add("start", "17.0", "17.10")
t.tag_config("start", background="white", foreground="black")
r.mainloop()