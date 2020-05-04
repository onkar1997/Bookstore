# importing all modules from tkinter
from tkinter import *
# importing backend.py file 
import backend

# getting selected data by the user
def get_selected_row(event):
    try:
        global selected_tuple
        index=l1.curselection()[0]
        selected_tuple=l1.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

# function to view the data
def view_command():
    l1.delete(0,END)
    for row in backend.view():
        l1.insert(END, row)

# searching data function
def search_command():
    l1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        l1.insert(END, row)

# adding data
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    l1.delete(0,END)
    l1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

# deleting data
def delete_command():
    backend.delete(selected_tuple[0])

# updating data
def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

# function to clear all the data
def clearall_command():
    l1.delete(0,END)
    backend.clearall()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

# function to clear data from text boxes
def clear_command():
    backend.clear()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


window= Tk()

window.wm_title("BOOK STORE APP")

l1=Label(window, text="TITLE :")
l1.grid(row=0,column=0)

l2=Label(window, text="AUTHOR :")
l2.grid(row=0,column=2)

l3=Label(window, text="YEAR :")
l3.grid(row=1,column=0)

l4=Label(window, text="ISBN :")
l4.grid(row=1,column=2)

title_text= StringVar()
e1=Entry(window, textvariable= title_text)
e1.grid(row=0, column=1)

author_text= StringVar()
e2=Entry(window, textvariable= author_text)
e2.grid(row=0, column=3)

year_text= StringVar()
e3=Entry(window, textvariable= year_text)
e3.grid(row=1, column=1)

isbn_text= StringVar()
e4=Entry(window, textvariable= isbn_text)
e4.grid(row=1, column=3)

l1= Listbox(window, height=13, width=40)
l1.grid(row=3, column=0, rowspan=9, columnspan=2)

sb1= Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

l1.configure(yscrollcommand=sb1.set)
sb1.configure(command=l1.yview)

l1.bind('<<ListboxSelect>>',get_selected_row)

b1= Button(window, text="View All", width=15, command=view_command)
b1.grid(row=3, column=3)

b2= Button(window, text="Search Entry", width=15, command=search_command)
b2.grid(row=4, column=3)

b3= Button(window, text="Add Entry", width=15, command=add_command)
b3.grid(row=5, column=3)

b4= Button(window, text="Update", width=15, command=update_command)
b4.grid(row=6, column=3)

b5= Button(window, text="Delete", width=15, command=delete_command)
b5.grid(row=7, column=3)

b6= Button(window, text="Close", width=15, command=window.destroy)
b6.grid(row=8, column=3)

b7= Button(window, text="Clear All", width=15, command=clearall_command)
b7.grid(row=9, column=3)

b8= Button(window, text="Clear", width=50, command=clear_command)
b8.grid(row=2, column=0, columnspan=4)

window.mainloop()
