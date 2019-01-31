"""
The Program stores the book information in a database
Title, Author
Year, ISBN

User can:
Search an Entry.
View all Entries
Update Entries
Delete Entries
Close
"""
'''The textvariable parameter excepts as a parameter the value that the user will enter in the Entry widget, and that is a special
   datatype.'''

from tkinter import *
import backend


def view_all():
    results = backend.view()
    if list1.size() > 0: list1.delete(0, END)
    for row in results:
        # print(type(row[1]))
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    title = title_entry.get()
    name = author_entry.get()
    year= year_entry.get()
    isbn= isbn_entry.get()
    # print("{} {} {} {}".format(type(title), type(name), type(year), type(isbn)))
    if title!="" or name!="" or year!="" or isbn!="":
        for row in backend.search(title, name, year, isbn):
            list1.insert(END, row)


def add_command():
    if title_entry.get()!="" and author_entry.get()!="" and year_entry.get()!="" and isbn_entry.get()!="":
        backend.insert(title= title_entry.get(), author=author_entry.get(), year= year_entry.get(), isbn=isbn_entry.get())
        list1.delete(0, END)
        list1.insert(END, (title_entry.get()!="" and author_entry.get()!="" and year_entry.get()!="" and isbn_entry.get()!=""))


def get_selected_row(event):
    # list1.delete(0, END)
    global row, index
    index = list1.curselection()
    index = list1.index(index)
    row = list1.get(index)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.insert(END, row[1])
    e2.insert(END, row[2])
    e3.insert(END, row[3])
    e4.insert(END, row[4])


def delete_command():
    id = row[0]
    backend.delete(id)
    list1.delete(index)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def update_command():
    if title_entry.get()!="" and author_entry.get()!="" and year_entry.get()!="" and isbn_entry.get()!="":
        list1.delete(index)
        list1.insert(index, (row[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get()))
        backend.update(row[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)


if __name__ == '__main__':
    window = Tk()

    window.title("BookStore")

    l1 = Label(window, text="Title")
    l1.grid( row=0, column=0)

    l2 = Label(window, text="Author")
    l2.grid( row=0, column=2)

    l3 = Label(window, text="Year")
    l3.grid( row=1, column=0)

    l4 = Label(window, text="ISBN")
    l4.grid( row=1, column=2)

    title_entry = StringVar()
    e1 = Entry(window, textvariable=title_entry)
    e1.grid(row=0, column=1)

    author_entry = StringVar()
    e2 = Entry(window, textvariable=author_entry)
    e2.grid(row=0, column=3)

    year_entry = StringVar()
    e3 = Entry(window, textvariable=year_entry)
    e3.grid(row=1, column=1)

    isbn_entry = StringVar()
    e4 = Entry(window, textvariable=isbn_entry)
    e4.grid(row=1, column=3)

    list1 = Listbox(window, height=6, width=35)
    list1.grid(row=2, column=0, rowspan=6, columnspan=2)

    list1.bind('<<ListboxSelect>>', get_selected_row)

    sb1 = Scrollbar(window)
    sb1.grid(row=2, column=2, rowspan=6)

    sb2 = Scrollbar(window, orient= HORIZONTAL)
    sb2.grid(row=7, column=0, columnspan=2)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.configure(xscrollcommand=sb2.set)
    sb2.configure(command=list1.xview)

    b1= Button(window, text="View All", width=12, command= view_all)
    b1.grid(row=2, column=3)

    b2= Button(window, text="Search Entry", width=12, command=search_command)
    b2.grid(row=4, column=3)

    b3= Button(window, text="Add Entry", width=12, command= add_command)
    b3.grid(row=3, column=3)

    b4= Button(window, text="Delete Selected", width=12, command=delete_command)
    b4.grid(row=6, column=3)

    b5= Button(window, text="Update Selected", width=12, command= update_command)
    b5.grid(row=5, column=3)

    b6= Button(window, text="Close", width=12)
    b6.grid(row=7, column=3)

    mainloop()

    backend.closeConnection()