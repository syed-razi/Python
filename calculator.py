from Tkinter import *
import ttk


class Numbers:
    def __init__(self, n):
        self.n = int(n)

    def intToBinary(self, i2b):
        if i2b == 1:
            s = str(self.n % 2)
            while n > 1:
                self.n = self.n // 2
                s = str(self.n % 2) + s
            return s


class Calculator:
    num1 = ""
    num2 = ""
    operation = ""
    isNum1 = True

    def __init__(self, master):
        mainframe = ttk.Frame(master, relief=SUNKEN, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, columnspan=7, rowspan=6, sticky="NWES")
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_rowconfigure(0, weight=1)

        viewLabel = ttk.Label(mainframe, text="")
        viewLabel.grid(column=0, row=1, columnspan=5, sticky=(E, W))

        nineButton = ttk.Button(mainframe, text='9',
                                command=lambda: self.AppendDigit(9,
                                                                 viewLabel))
        nineButton.grid(column=2, row=2, pady=5)

        eightButton = ttk.Button(mainframe, text='8',
                                 command=lambda: self.AppendDigit(8,
                                                                  viewLabel))
        eightButton.grid(column=1, row=2, pady=5)

        sevenButton = ttk.Button(mainframe, text='7',
                                 command=lambda: self.AppendDigit(7,
                                                                  viewLabel))
        sevenButton.grid(column=0, row=2, pady=5)

        sixButton = ttk.Button(mainframe, text='6',
                               command=lambda: self.AppendDigit(6,
                                                                viewLabel))
        sixButton.grid(column=2, row=3, pady=5)

        fiveButton = ttk.Button(mainframe, text='5',
                                command=lambda: self.AppendDigit(5,
                                                                 viewLabel))
        fiveButton.grid(column=1, row=3, pady=5)

        fourButton = ttk.Button(mainframe, text='4',
                                command=lambda: self.AppendDigit(4,
                                                                 viewLabel))
        fourButton.grid(column=0, row=3, pady=5)

        threeButton = ttk.Button(mainframe, text='3',
                                 command=lambda: self.AppendDigit(3,
                                                                  viewLabel))
        threeButton.grid(column=2, row=4, pady=5)

        twoButton = ttk.Button(mainframe, text='2',
                               command=lambda: self.AppendDigit(2,
                                                                viewLabel))
        twoButton.grid(column=1, row=4, pady=5)

        oneButton = ttk.Button(mainframe, text='1',
                               command=lambda: self.AppendDigit(1,
                                                                viewLabel))
        oneButton.grid(column=0, row=4, pady=5)

        zeroButton = ttk.Button(mainframe, text='0',
                                command=lambda: self.AppendDigit(0,
                                                                 viewLabel))
        zeroButton.grid(column=1, row=5, pady=5)

        addButton = ttk.Button(mainframe, text='+',
                               command=lambda: self.RecordOperator('+'))
        addButton.grid(column=3, row=2, pady=5)

        subtractButton = ttk.Button(mainframe, text='-',
                                    command=lambda: self.RecordOperator('-'))
        subtractButton.grid(column=3, row=3, pady=5)

        multButton = ttk.Button(mainframe, text='*',
                                command=lambda: self.RecordOperator('*'))
        multButton.grid(column=3, row=4, pady=5)

        intdivButton = ttk.Button(mainframe, text='//',
                                  command=lambda: self.RecordOperator('//'))
        intdivButton.grid(column=3, row=5, pady=5)

        equalsButton = ttk.Button(mainframe, text='=',
                                  command=lambda: self.ComputeResult(viewLabel))
        equalsButton.grid(column=4, row=4, pady=5)

        clearButton = ttk.Button(mainframe, text='Clear',
                                 command=lambda: self.ClearAll(viewLabel))
        clearButton.grid(column=4, row=3, pady=5)

        i2b = IntVar()

        x = Numbers(equalsButton.cget("command"))

        int2binButton = ttk.RadioButtion(mainframe, text='ToBinary',
                                         variable=i2b, value=1, command=lambda: x.intToBinary(i2b))
        int2binButton.grid(column=5, row=3, pady=5)

    def AppendDigit(self, digit, viewLabel):
        if(self.isNum1):
            self.num1 = self.num1 + str(digit)
            viewLabel.config(text=self.num1)
        else:
            self.num2 = self.num2 + str(digit)
            viewLabel.config(text=self.num2)

        return

    def RecordOperator(self, op):
        self.operation = op
        self.isNum1 = False

        return

    def ComputeResult(self, viewLabel):
        if(self.operation == "+"):
            r = str(int(self.num1) + int(self.num2))
            q = ""

        elif(self.operation == "-"):
            r = str(int(self.num1) - int(self.num2))
            q = ""

        elif(self.operation == "*"):
            r = str(int(self.num1) * int(self.num2))
            q = ""

        elif(self.operation == "//"):
            r = str(int(self.num1) // int(self.num2))
            q = "R" + str(int(self.num1) % int(self.num2))

        viewLabel.config(text=(r + q))

        self.num1 = r
        self.num2 = ""
        self.isNum1 = True

        return

    def ClearAll(self, viewLabel):
        self.num1 = ""
        self.num2 = ""
        self.operation = ""
        isNum1 = True

        viewLabel.config(text="")

        return

        # View label
        # 0 −− 9 Buttons
        # Operation Buttons (+ , −, ∗ , // )
        # Equals (=) and Clear Buttons


def main():
    master = Tk()

    Calculator(master)

    master.title("Calculator")
    master.mainloop()


if __name__ == main():
    main()
