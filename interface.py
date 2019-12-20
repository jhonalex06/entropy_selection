import tkinter as tk
import pandas as pd
from Categorical_Entropy import excecute_selection


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.say_hi()
        self.create_widgets()

    def create_widgets(self):

        var = tk.StringVar()
        var.set('hello')

        self.label = tk.Label(self, textvariable=var,font=10)
        self.label.grid(row=0)
        entry = tk.Entry(self)
        entry.grid(row=0, column=1)

        self.bt0 = tk.Button(self)
        self.bt0["text"] = "..."
        self.bt0["command"] = lambda: excecute_selection(self.df, True, self.text, root)
        self.bt0.grid(row=0, column=2)

        self.bt01 = tk.Button(self)
        self.bt01["text"] = "Calculate categorical entropy"
        self.bt01["command"] = lambda: excecute_selection(self.df, True, self.text)
        self.bt01.grid(row=1, column=0)

        self.bt02 = tk.Button(self)
        self.bt02["text"] = "Calculate numerical entropy"
        self.bt02["command"] = lambda: excecute_selection(self.df, True, self.text)
        self.bt02.grid(row=1, column=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=1, column=2)

        self.text = tk.Text(self, height=2, width=30)
        self.text.grid(row=2, column=0, columnspan=3, ipadx=20, ipady=40, sticky="NSEW")

    def say_hi(self):
        print("hi there, everyone!")
        self.df = pd.read_csv('breast-cancer.csv', sep=',')

root = tk.Tk()
app = Application(master=root)
app.mainloop()