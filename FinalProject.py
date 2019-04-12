from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("FinalProject")

class Item:
    def __init__(self, Item_Number, Quantity, Item_Name, Item_Location, Item_Description):
        self.Item_Number = Item_Number
        self.Quantity = Quantity
        self.Item_Name = Item_Name
        self.Item_Location = Item_Location
        self.Item_Description = Item_Description

    def makelist(self):
        return [self.Item_Number, self.Quantity, self.Item_Name, self.Item_Location, self.Item_Description]

    def getItem_Number(self):
        return self.Item_Number

def choosereadfile():
    readfile = filedialog.askopenfilename()
    loaddata(readfile)

#def choosewritefile():
    #writefile = filedialog.askopenfilename()
    #savedata(writefile)

def savedata():
    storeddata = open("storeddata.txt", "r")
    updateddata = open("updateddata.txt", "w")
    for line in storeddata:
        line = line[:-1]
        print(line, file=updateddata)
    storeddata.close
    updateddata.close
    

def loaddata(readfile):
    items = []
    data = open(readfile, "r")
    for line in data:
    #file_contents = data.read()
    #file_contents
    #print(file_contents, end="")
        #print(line, end="")
        #line = line[:-1]
        line = line.strip()
        line = line.split(",")
        items.append(line)
        #print(line)
    #print(items)
    data.close
    objectlist = [Item(*item).makelist() for item in items]
    storeddata = open("storeddata.txt", "w")
    for o in objectlist:
        print(o, file=storeddata)
    storeddata.close
    #print(objectlist[0].getItem_Number())
    print(objectlist)

def additem(*args):
    a = Item_Number.get()
    b = Quantity.get()
    c = Item_Name.get()
    d = Item_Location.get()
    e = Item_Description.get()
    newitem = Item(a, b, c, d, e).makelist()
    storeddata = open("storeddata.txt", "a")
        

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

mainframe.configure()

Item_Number = StringVar()
Quantity = StringVar()
Item_Name = StringVar()
Item_Location = StringVar()
Item_Description = StringVar()


Item_Number_entry = ttk.Entry(mainframe, width=50, textvariable=Item_Number)
Item_Number_entry.grid(column=2, row=3, columnspan=2, sticky=(W, E))

Quantity_entry = ttk.Entry(mainframe, width=50, textvariable=Quantity)
Quantity_entry.grid(column=2, row=4, columnspan=2, sticky=(W, E))

Item_Name_entry = ttk.Entry(mainframe, width=50, textvariable=Item_Name)
Item_Name_entry.grid(column=2, row=5, columnspan=2, sticky=(W, E))

Item_Location_entry = ttk.Entry(mainframe, width=50, textvariable=Item_Location)
Item_Location_entry.grid(column=2, row=6, columnspan=2, sticky=(W, E))

Item_Description_entry = ttk.Entry(mainframe, width=50, textvariable=Item_Description)
Item_Description_entry.grid(column=2, row=7, columnspan=2, sticky=(W, E))


ttk.Label(mainframe, text="Item Number").grid(column=1, row=3, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="Quantity").grid(column=1, row=4, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="Item Name").grid(column=1, row=5, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="Item Location").grid(column=1, row=6, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="Item Description").grid(column=1, row=7, columnspan=1, sticky=(W, E))
                                                                                    

ttk.Button(mainframe, text="Enter").grid(column=4, row=3, columnspan=1, sticky=(W, E))

ttk.Button(mainframe, text="New").grid(column=5, row=3, columnspan=1, sticky=(W, E))
ttk.Button(mainframe, text="Delete").grid(column=5, row=4, columnspan=1, sticky=(W, E))
ttk.Button(mainframe, text="Search").grid(column=5, row=5, columnspan=1, sticky=(W, E))
ttk.Button(mainframe, text="Update").grid(column=5, row=6, columnspan=1, sticky=(W, E))
ttk.Button(mainframe, text="Load Data", command=choosereadfile).grid(column=5, row=7, columnspan=1, sticky=(W, E))
ttk.Button(mainframe, text="Save Data", command=savedata).grid(column=5, row=8, columnspan=1, sticky=(W, E))

#root.bind('<Return>', putinchat)
