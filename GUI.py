from tkinter import *                             #importing libraries 
from difflib import get_close_matches
import json

root=Tk()                                         #window configs

root.title("Dictionary")
root.iconbitmap("path\\Martz90-Circle-Books.ico") #replace path with the path of respected files
root.config(background='#1D1C1A')
root.geometry('600x400+50+50')
root.minsize(500,500)
root.maxsize(500,500)

data=json.load(open("path\\dic.json")) #opening file which have dictionry's data


count=0


#defining functions 


def delete():                     #it deletes the pre-existing label
    label.destroy()

def coun():                       #it counts number of clicks
    global count
    count = count+1
    return count

def translate(w):                 #its the main function that finds the meaning of word
    w=w.lower()
    if w in data and count==0:    #normal conditions when the session is just started with 0 translates
        global label
        
        label=Label(root,text=data[w],wraplength=150,bg='#1D1C1A',fg='#ffffff')
        label.grid(column=0,row=2,sticky=EW)
    elif count>0:                 #if translate function is already once
        delete()
        label=Label(root,text=data[w],wraplength=150,bg='#1D1C1A',fg='#ffffff')
        label.grid(column=0,row=2,sticky=EW)
    
        

    elif len(get_close_matches(w,data.keys()))>0:                                 #condition if the word is misspelt 
        root2=Toplevel(root)                                                      #second window
        root2.config(background='#404040')
        root2.iconbitmap("path\\Martz90-Circle-Books.ico")
        root2.geometry('600x400+50+50')
        root2.minisize(400,400)
        root2.maxsize(400,400)
        
        def true():
            x=Label(root2,text=data[get_close_matches(w,data.keys())[0]],wraplength=130)
            x.grid(column=0, row=3,sticky=EW)
        
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
e.grid(column=3,row=0,padx=6,pady=2,sticky=N)


tran=Button(root,text='Find Meaning',command=lambda : [translate(e.get()),coun()])
tran.grid(column=3,row=1)



root.mainloop()