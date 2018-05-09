from tkinter import *
import matplotlib.pyplot as plt
import random
import sqlite3
from sqlite3 import Error

i=0
valueArr=[]
rollingNo=[]
count=[0,0,0,0,0,0]
database = "DiceRoll.db"
window=Tk()
intro=Label (window, text="Not Yet Rolled", bg="black", fg="white", font="none 12 bold", height=5)


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

conn = create_connection(database)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created succesfully!")
    except Error as e:
        print(e)

def create_rollingData(conn, dice_Data):
    sql = ''' INSERT INTO rollingData(value) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, dice_Data)
    return cur.lastrowid


def click():
    intro.destroy()
    global i;
    i+=1
    diceNumber=random.randint(1,6)
    Label (window, text=diceNumber, bg="black", fg="white", font="none 20 bold", height=5) .grid(row=1, column=0, sticky=N)
    valueArr.append(diceNumber)
    rollingNo.append(i)
    count[diceNumber-1]=count[diceNumber-1]+1
    dice_Data = (diceNumber);
    with conn:
        create_rollingData(conn, dice_Data)
    print("Dice rolling Number ",i," is ",diceNumber)


def main():

    # create a database connection
    sql_create_rollingData_table = """ CREATE TABLE IF NOT EXISTS rollingData (
                                        value integer NOT NULL
                                    );
                                     """
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_rollingData_table)
        print("Hurray! Connection to the database has esatablished.")
        # create tasks table
        #create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")





    window.title("My canvas")
    window.configure(background="black")


    icon = PhotoImage(file="cool.gif")
    window.tk.call('wm','iconphoto',window._w,icon)


    pic= PhotoImage(file="cool.gif")
    Label (window, text="The Rolling Dice Machine", bg="black", fg="white", font="none 12 bold") .grid(row=0, column=0, sticky=N)

    intro.grid(row=1, column=0, sticky=N)
    Button(window, text="Roll", width=6, command=click) .grid(row=2, column=0, sticky=N)
    window.mainloop()



    print(valueArr)
    plt.pie(count,labels=[1,2,3,4,5,6])
    plt.show()
    conn.close()


if __name__ == '__main__':
    main()
