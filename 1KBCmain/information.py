from tkinter import *
r=Tk()
r.title('INFORMATION')
r.config(bg='yellow')
frame1 = Frame(r, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=320, height=1000,
               bd=0)
frame1.place_configure(x=0, y=200)
l1=Label(frame1,text='PROJECT NAME-KBC',bg='BLUE', relief="groove", fg='WHITE', width=20,
          font=('Tempus Sans ITC', 14))
l1.pack(side=TOP, fill=BOTH)
l2=Label(frame1,text='JASH VORA',bg='BLACK', relief="groove", fg='WHITE', width=20,
          font=('Tempus Sans ITC', 14))
l2.pack(side=TOP,expand='yes',fill=BOTH)
l3=Label(frame1,text='ANOOJ',bg='BLACK', relief="groove", fg='WHITE', width=20,
          font=('Tempus Sans ITC', 14))
l3.pack(side=TOP,expand='yes',fill=BOTH)
l4=Label(frame1,text='DEEPAK',bg='BLACK', relief="groove", fg='WHITE', width=20,
          font=('Tempus Sans ITC', 14))
l4.pack(side=TOP,expand='yes',fill=BOTH)
l5=Label(frame1,text='PRATHAMESH',bg='BLACK', relief="groove", fg='WHITE', width=20,
          font=('Tempus Sans ITC', 14))
l5.pack(side=TOP,expand='yes',fill=BOTH)





r.mainloop()