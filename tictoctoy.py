from tkinter import *
from tkinter import ttk
from tkinter import messagebox

activplayer=1
p1=[]
p2=[]

root=Tk()
root.title("Tic Toc Toy : Plyer 1")
root.resizable(width=False, height=False)

#disable button function 
def desiblebutton():
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
    b5["state"] = "disabled"
    b6["state"] = "disabled"
    b7["state"] = "disabled"
    b8["state"] = "disabled"
    b9["state"] = "disabled"



def Butonclik(id):
    global activplayer,p1,p2


    if (activplayer ==1):
        setlayot(id,"X")
        p1.append(id)
        root.title("tic tac toe :player 2")
        activplayer=2



    elif (activplayer ==2):
        setlayot(id,"O")
        p2.append(id)
        root.title("player 1")
        activplayer=1



    chickwiner()


def setlayot(id,text):
    if (id==1):
        b1.config(text=text)
        b1["state"] = "disabled"
    elif (id==2):
        b2.config(text=text)
        b2["state"] = "disabled"
    elif (id==3):
        b3.config(text=text)
        b3["state"] = "disabled"
    elif (id==4):
        b4.config(text=text)
        b4["state"] = "disabled"
    elif (id==5):
        b5.config(text=text)
        b5["state"] = "disabled"


    elif (id==6):
        b6.config(text=text)
        b6["state"] = "disabled"

    elif (id==7):
        b7.config(text=text)
        b7["state"] = "disabled"
    elif (id==8):
        b8.config(text=text)
        b8["state"] = "disabled"
    elif (id==9):
        b9.config(text=text)
        b9["state"] = "disabled"



def chickwiner():
    winer=-1
    if ((1 in p1 )and (2 in p1 ) and (3 in p1)):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winer=1

    if ((1 in p2 )and (2 in p2 ) and (3 in p2)):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winer=2


    if ((4 in p1 )and (5 in p1 ) and (6 in p1)):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winer=1
    if ((4 in p2 )and (5 in p2 ) and (6 in p2)):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winer=2

    if ((7 in p1 )and (8 in p1 ) and (9 in p1)):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winer=1
    if ((7 in p2 )and (8 in p2 ) and (9 in p2)):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winer=2

    if ((1 in p1 )and (4 in p1 ) and (7 in p1)):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winer=1
    if ((1 in p2 )and (4 in p2 ) and (7 in p2)):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winer=2
    
    if ((2 in p1 )and (5 in p1 ) and (8 in p1)):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winer=1
    if ((2 in p2 )and (5 in p2 ) and (8 in p2)):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winer=2  
    
    if ((3 in p1 )and (6 in p1 ) and (9 in p1)):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winer=1  
    if ((3 in p2 )and (6 in p2 ) and (9 in p2)):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winer=2
    
    
    
    
    if ((1 in p1 )and (5 in p1 ) and (9 in p1)):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winer=1
    if ((1 in p2 )and (5 in p2 ) and (9 in p2)):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winer=2
    if ((3 in p1 )and (5 in p1 ) and (7 in p1)):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winer=1
    if ((3 in p2 )and (5 in p2 ) and (7 in p2)):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winer=2






    if winer ==1:
        messagebox.showinfo(title="Winner ",message="Winer is Player 1")
        desiblebutton()
    elif winer ==2:
        messagebox.showinfo(title="Winner ",message="Winer is Player 2")
        desiblebutton()



def rest():
    global b1,b2, b3,b4,b5,b6,b7,b8,b9
    global activplayer,p1,p2
    activplayer=1
    p1=[]
    p2=[]

    b1=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(1))
    b1.grid(row=0, column=0)



    b2=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(2))
    b2.grid(row=0, column=1)


    b3=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(3))
    b3.grid(row=0, column=2)


    b4=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(4))
    b4.grid(row=1, column=0)

    b5=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(5))
    b5.grid(row=1, column=1)

    b6=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(6))
    b6.grid(row=1, column=2)


    b7=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(7))
    b7.grid(row=2, column=0)


    b8=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(8))
    b8.grid(row=2, column=1)

    b9=Button(root,text=" ", font=("helvetica",20),height=3,width=6 ,bg="SystemButtonFace",command=lambda : Butonclik(9))
    b9.grid(row=2, column=2)

rest()
my_mnu=Menu(root)
root.config(menu=my_mnu)
option_menu=Menu(my_mnu,tearoff=False)
my_mnu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="reset Game",command=rest)
    

root.mainloop()


