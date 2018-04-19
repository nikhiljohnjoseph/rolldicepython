from tkinter import *
import matplotlib.pyplot as plt
import random

i=0
valueArr=[]
rollingNo=[]
count=[0,0,0,0,0,0]

def click():
    intro.destroy()
    global i;
    i+=1
    diceNumber=random.randint(1,6)
    Label (window, text=diceNumber, bg="black", fg="white", font="none 20 bold", height=5) .grid(row=1, column=0, sticky=N)
    valueArr.append(diceNumber)
    rollingNo.append(i)
    count[diceNumber-1]=count[diceNumber-1]+1
    print("Dice rolling Number ",i," is ",diceNumber)

        
    
window=Tk()
window.title("My canvas")
window.configure(background="black")


icon = PhotoImage(file="cool.gif")
window.tk.call('wm','iconphoto',window._w,icon)


pic= PhotoImage(file="cool.gif")
Label (window, text="The Rolling Dice Machine", bg="black", fg="white", font="none 12 bold") .grid(row=0, column=0, sticky=N)
intro=Label (window, text="Not Yet Rolled", bg="black", fg="white", font="none 12 bold", height=5)
intro.grid(row=1, column=0, sticky=N)
Button(window, text="Roll", width=6, command=click) .grid(row=2, column=0, sticky=N)
window.mainloop()

print(valueArr)
plt.pie(count,labels=[1,2,3,4,5,6])
plt.show()
