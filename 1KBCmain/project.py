from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
#from gtts import gTTS
import time
import os
from pygame import mixer
rootlogin = Tk()
Project_window_width=805
Project__window_height=670
Screen_width=rootlogin.winfo_screenwidth()
Screen_height=rootlogin.winfo_screenheight()
x=(Screen_width/2)-(Project_window_width/2)
y=(Screen_height/2)-(Project__window_height/2)
rootlogin.geometry("%dx%d+%d+%d"%(Project_window_width,Project__window_height,x,y))


mixer.init()

rootlogin.config(bg='dark slate blue')
rootlogin.resizable(width=FALSE,height=FALSE)
rootlogin.title("K.B.L")
rootlogin.iconbitmap(r'kbcicon.ico')


def RulesUI():
 r = Toplevel()
 Questionans__window_width = 570
 Questionans__window_height = 470
 Screen_width = r.winfo_screenwidth()
 Screen_height = r.winfo_screenheight()
 x = (Screen_width / 2) - (Questionans__window_width / 2)
 y = (Screen_height / 2) - (Questionans__window_height / 2)
 r.geometry("%dx%d+%d+%d" % (Questionans__window_width, Questionans__window_height, x, y))
 r.resizable(width=FALSE, height=FALSE)
 mixer.init()
 r.title('RULES')

 frame2 = Frame(r, highlightbackground="black", highlightcolor="black", highlightthickness=1, height=50, width=400,
                bd=0)
 frame2.pack(side=TOP, fill=BOTH)
 l1 = Label(frame2, text='RULES', bg='gold', relief="groove", fg='Black', width=28, font=('Helvetica', 14))
 l1.pack(side=TOP, fill=BOTH)

 frame1 = Frame(r, highlightbackground="black", highlightcolor="black", highlightthickness=1, height=500, width=600,
                bd=0)
 frame1.pack(side=TOP, fill=BOTH)

 t = Text(frame1, bg='black', relief="raised", fg='white', width=50, font=('Helvetica', 14, 'bold italic'))
 t.pack(side=TOP, fill=BOTH)
 t.insert(END,
          'RULE NO 1: THERE ARE 10 QUESTIONS STARTING FROM \n\t1 LAKH AND GOES UPTO 10 LAKHS\n\nRULE NO 2:THERE ARE THREE LIFELINES FOR YOUR HELP\n\n')
 t.insert(END, '\t1.50-50:TWO WRONG OPTIONS WILL BE\n\t ELIMINATED')
 t.insert(END, '\n\n\t2.CHANGE QSNT:CURRENT QUESTION WILL\n\t BE CHANGED')
 t.insert(END, '\n\n\t3.EXPERT ADVICE:EXPERT WILL GUIDE YOU')
 t.insert(END, '\n\nRULE NO 3:THERE IS QUIT OPTION IN CASE YOU ARE NOT \n\tSURE WITH THE ANSWER')
 t.insert(END, '\n\nRULE NO 4:ONCE YOU CROSS 5 LAKH YOU WILL ATLEAST \n\tWIN 5 LAKH')

 t.tag_add("start", "1.0", "1.10")
 t.tag_config("start", background="white", foreground="black")
 t.tag_add("start", "4.0", "4.10")
 t.tag_config("start", background="white", foreground="black")
 t.tag_add("start", "14.0", "14.10")
 t.tag_config("start", background="white", foreground="black")
 t.tag_add("start", "17.0", "17.10")
 t.tag_config("start", background="white", foreground="black")
 r.mainloop()


def ContactUS():
 rm = Toplevel()
 rm.config(bg='purple')
 Questionans__window_width = 600
 Questionans__window_height = 400
 Screen_width = rm.winfo_screenwidth()
 Screen_height = rm.winfo_screenheight()
 x = (Screen_width / 2) - (Questionans__window_width / 2)
 y = (Screen_height / 2) - (Questionans__window_height / 2)
 rm.geometry("%dx%d+%d+%d" % (Questionans__window_width, Questionans__window_height, x, y))
 rm.resizable(width=FALSE, height=FALSE)
 mixer.init()

 img = ImageTk.PhotoImage(Image.open("kbc image.jpg"))
 image = Label(rm, image=img, width=301, height=167)
 image.image = img
 image.place(x=5, y=5)
 rm.title('CONTACT US')
 frame1 = Frame(rm, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=320, height=600,
                bd=0)
 frame1.place_configure(x=0, y=250)
 frame2 = Frame(rm, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=320, height=600,
                bd=0)
 frame2.place_configure(x=0, y=210)
 l1 = Label(frame2, text='CONTACT US', bg='yellow', relief="raised", fg='black', width=20,
            font=('Helvetica', 14))
 l1.pack(side=TOP)
 t = Text(frame1, bg='burlywood1', relief="raised", fg='black', width=100,
          font=('Helvetica', 14))
 t.pack(side=TOP, fill=BOTH)
 t.insert(END, 'JASH VORA-9819557269')
 t.insert(END, '\nANOOJ SARVANKAR-9594162665')
 t.insert(END, '\nDEEPAK YADAV-9082952272')
 t.insert(END, '\nPRATHAMESH SHERKAR-9594028631')
 t.insert(END, '\n\nwww.pythug.com')
 t.tag_add("start", "6.0", "6.40")
 t.tag_config("start", background="DarkSeaGreen1", foreground="black")

 frame3 = Frame(rm, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=100, height=100,
                bd=0)
 frame3.place_configure(x=350, y=50)
 l2 = Label(frame3, text='PLAY TO WIN', bg='yellow3', relief="raised", fg='black', width=20,
            font=('Helvetica', 14))
 l2.pack(side=TOP)

 img = ImageTk.PhotoImage(Image.open("KBCcon.png"))
 image = Label(rm, image=img, width=225, height=55)
 image.image = img
 image.place(x=350, y=100)
 rm.mainloop()


def stop():
 mixer.music.stop()

#def play_music():
#mixer.music.load("KBCstart.mp3")
# while():
#   print("Playing music")

def set_vol(val):
 volume = int(val)/100
 mixer.music.set_volume(volume)


menu1=Menu(rootlogin)
rootlogin.config(menu=menu1)
submenu=Menu(menu1)
menu1.add_cascade(label="Menu", menu=submenu, compound=RIGHT,font=('Tempus Sans ITC', 20))

submenu.add_cascade(label="Rules",activebackground="blue",command=lambda : RulesUI(),font=('Tempus Sans ITC', 14))
submenu.add_separator()
submenu.add_cascade(label="Information",activebackground="blue",font=('Tempus Sans ITC', 14))
submenu.add_separator()
submenu.add_cascade(label="Contact us",activebackground="blue",command=lambda : ContactUS(),font=('Tempus Sans ITC', 14))
submenu.add_separator()
submenu.add_cascade(label="Exit",activebackground="blue",font=('Tempus Sans ITC', 14),command=lambda: exit())
submenu.add_separator()


rootlogin.grid_rowconfigure(1, weight=1)
rootlogin.grid_columnconfigure(0, weight=1)



img = ImageTk.PhotoImage(Image.open("amitabh_bachan.jpg"))
image = Label(rootlogin, image = img,width=405,height=665)
image.image = img
image.place(x=0, y=0)

img = ImageTk.PhotoImage(Image.open("KBC.jpg"))
image = Label(rootlogin, image = img,width=390,height=390)
image.image = img
image.place(x=410, y=0)

# l=Label(rootlogin,text="A. P. Shah Institute of Technology",bg="white",fg="red")
# l.place(x=850,y=10)

l=Label(rootlogin, text='Name:', bg='dark slate blue', fg='White',font=('Tempus Sans ITC', 14))
l.place(x=430,y=445)
fname=Entry(rootlogin, text='', bg='White', fg='black')
fname.place_configure(x=520,y=450)

#l=Label(rootlogin, text='Password:', bg='dark slate blue', fg='White',font=('Tempus Sans ITC', 14))
#l.place(x=410,y=550)
#pas=Entry(rootlogin, text='',bg='White', fg='black')
#pas.place(x=500,y=550)
nametonext=''
def Playbutton():
 global nametonext
 nametonext=fname.get()
 with open('temp.txt','w') as f:
  f.write(nametonext)
 stop()
 rootlogin.destroy()
 os.system('python KBCBeta2.py')

b = Button(rootlogin, text ="Play",width=16,command=lambda: Playbutton())
b.place(x=520,y=510)
b = Button(rootlogin, text ="Quit",width=15,command=lambda: rootlogin.destroy())
b.place(x=420,y=620)

scale= Scale(rootlogin,orient=HORIZONTAL,command=set_vol,bg='dark slate blue',fg='white')
scale.set(50)
scale.place(x=700,y=609)

mixer.music.load("startaudio.mp3")
mixer.music.play()
rootlogin.mainloop()