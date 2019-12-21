import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pandas as pd
from Categorical_Entropy import excecute_selection
from chimerge import excecute_chimerge

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        #self.load_data()
        self.create_widgets()
    
    def load_data(self):        
        self.filename = filedialog.askopenfilename()
        self.df = pd.read_csv(self.filename, sep=',')
        self.entry.insert(tk.END,self.filename)
        self.combo["values"] = self.df.columns.tolist()
        self.combo.set(self.df.columns.tolist()[len(self.df.columns.tolist()) - 1])

    def create_widgets(self):
        var = tk.StringVar()
        var.set('choose the csv: ')

        self.label = tk.Label(self, textvariable=var,font=12)
        self.label.grid(row=0)
        self.entry = tk.Entry(self, width=26)
        self.entry.grid(row=0, column=1)

        self.bt0 = tk.Button(self, width=16)
        self.bt0["text"] = "..."
        self.bt0["command"] = lambda: self.load_data()
        self.bt0.grid(row=0, column=2)

        self.bt01 = tk.Button(self)
        self.bt01["text"] = "Calculate categorical entropy"
        self.bt01["command"] = lambda: excecute_selection(self.df, True, self.text, root)
        self.bt01.grid(row=1, column=0)

        self.bt02 = tk.Button(self)
        self.bt02["text"] = "Calculate numerical entropy"
        self.bt02["command"] = lambda: excecute_selection(self.df, True, self.text, root)
        self.bt02.grid(row=1, column=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=1, column=2, sticky="NSEW")

        self.text = tk.Text(self, height=2, width=30)
        self.text.grid(row=2, column=0, columnspan=3, ipadx=20, ipady=80, sticky="NSEW")

        scrollb = ttk.Scrollbar(self, command = self.text.yview)
        scrollb.grid(row=2, column=3, sticky='nsew')
        self.text['yscrollcommand'] = scrollb.set

        self.combo = ttk.Combobox(self, width=24)
        self.combo.grid(row=3, column=0)

        self.combo2 = ttk.Combobox(self, width=24)
        self.combo2.grid(row=3, column=1)
        self.combo2["values"] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.combo2.set('1')

        self.bt03 = tk.Button(self)
        self.bt03["text"] = "Calculate Chi-Merge"
        self.bt03["command"] = lambda: excecute_chimerge(self.df, self.combo.get(), self.combo2.get(), self.text, root)
        self.bt03.grid(row=3, column=2, sticky="NSEW")

root = tk.Tk()
root.title('Selection by entropy')
app = Application(master=root)
app.mainloop()