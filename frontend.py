"""
Developed by Sefa LOK , Electronics Engineer and IT Specialist.

Date: 13.12.2020 , Version: 1.0

"""

from tkinter import *
from backend import Database

database=Database("books.db")


def get_selected_row(event):
    try:
        global selected_tuple
        index=lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])

        t0.delete("1.0",END)
        t0.insert(END,selected_tuple[5])

        
    except:
        pass



def view_command():
    lb1.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    t0.delete("1.0",END)

    rows=database.view()

    for row in rows[0:4]:
        lb1.insert(END,row)
    

    

def search_command():
    lb1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),t0.get("1.0",END)):
        lb1.insert(END,row)

def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),t0.get("1.0",END))
    lb1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),t0.get("1.0",END))

def clear_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    t0.delete("1.0",END)


    
def close_window():
    database.__del__()
    window.destroy()


#def Data_Scraper_window():

    DWindow=Tk()
    DWindow.wm_title("Data Scraping Window")
    DWindow.geometry("600x500")


    Label1=Label(DWindow,text="Please Enter the web URL to import data from:")
    Label1.grid(row=1,column=1)

    URL=StringVar()
    Entr1=Entry(DWindow,textvariable=URL,width=45)
    Entr1.grid(row=1,column=2)

    But1=Button(DWindow,text="Go for it",width=12)
    But1.grid(row=2,column=2)
    
    
    
    
    DWindow.mainloop()







window=Tk()

window.wm_title("Sefa's Library")

window.geometry("450x420")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1,)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

lb1=Listbox(window,height=7,width=35)
lb1.grid(row=4,column=0,rowspan=6,columnspan=2)



sb1=Scrollbar(window)
sb1.grid(row=4,column=2,rowspan=6)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

lb1.bind('<<ListboxSelect>>',get_selected_row)

l5=Label(window,text="Please enter the content here:")
l5.grid(row=47,column=1,columnspan=2)



b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=close_window)
b6.grid(row=7,column=3)

b7=Button(window,text="Clear Entries",width=12,command=clear_command)
b7.grid(row=2,column=0)

# b8=Button(window,text="Scrap Data",width=12,command=Data_Scraper_window)
# b8.grid(row=9,column=3)

t0=Text(window,height=10,width=50)
t0.grid(row=50,column=0,rowspan=6,columnspan=10)

sb2=Scrollbar(window)
sb2.grid(row=50,column=10,rowspan=6)

t0.configure(yscrollcommand=sb2.set)
sb2.configure(command=t0.yview)

window.mainloop()
