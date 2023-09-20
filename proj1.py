from tkinter import *


def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text== "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            value = eval(screen.get())


        scvalue.set(value)
        screen.update() 
    elif text== 'c':
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root = Tk()
root.geometry("600x400")
root.title("calculator by prabesh")



scvaue = StringVar()
scvaue.set("")
screen = Entry(root, textvariable=scvaue,font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10,padx=10)

f = Frame(root,bg="grey")
b = Button(f,text="9",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)


b = Button(f,text="8",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)

b = Button(f,text="7",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)
f.pack()


f = Frame(root,bg="grey")
b = Button(f,text="6",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)


b = Button(f,text="5",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)

b = Button(f,text="4",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)
f.pack()


f = Frame(root,bg="grey")
b = Button(f,text="3",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=12)


b = Button(f,text="2",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=12)

b = Button(f,text="1",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)
f.pack()


f = Frame(root,bg="grey")
b = Button(f,text="0",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)


b = Button(f,text="+",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)

b = Button(f,text="-",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)
f.pack()


f = Frame(root,bg="grey")
b = Button(f,text="/",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)


b = Button(f,text="*",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)

b = Button(f,text="%",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="=",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)


b = Button(f,text="C",padx=20,pady=15,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=3)


f.pack()




root.mainloop()



