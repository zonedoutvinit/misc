from tkinter import *   #For Gui components
from tkinter import ttk
import sqlite3 as db  #For DB
from tkcalendar import DateEntry #For Calender GUI

# this init the sqlite3 db connection 
def init():
    connectionObjn = db.connect("expense.db") #Connection obj with sqlite3 .db file
    curr = connectionObjn.cursor()
    #Query
    query = '''
    create table if not exists expenses (
        date string,
        name string,
        title string,
        expense number
        )
    '''
    curr.execute(query)
    connectionObjn.commit()
    
#Submit button     
def submit():
    values=[dateEntry.get(),Name.get(),Title.get(),Expense.get()]
    print(values)
    Etable.insert('','end',values=values)
    connectionObjn = db.connect("expense.db")
    curr = connectionObjn.cursor()
    #Query
    query = '''
    INSERT INTO expenses VALUES 
    (?, ?, ?, ?)
    '''
    curr.execute(query,(dateEntry.get(),Name.get(),Title.get(),Expense.get()))
    connectionObjn.commit()
    
#View button 
def view():
    connectionObjn = db.connect("expense.db")
    curr = connectionObjn.cursor()
    #Queries
    query = '''
     select * from expenses
    '''
    total='''
    select sum(expense) from expenses
    '''
    curr.execute(query)
    rows=curr.fetchall()
    curr.execute(total)
    amount=curr.fetchall()[0]
    print(rows)
    print(amount)
    
    l=Label(root,text="Date\t  Name\t  Title\t  Expense",font=('arial',15,'bold'),bg="Skyblue",fg="white")
    l.grid(row=6,column=0,padx=7,pady=7)
    st=""
    for i in rows:
        for j in i:
            st+=str(j)+'\t'
        st+='\n'
    print(st)
    l=Label(root,text=st,font=('arial',12))
    l.grid(row=7,column=0,padx=7,pady=7)
    
    
init()
root=Tk()
root.title("Expense Tracker")
root.geometry('900x500')

#Definitions
dateLabel=Label(root,text="Date",font=('arial',15,'bold'),bg="Skyblue",fg="white",width=12)
dateLabel.grid(row=0,column=0,padx=7,pady=7)

dateEntry=DateEntry(root,width=12,font=('arial',15,'bold'))
dateEntry.grid(row=0,column=1,padx=7,pady=7)

Name=StringVar()
nameLabel=Label(root, text="Name",font=('arial',15,'bold'),bg="Yellow",fg="white",width=12)
nameLabel.grid(row=1,column=0,padx=7,pady=7)
NameEntry=Entry(root,textvariable=Name,font=('arial',15,'bold'))
NameEntry.grid(row=1,column=1,padx=7,pady=7)

Title=StringVar()
titleLabel=Label(root, text="Title",font=('arial',15,'bold'),bg="Red",fg="white",width=12)
titleLabel.grid(row=2,column=0,padx=7,pady=7)
titleEntry=Entry(root,textvariable=Title,font=('arial',15,'bold'))
titleEntry.grid(row=2,column=1,padx=7,pady=7)

Expense=IntVar()
expenseLabel=Label(root,text="Expense",font=('arial',15,'bold'),bg="SeaGreen",fg="white",width=12)
expenseLabel.grid(row=3,column=0,padx=7,pady=7)
expenseEntry=Entry(root,textvariable=Expense,font=('arial',15,'bold'))
expenseEntry.grid(row=3,column=1,padx=7,pady=7)

submitbtn=Button(root, command=submit, text="Submit", font=('arial',15,'bold'), bg="DodgerBlue2", fg="white", width=12)
submitbtn.grid(row=4,column=0,padx=13,pady=13)

viewtn=Button(root, command=view, text="View expenses", font=('arial',15,'bold'), bg="DodgerBlue2", fg="white", width=12)
viewtn.grid(row=4,column=1,padx=13,pady=13)

# all saved expenses--------------
Elist=['Date','Name','Title','Expense']
Etable=ttk.Treeview(root,column=Elist,show='headings',height=7)
for c in Elist:
    Etable.heading(c,text=c.title())
Etable.grid(row=5,column=0,padx=7,pady=7,columnspan=3)

mainloop()
