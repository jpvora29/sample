from tkinter import*
from tkinter import messagebox
Formfill = Tk()
EnterDetails__window_width=400
EnterDetails__window_height=400
Screen_width=Formfill.winfo_screenwidth()
Screen_height=Formfill.winfo_screenheight()
x=(Screen_width/2)-(EnterDetails__window_width/2)
y=(Screen_height/2)-(EnterDetails__window_height/2)
Formfill.geometry("%dx%d+%d+%d"%(EnterDetails__window_width,EnterDetails__window_height,x,y))

Formfill.resizable(width=FALSE,height=FALSE)
Formfill.config(bg='RoyalBlue1')

def submit():

    if tandc.get()==0:
        messagebox.showerror("T&c","Please Select T&c")
    else:
        messagebox.askokcancel("Submiting","Submit Your Details")
        file=open('details.txt','a')
        file.write(fname.get()+","+lname.get()+","+age.get()+","+gender.get()+","+email.get()+","+number.get()+","+Pasword.get()+"\n")
        file.close()
        quit()



l=Label(Formfill, text='Enter a first name', bg='RoyalBlue1', fg='White',font=('Tempus Sans ITC', 14))
l.place(x=40,y=40)
fname=Entry(Formfill, text='', bg='White', fg='black')
fname.place(x=200,y=40)

l=Label(Formfill, text='Enter a last name', bg='RoyalBlue1', fg='White',font=('Tempus Sans ITC', 14))
l.place(x=40,y=80)
lname=Entry(Formfill, text='',bg='White', fg='black')
lname.place(x=200,y=80)

l=Label(Formfill, text='Age', bg='RoyalBlue1', fg='White',font=('Tempus Sans ITC', 14))
l.place(x=40,y=120)
age=Entry(Formfill, text='', bg='White', fg='black')
age.place(x=200,y=120)

gender = StringVar()
l=Label(Formfill, text='Gender', bg='RoyalBlue1', fg='White',font=('Tempus Sans ITC', 14))
l.place(x=40,y=160)
r1=Radiobutton(Formfill, text='Male', bg='RoyalBlue1', fg='black',variable=gender,value='male',font=('Tempus Sans ITC', 14))
r1.place(x=190,y=160)
r2=Radiobutton(Formfill, text='Female', bg='RoyalBlue1', fg='black',variable=gender,value='female',font=('Tempus Sans ITC', 14))
r2.place(x=290,y=160)

l=Label(Formfill, text='Email ID', bg='RoyalBlue1', fg='white',font=('Tempus Sans ITC', 14))
l.place(x=40,y=200)
email=Entry(Formfill, text='', bg='White', fg='black')
email.place(x=200,y=200)

l=Label(Formfill, text='Mobile No.', bg='RoyalBlue1', fg='white',font=('Tempus Sans ITC', 14))
l.place(x=40,y=240)
number=Entry(Formfill, text='', bg='White', fg='black')
number.place(x=200,y=240)

l=Label(Formfill, text='Password', bg='RoyalBlue1', fg='white',font=('Tempus Sans ITC', 14))
l.place(x=40,y=280)
Pasword=Entry(Formfill, text='', bg='White', fg='black')
Pasword.place(x=200,y=280)



tandc=IntVar()


r3=Checkbutton(Formfill, text='T&C', bg='RoyalBlue1', fg='black',variable=tandc,onvalue=1,font=('Tempus Sans ITC', 14))
r3.place(x=40,y=340)


b = Button(Formfill, text ="SUBMIT",bg='White', fg='red',command =submit,font=('Tempus Sans ITC', 14))
b.place(x=300,y=350)



Formfill.mainloop()