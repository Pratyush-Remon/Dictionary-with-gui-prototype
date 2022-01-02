from tkinter import *
from tkinter import ttk
from difflib import get_close_matches
import json

root=Tk()

root.title("Dictionary")
root.iconbitmap("Martz90-Circle-Books.ico")
root.config(background='#1D1C1A')
root.geometry('600x400+50+50')

data=json.load(open("C:\\Users\\lenovo pc\\python\\dictionary\\dic.json"))



def translate(w):
    w=w.lower()

    if w in data:
        lable4=Label(root,text=data[w])
        lable4.grid(column=0,row=2)
    elif len(get_close_matches(w,data.keys()))>0:
        root2=Toplevel(root)
        labl1=Label(root2,text=("Do you mean %s instead?[Y/N]"%get_close_matches(w,data.keys())[0]))
        labl1.grid(column=0,row=0)
        res=Entry(root2,width=15,borderwidth=3)
        res.grid(column=3,row=1)
        
        if res.get()=='Y':
            lable2=Label(root2,text=(get_close_matches(w,data.keys())[0]))
            lable2.grid(column=0,row=2)
        elif res.get()=='N':
            lable2=Label(root2,text="Word don't exists in our dictionary")
            lable2.grid(column=0,row=2)
        else:
            lable2=Label(root2,text="We can't understand your response")
            lable2.grid(column=0,row=2)
    else:
       lable3=Label(root,text="Word doesn't exist in our dictionary")
       lable3.grid(column=0,row=2)

e=Entry(root,width=15,borderwidth=3)             #to get input
e.grid(column=3,row=0,padx=6,pady=2)


tran=Button(root,text='Translate',command=lambda : translate(e.get()))
tran.grid(column=3,row=1)



root.mainloop()
