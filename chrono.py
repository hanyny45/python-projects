


import time
from tkinter import *
from tkinter import messagebox


# creating Tk window
root=Tk()

root.geometry("300x250")
root.title("Time counter ")
hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")
hourEntry =Entry(root ,width=3,font=("Arial",18,""),textvariable=hour)
hourEntry.place(x=80,y=20)
minutEntry =Entry(root ,width=3,font=("Arial",18,""),textvariable=minute)
minutEntry.place(x=130,y=20)
secondEntry=Entry(root,width=3,font=('Arial',18,""),textvariable=second)
secondEntry.place(x=180,y=20)
def submit():
	try:
		# the input provided by the user is
		# stored in here :temp
    	 temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
		
        
	while temp >-1:
		
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
		mins,secs = divmod(temp,60) 

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
		hours=0
		if mins >60:
			hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to 
		# two decimal places
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))
		root.update()
		time.sleep(1)
		if (temp == 0):
			messagebox.showinfo("Time Countdown", "Time's up ")
		temp -= 1


btn=Button(root,text='Set Time Countdown',bd='5',command=submit)
btn.place(x=70,y =120)


root.mainloop()


