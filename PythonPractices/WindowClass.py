import tkinter as t

class Windowz(t.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        label = t.Label(self,text = "Hello World")
        label.pack(fill = t.BOTH,padx=100,pady=50,expand=1)

if __name__ == "__main__":
    win = Windowz()
    win.mainloop()        