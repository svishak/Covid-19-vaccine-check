from tkinter import *
import sqlite3

root=Tk()
root.title('DBMS')
root.geometry('600x600')

conn=sqlite3.connect("COVID19_testing.db")

c=conn.cursor()

'''c.execute(""" CREATE TABLE COVID19_testing(
        first_name text,
        last_name text,
        address text,
        sex text,
        BU_number int,
        aadhar_number int,
        tested_date date)
        """)'''

def submit():
    conn = sqlite3.connect("COVID19_testing.db")

    c = conn.cursor()
    c.execute("INSERT INTO COVID19_testing VALUES(:f_name,:l_name,:address,:sex,:bu_number,:aadhar,:date)",
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address':address.get(),
        'sex':sex.get(),
        'bu_number':bu_number.get(),
        'aadhar':aadhar.get(),
        'date':date.get()



    })



    conn.commit()
    conn.close()


    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    sex.delete(0, END)
    bu_number.delete(0, END)
    aadhar.delete(0, END)
    date.delete(0, END)

def query():
    conn = sqlite3.connect("COVID19_testing.db")

    c = conn.cursor()
    c.execute("SELECT * FROM COVID19_testing WHERE (round(julianday('now') - julianday(tested_date)))>0  ")
    records=c.fetchall()
    #print(records)
    print_records=''
    for record in records:
        print_records+= str(record)+'\n'
    query_label=Label(root,text=print_records)
    query_label.grid(row=12,column=1)
    conn.commit()
    conn.close()



f_name= Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name= Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)

address= Entry(root,width=30)
address.grid(row=2,column=1,padx=20)

sex= Entry(root,width=30)
sex.grid(row=3,column=1,padx=20)

bu_number= Entry(root,width=30)
bu_number.grid(row=4,column=1,padx=20)

aadhar= Entry(root,width=30)
aadhar.grid(row=5,column=1,padx=20)

date= Entry(root,width=30)
date.grid(row=6,column=1,padx=20)

f_name_label=Label(root,text='First name')
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text='Last name')
l_name_label.grid(row=1,column=0)

address_label=Label(root,text='Address')
address_label.grid(row=2,column=0)

sex_label=Label(root,text='Sex')
sex_label.grid(row=3,column=0)

BU_label=Label(root,text='BU_number')
BU_label.grid(row=4,column=0)

aadhar_label=Label(root,text='Aadhar')
aadhar_label.grid(row=5,column=0)

test_date_label=Label(root,text='Tested date')
test_date_label.grid(row=6,column=0)

submit_button= Button(root,text='Add record',command=submit)
submit_button.grid(row=8,column=1,padx=6,pady=6)

query_btn= Button(root,text='Show record',command=query)
query_btn.grid(row=10,column=1,padx=6,pady=6)

conn.commit()
conn.close()

root.mainloop()

