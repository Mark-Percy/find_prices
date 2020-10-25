from tkinter import Tk, Button, Frame, Entry, Label, PhotoImage

class GuiFrame(Frame):
    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.txt_label = Label(self, text="Enter Search item")
        self.input_item_txt = Entry(self)
        self.search = Button(self,
            text="Search",
            fg="green",
            command=self.search_txt)
        
        self.quit = Button(self, 
            text="QUIT", fg="red",
            command=self.master.destroy)


        self.txt_label.grid(row=0,column=0)
        self.input_item_txt.grid(row=0,column=1)
        self.search.grid(row=2,column=1)
        self.quit.grid(row=2,column=0)


    def search_txt(self):
        search_term = self.input_item_txt.get()
        print(search_term)

