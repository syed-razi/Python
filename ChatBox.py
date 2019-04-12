from Tkinter import *
import ttk


def putinchat(*args):
    texttoadd = str(text.get()) + "\n"
    print(texttoadd)
    history.insert(1.0, texttoadd)
    text.set("")


root = Tk()
root.title("Message Box")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

mainframe.configure()

text = StringVar()

text_entry = ttk.Entry(mainframe, width=50, textvariable=text)
text_entry.grid(column=1, row=3, columnspan=3, sticky=(W, E))

ttk.Button(mainframe, text="Enter", command=putinchat).grid(
    column=4, row=3, columnspan=1, sticky=(W, E))

history = Text(mainframe, width=50, height=20)
history.grid(column=1, row=1, columnspan=3, sticky=(W, E))

root.bind('<Return>', putinchat)
