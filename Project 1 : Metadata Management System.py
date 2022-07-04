"""
Description:
In a Data Warehouse, upstream sends out data that needs to be stored in different tables.
These tables can have multiple attributes having different types of data.
Also, in every release there are attribute changes happening in the metadata as per business communications.
For anyone to get the latest details of a table and its content, a Metadata sheet needs to be maintained by the Modeller of the Data Warehouse.
In our project, these details were maintained in an Excel sheet and were having some drawbacks:
    1. As the size of excel sheet increased, the process became slow as it was not able to handle huge amount of data.
    2. Filtering down of required data was comparatively slower.
So, we came up with an idea of moving all the Metadata details to a Database, and create a GUI using python to handle the upcoming changes in data.
This program has below functionalities:
    1. Insert new attribute and table details
    2. Delete old records
    3. Update old records
    4. Duplicate records cannot be inserted
Advantages:
    1. Quick and easy maintenance of Metadata details
    2. Secured user access
    3. Simple visualization of records
Tools used:
Python and SQL
Packages used in Python:
Tkinter and sqlite3

Tasks:
Need to fix the scrollbar : https://serveanswer.com/questions/horizontal-scrollbar-for-treeview
add a quit button and then ask do you really want to quit : https://www.geeksforgeeks.org/create-a-yes-no-message-box-in-python-using-tkinter/
add a singup button and when one does the signup add the details in a list
when someone requests for a singup and submits his details then it should send to the admin team with the details, then admin team needs to approve it, then only the person should be able to access the Metadata management system
Add a login screen -- done
update functionality -- done
add message text to show that duplicate record cannot be inserted when asked to do so -- done

Links:
Geek for Geeks : https://www.geeksforgeeks.org/python-gui-tkinter/
Building Out The GUI for our Database App - Python Tkinter GUI Tutorial #20 : https://www.youtube.com/watch?v=AK1J8xF4fuk&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=20
Delete Database Record With Treeview - Python Tkinter GUI Tutorial #178 : https://www.youtube.com/watch?v=n0usdtoU5cE
CRUD Operation in Python With SQLite Database. || Database Connection || Login and Registration Form : https://www.youtube.com/watch?v=h6wJV2qPBR8
Python Tkinter Crud Step by Step GUI Mysql Database : https://www.youtube.com/watch?v=Jpf_G1D3TlE
Github : https://github.com/r2123b/TreeViewHorizontalScrollbar/blob/master/SampleCode.py
Exception handling : https://www.geeksforgeeks.org/python-exception-handling/
"""

import tkinter
import sqlite3
from tkinter import messagebox, ttk
from tkinter import *

connection = sqlite3.connect("Metadata_Database.db")
crsr = connection.cursor()

master_login = tkinter.Tk()
master_login.title('Login : Metadata Management System')

#photo = tkinter.PhotoImage(file = r"/Users/shubham.chand/Downloads/Python/metadata.png")
photo = tkinter.PhotoImage(file = r"metadata.png")
icon_login = tkinter.Label(image=photo)
icon_login.grid(row=0, column=0)

text_login = tkinter.Label(master_login, text='Please enter the credentials below:', foreground='Yellow', font=("Arial", 15))
text_login.grid(row=0, column=1)

user_id_label = tkinter.Label(master_login, text="User Id")
user_id_label.grid(row=1, column=0, pady=10)
password_label = tkinter.Label(master_login, text="Password")
password_label.grid(row=2, column=0, pady=10)

user_id = tkinter.Entry(master_login, width=30)
user_id.grid(row=1, column=1, pady=10)
password = tkinter.Entry(master_login, width=30, show="*")
password.grid(row=2, column=1, pady=10)

def login_success():

    master = tkinter.Toplevel()
    master.title('Metadata Management System')

    '''
    # CREATE TABLE
    crsr.execute("""Create table Metadata (
    Logical_Table_Name text Primary Key,
    Physical_Table_Name text Not Null,
    Logical_Attribute_Name text Not Null,
    Physical_Attribute_Name text Not Null,
    Datatype text NOT NULL,
    Definition text,
    Primary_Key text,
    Foreign_Key text)""")
    '''

    # Labels
    l_table_label = tkinter.Label(master, text="Logical Table Name")
    p_table_label = tkinter.Label(master, text="Physical Table Name")
    l_attr_label = tkinter.Label(master, text="Logical Attribute Name")
    p_attr_label = tkinter.Label(master, text="Physical Attribute Name")
    data_label = tkinter.Label(master, text="Datatype of Attribute")
    defi_label = tkinter.Label(master, text="Definition of Attribute")
    pk_label = tkinter.Label(master, text="Is this a Primary Key?")
    fk_label = tkinter.Label(master, text="Is this a Foreign Key?")
    l_table_label.grid(row=0, column=0, pady=10)
    p_table_label.grid(row=1, column=0, pady=10)
    l_attr_label.grid(row=2, column=0, pady=10)
    p_attr_label.grid(row=3, column=0, pady=10)
    data_label.grid(row=4, column=0, pady=10)
    defi_label.grid(row=5, column=0, pady=10)
    pk_label.grid(row=6, column=0, pady=10)
    fk_label.grid(row=7, column=0, pady=10)

    # Inputs
    l_table = tkinter.Entry(master, width=30)
    p_table = tkinter.Entry(master, width=30)
    l_attr = tkinter.Entry(master, width=30)
    p_attr = tkinter.Entry(master, width=30)
    data = tkinter.StringVar()
    data1 = tkinter.Radiobutton(master, text='TEXT', variable=data, value='TEXT')
    data2 = tkinter.Radiobutton(master, text='INTEGER', variable=data, value='INTEGER')
    data3 = tkinter.Radiobutton(master, text='REAL', variable=data, value='REAL')
    data.set('NONE')
    defi = tkinter.Entry(master, width=30)
    pk1= tkinter.StringVar()
    pk = tkinter.Checkbutton(master, width=30, variable=pk1, onvalue='Y', offvalue='N')
    pk1.set('N')
    fk1= tkinter.StringVar()
    fk = tkinter.Checkbutton(master, width=30, variable=fk1, onvalue='Y', offvalue='N')
    fk1.set('N')
    l_table.grid(row=0, column=1, columnspan=3)
    p_table.grid(row=1, column=1, columnspan=3)
    l_attr.grid(row=2, column=1, columnspan=3)
    p_attr.grid(row=3, column=1, columnspan=3)
    data1.grid(row=4, column=1)
    data2.grid(row=4, column=2)
    data3.grid(row=4, column=3)
    defi.grid(row=5, column=1, columnspan=3)
    pk.grid(row=6, column=1, columnspan=3)
    fk.grid(row=7, column=1, columnspan=3)


    # Reset
    def reset():
        l_table.delete(0, tkinter.END)
        p_table.delete(0, tkinter.END)
        l_attr.delete(0, tkinter.END)
        p_attr.delete(0, tkinter.END)
        data.set('NONE')
        defi.delete(0, tkinter.END)
        pk1.set('N')
        fk1.set('N')


    # Insert Records
    def insert():
        l_table_v=l_table.get()
        p_table_v=p_table.get()
        l_attr_v=l_attr.get()
        p_attr_v=p_attr.get()
        data_v=data.get()
        defi_v=defi.get()
        pk_v=pk1.get()
        fk_v=fk1.get()
        try:
            crsr.execute(f'Insert into Metadata values ("{l_table_v}", "{p_table_v}", "{l_attr_v}", "{p_attr_v}", "{data_v}", "{defi_v}", "{pk_v}", "{fk_v}")')
            connection.commit()
            print("Record Inserted : ", l_table_v, p_table_v, l_attr_v, p_attr_v, data_v, defi_v, pk_v, fk_v)
            reset()
            #messageVar=tkinter.Message(master, text='Records inserted Successfully!')
            #messageVar.config(fg='lightgreen')
            #messageVar.grid(row=9, column=0)
            messagebox.showinfo("Success", "Record inserted Successfully!")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Failure", "Duplicate record cannot be added")
        show()

    ins_record = tkinter.Button(master, text="Insert records", command=insert, foreground='green')
    ins_record.grid(row=9, column=1, pady=10)


    # Delete Records
    def delete():
        l_table_v=l_table.get()
        p_table_v=p_table.get()
        l_attr_v=l_attr.get()
        p_attr_v=p_attr.get()
        data_v=data.get()
        defi_v=defi.get()
        pk_v=pk1.get()
        fk_v=fk1.get()
        crsr.execute(f"Delete from Metadata where "
                     f"Logical_Table_Name='{l_table_v}' and Physical_Table_Name='{p_table_v}' and "
                     f"Logical_Attribute_Name='{l_attr_v}' and Physical_Attribute_Name='{p_attr_v}'")
        connection.commit()
        print("Record Deleted : ", l_table_v, p_table_v, l_attr_v, p_attr_v, data_v, defi_v, pk_v, fk_v)
        reset()
        messagebox.showinfo("Success", "Record deleted Successfully!")
        show()

    del_record = tkinter.Button(master, text="Delete records", command=delete, foreground='red')
    del_record.grid(row=9, column=2, pady=10)


    # Update Records
    def update():
        l_table_v=l_table.get()
        p_table_v=p_table.get()
        l_attr_v=l_attr.get()
        p_attr_v=p_attr.get()
        data_v=data.get()
        defi_v=defi.get()
        pk_v=pk1.get()
        fk_v=fk1.get()
        crsr.execute(f"Update Metadata set Datatype='{data_v}', Definition='{defi_v}', Primary_Key='{pk_v}', Foreign_Key='{fk_v}' where "
                     f"Logical_Table_Name='{l_table_v}' and Physical_Table_Name='{p_table_v}' and "
                     f"Logical_Attribute_Name='{l_attr_v}' and Physical_Attribute_Name='{p_attr_v}'")
        connection.commit()
        print("Record Updated : ", l_table_v, p_table_v, l_attr_v, p_attr_v, data_v, defi_v, pk_v, fk_v)
        reset()
        messagebox.showinfo("Success", "Record updated Successfully!")
        show()

    upd_record = tkinter.Button(master, text="Update records", command=update, foreground='blue')
    upd_record.grid(row=9, column=3, pady=10)


    # remove records from Tree View
    def removeall():
        for record in list.get_children():
            list.delete(record)


    # Show Records
    def show():
        l_table.config(state="normal")
        p_table.config(state="normal")
        l_attr.config(state="normal")
        p_attr.config(state="normal")
        reset()
        removeall()
        crsr.execute("SELECT * FROM metadata order by Logical_Table_Name, Physical_Table_Name, Logical_Attribute_Name, Physical_Attribute_Name")
        ans = crsr.fetchall()
        for i, (Logical_Table_Name, Physical_Table_Name, Logical_Attribute_Name, Physical_Attribute_Name, Datatype, Definition, Primary_Key, Foreign_Key) \
                in enumerate(ans, start=1):
            list.insert("", "end",
                        values=(Logical_Table_Name, Physical_Table_Name, Logical_Attribute_Name, Physical_Attribute_Name, Datatype, Definition, Primary_Key, Foreign_Key))

    sho_record = tkinter.Button(master, text="Reset", command=show)
    sho_record.grid(row=9, column=0, columnspan=1, ipadx=15)


    # Populate details for the selected record
    def GetValue(event):
        l_table.config(state="normal")
        p_table.config(state="normal")
        l_attr.config(state="normal")
        p_attr.config(state="normal")
        reset()
        row_id = list.selection()[0]
        select = list.set(row_id)
        l_table.insert(0, select['Logical_Table_Name'])
        p_table.insert(0, select['Physical_Table_Name'])
        l_attr.insert(0, select['Logical_Attribute_Name'])
        p_attr.insert(0, select['Physical_Attribute_Name'])
        crsr.execute(f"SELECT distinct * FROM metadata where "
                     f"Logical_Table_Name='{select['Logical_Table_Name']}' and Physical_Table_Name='{select['Physical_Table_Name']}' and "
                     f"Logical_Attribute_Name='{select['Logical_Attribute_Name']}' and Physical_Attribute_Name='{select['Physical_Attribute_Name']}'")
        ans = crsr.fetchall()
        for i, (Logical_Table_Name, Physical_Table_Name, Logical_Attribute_Name, Physical_Attribute_Name, Datatype, Definition, Primary_Key, Foreign_Key) \
                in enumerate(ans, start=1):
            print("Selected Record : ", Logical_Table_Name, Physical_Table_Name, Logical_Attribute_Name, Physical_Attribute_Name, end=" ")
            data.set(Datatype)
            defi.insert(0, Definition)
            pk1.set(Primary_Key)
            fk1.set(Foreign_Key)
        print()
        l_table.config(state="disabled")
        p_table.config(state="disabled")
        l_attr.config(state="disabled")
        p_attr.config(state="disabled")



    #cols=('Logical_Table_Name', 'Physical_Table_Name', 'Logical_Attribute_Name', 'Physical_Attribute_Name', 'Datatype', 'Definition', 'Primary_Key', 'Foreign_Key')
    cols=('Logical_Table_Name', 'Physical_Table_Name', 'Logical_Attribute_Name', 'Physical_Attribute_Name')
    list=ttk.Treeview(master, columns=cols, show='headings')
    for col in cols:
        list.heading(col, text=col)
        list.grid(row=0, column=4, rowspan=10, padx=20, pady=10, ipady=100)

    # attach a Horizontal (x) scrollbar to the frame
    treeXScroll = ttk.Scrollbar(master, orient=HORIZONTAL)
    treeXScroll.configure(command=list.xview)
    list.configure(xscrollcommand=treeXScroll.set)
    treeXScroll.grid(row=9, column=4, columnspan=3, ipadx=100)

    show()

    list.bind('<Double-Button-1>', GetValue)
    master.mainloop()

def check():
    if (user_id.get()=='shubham' and password.get()=='chand'):
        login_success()
    else:
        messagebox.showinfo("Failure", "Wrong Credentials")

login = tkinter.Button(master_login, text="Login", command=check, foreground='green')
login.grid(row=3, column=1, pady=10, ipadx=100)

master_login.mainloop()
connection.close()
