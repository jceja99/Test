import tkinter

root = tkinter.Tk()
root.title("TRASH PROGRAM 2019")
root.columnconfigure(0, minsize=100)
root.columnconfigure(1,minsize=200)

def button1func():
    label_1.config(image=img1)
    label_2.config(text="Thanos nigga")

def button2func():
    label_1.config(image=img2)
    label_2.config(text="WestTrash :(")

def button3func():
    label_1.config(image=img3)
    label_2.config(text="FUCK THIS FOO")

img1 = tkinter.PhotoImage(file="Thanos.png")
img1thumb = img1.subsample(5)

img2 = tkinter.PhotoImage(file="Westbrick.png")
img2thumb = img2.subsample(8)

img3 = tkinter.PhotoImage(file="Lillard.png")
img3thumb = img3.subsample(4)

label_1 = tkinter.Label(root, text="All these niggas trash")
label_1.grid(row=1, rowspan =3, column=1)

label_2 = tkinter.Label(root, text = "===Select a bag of garbage===")
label_2.grid(row=0, column=1)

Button1 = tkinter.Button(root, image=img1thumb, text="Ha", bg="black", width=100, height=100, command=lambda: button1func())
Button1.grid(row=1, column=0)

Button2 = tkinter.Button(root, image=img2thumb, text="Garb", bg="black", width=100, height=100, command=lambda: button2func())
Button2.grid(row=2, column=0)

Button3 = tkinter.Button(root, image=img3thumb, text="kys fgt", bg="black", width=100, height=100, command=lambda: button3func())
Button3.grid(row=3, column=0)

root.mainloop()


