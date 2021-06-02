from tkinter import *
import sqlite3

def printRecords():
    connection = sqlite3.connect('COVID19_testing.db')
    cur = connection.cursor()
    cur.execute("select * from COVID19_testing where  aadhar_number = ?", (z.get(),))
    connection.commit()
    variablename = cur.fetchall()
    print_records=""
    for record in variablename:
        print_records+= str(record)+'\n'

    query_label=Label(root,text=print_records)
    query_label.grid(row=4,column=0)
    if(len(variablename)==0):
        Label(root, text="Haven't got covid ").grid()
    else:

        cur.execute("select First_name from COVID19_testing where  aadhar_number = ? AND (round(julianday('now') - julianday(tested_date)))>100", (z.get(),))
        connection.commit()
        variablename1 = cur.fetchall()
        print_records1 = ""
        for record in variablename1:
            print_records1 += str(record) + '\n'
        query_label = Label(root, text=print_records1)
        query_label.grid(row=6, column=0)
        



root = Tk()
root.title ( "Search aadhar")
root.geometry('600x200')


z= StringVar()
y=StringVar()
#Label
Label(root, text = "Enter the Aadhar number you are searching for:      ").grid()
#Textbox
bookSearchEntry = Entry(root, textvariable = z)
bookSearchEntry.grid(row = 0, column = 1)
#Button
bookSearchButton = Button(root, text = "Search", command = printRecords)
bookSearchButton.grid(row = 0, column = 2)

root.mainloop()