from tkinter import *
from tkinter import ttk                                #not using it, i guess but let it be
from difflib import get_close_matches
import json

root=Tk()

root.title("Dictionary")
root.iconbitmap("path\\Martz90-Circle-Books.ico")
root.config(background='#1D1C1A')
root.geometry('600x400+50+50')

data=json.load(open("path\\dic.json"))




def translate(w):
    w=w.lower()

    if w in data:
        lable4=Label(root,text=data[w])
        lable4.grid(column=0,row=2)
    elif len(get_close_matches(w,data.keys()))>0:                                 #condition if the word is misspelt 
        root2=Toplevel(root)                                                      #second window
        root2.config(background='#404040')
        root2.iconbitmap("path\\Martz90-Circle-Books.ico")
        root2.geometry('600x400+50+50')
        
        def true():
            x=Label(root2,text=data[get_close_matches(w,data.keys())[0]])
            x.grid(column=0, row=3)
        
        def no():
            v= Label(root2,text="We don't have your word in our dictionary.")
            v.grid(column=0,row=3)
            
        labl1=Label(root2,text=("Do you mean %s instead?[Yes/No]"%get_close_matches(w,data.keys())[0]))
        labl1.grid(column=0,row=0)
        
        yes=Button(root2,text='Yes', command= true)
        yes.grid(column=0,row=1)
        
        nope=Button(root2,text='No',command= no)
        nope.grid(column=1,row=1)
        


e=Entry(root,width=15,borderwidth=3)             #to get input
e.grid(column=3,row=0,padx=6,pady=2)


tran=Button(root,text='Translate',command=lambda : translate(e.get()))
tran.grid(column=3,row=1)



root.mainloop()
