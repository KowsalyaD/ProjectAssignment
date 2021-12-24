from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title('Evalution Wizard')
root.geometry('500x600')
root.configure(bg='white')
root.resizable(False,False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

def show_frame(frame):
    frame.tkraise()

def previous():
    show_frame(firstframe)
def msg():
    messagebox.showwarning("Hey user ", "Your information have been saved Successfully!")
    

firstframe = tk.Frame(root, bg='white')
secondframe = tk.Frame(root,bg='white')
thirdframe = tk.Frame(root, bg='white')
fourthframe = tk.Frame(root, bg='white')

for frame in(firstframe, secondframe, thirdframe, fourthframe):
    frame.grid(row=0,column=0,sticky='nsew')

fname = StringVar()
lname = StringVar()
Id = StringVar()
number = StringVar()
r = IntVar()
t = IntVar()
u = IntVar()
v = IntVar()
w = IntVar()
#---------first screen--------
Label(firstframe, text='Welcome ',font='Cambria  28 ', bg='white',fg='#2B65EC').place(x=180,y=200)
Label(firstframe, text='To ',font='Cambria  28 ', bg='white',fg='#2B65EC').place(x=220,y=250)
Label(firstframe, text='Evalution Wizard ',font='Cambria  28', bg='white', fg='#2B65EC').place(x=120,y=300)

#front = PhotoImage(file='E:\\Python\\codeimg.png')
#front_label = Label(firstframe,image=front)
#front_label.place(x=0,y=0)

login_button = PhotoImage(file='E:\\Python\\login.png')
my_button = Button(firstframe, image=login_button, command=lambda:show_frame(secondframe), borderwidth=0).place(x=180,y=500)

#-----------Second screen------
Label(secondframe, text='Basic Info',font='Cambria 20 ', bg='white',  fg='#2916F5').place(x=20,y=50)

profile_button = PhotoImage(file='E:\\Python\\profile.png')
prof_button = Button(secondframe, image=profile_button,  borderwidth=0).place(x=350,y=50)

#------name-------
fn_text=Label(secondframe,text='First Name ',font='Cambria 12', bg='white',fg='#2916F5')
fn_text.place(x=20,y=100)
fn_entry=Entry(secondframe,width=12,font='Cambria 12 ',textvariable=fname)
fn_entry.place(x=20,y=140)

ln_text=Label(secondframe,text='Last Name ',font='Cambria 12', bg='white', fg='#2916F5')
ln_text.place(x=200,y=100)
ln_entry=Entry(secondframe,width=12,font='Cambria 12 ',textvariable=lname)
ln_entry.place(x=200,y=140)

#------- Id-----
mi_text=Label(secondframe,text='Candidate Id ',font='Cambria 12', bg='white',fg='#2916F5')
mi_text.place(x=20,y=200)
mi_entry=Entry(secondframe,width=12,font='Cambria 12 ',textvariable=Id)
mi_entry.place(x=20,y=240)

#------Contact Num----
ctn_text=Label(secondframe,text='Contact No: ',font='Cambria 12', bg='white',fg='#2916F5')
ctn_text.place(x=20,y=300)
ctn_entry=Entry(secondframe,width=12,font='Cambria 12 ',textvariable=number)
ctn_entry.place(x=20,y=340)


#-----next Page-----
next_button = PhotoImage(file='E:\\Python\\nxt.png')
ne_button = Button(secondframe, image=next_button, command=lambda:show_frame(thirdframe), borderwidth=0).place(x=420,y=500)

pre1_button = PhotoImage(file='E:\\Python\\12.png')
previous1_button = Button(secondframe, image=pre1_button, command=lambda:show_frame(firstframe), borderwidth=0).place(x=20,y=500)

#--------third screen--------
Label(thirdframe, text="Skills ", font='Cambria 20', bg='white', fg='#2916F5').place(x=20,y=50)

Label(thirdframe, text=" Select one of the applicable skills ", font='Cambria 15', bg='white', fg='#2916F5').place(x=20,y=150)

Radiobutton(thirdframe, text=" C ", variable=r, value=1, font='Cambria 12',bg='white', fg='#2916F5').place(x=30,y=200)
Radiobutton(thirdframe, text=" Python ", variable=r, value=2, font='Cambria 12',bg='white',fg='#2916F5').place(x=30,y=250)
Radiobutton(thirdframe, text=" Java ", variable=r, value=3, font='Cambria 12',bg='white',fg='#2916F5').place(x=30,y=300)
Radiobutton(thirdframe, text=" C++ ", variable=r, value=4, font='Cambria 12',bg='white',fg='#2916F5').place(x=30,y=350)

neext_button = PhotoImage(file='E:\\Python\\nxt.png')
nee_button = Button(thirdframe, image=neext_button, command=lambda:show_frame(fourthframe), borderwidth=0).place(x=420,y=500)

pre3_button = PhotoImage(file='E:\\Python\\12.png')
previous3_button = Button(thirdframe, image=pre3_button, command=lambda:show_frame(secondframe), borderwidth=0).place(x=20,y=500)
#---------fourth Screen--------
Label(fourthframe, text="Score ", font='Cambria 20', bg='white',  fg='#2916F5').place(x=20,y=50)

Label(fourthframe, text="Experience ", font='Cambria 14', bg='white',fg='#2916F5').place(x=20,y=120)
Radiobutton(fourthframe, text=" Beginner ", variable=t, value=5, font='Cambria 12',bg='white',fg='#2916F5').place(x=20,y=150)
Radiobutton(fourthframe, text=" Intermediate ", variable=t, value=6, font='Cambria 12',bg='white',fg='#2916F5').place(x=20,y=180)
Radiobutton(fourthframe, text=" Expert ", variable=t, value=7, font='Cambria 12',bg='white',fg='#2916F5').place(x=20,y=210)

Label(fourthframe, text="Design Capabilities ", font='Cambria 14', bg='white',fg='#2916F5').place(x=20,y=300)
Radiobutton(fourthframe, text=" Beginner ", variable=u, value=8, font='Cambria 12',bg='white',fg='#2916F5').place(x=20,y=340)
Radiobutton(fourthframe, text=" Intermediate ", variable=u, value=9, font='Cambria 12',bg='white',fg='#2916F5').place(x=20,y=370)
Radiobutton(fourthframe, text=" Expert ", variable=u, value=10, font='Cambria 12',bg='white',fg='#2916F5').place(x=20,y=400)

Label(fourthframe, text=" Technology Strength ", font='Cambria 14', bg='white',fg='#2916F5').place(x=220,y=120)
Radiobutton(fourthframe, text=" Beginner ", variable=v, value=11, font='Cambria 12',bg='white',fg='#2916F5').place(x=220,y=150)
Radiobutton(fourthframe, text=" Intermediate ", variable=v, value=12, font='Cambria 12',bg='white',fg='#2916F5').place(x=220,y=180)
Radiobutton(fourthframe, text=" Expert ", variable=v, value=13, font='Cambria 12',bg='white',fg='#2916F5').place(x=220,y=210)

Label(fourthframe, text=" Leadership Ability ", font='Cambria 14', bg='white',fg='#2916F5').place(x=220,y=300)
Radiobutton(fourthframe, text=" Beginner ", variable=w, value=14, font='Cambria 12',bg='white',fg='#2916F5').place(x=220,y=340)
Radiobutton(fourthframe, text=" Intermediate ", variable=w, value=15, font='Cambria 12',bg='white',fg='#2916F5').place(x=220,y=370)
Radiobutton(fourthframe, text=" Expert ", variable=w, value=16, font='Cambria 12',bg='white',fg='#2916F5').place(x=220,y=400)

pre2_button = PhotoImage(file='E:\\Python\\12.png')
previous2_button = Button(fourthframe, image=pre2_button, command=lambda:show_frame(thirdframe), borderwidth=0).place(x=20,y=500)

sub_button = PhotoImage(file='E:\\Python\\submit.png')
submit_button = Button(fourthframe, image=sub_button, command=lambda:[show_frame(firstframe),msg()], borderwidth=0).place(x=380,y=500)

show_frame(firstframe)

root.mainloop()
                                                                              
