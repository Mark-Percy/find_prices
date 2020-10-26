from tkinter import Tk, Button, Frame, Entry, Label, PhotoImage
from src.main import search
from src.main.data_store import DataStore


class GuiFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.data_store = DataStore()
    
    def create_widgets(self):
        self.txt_label = Label(self, text="Enter Search item")
        self.input_item_txt = Entry(self)
        self.search = Button(self,
            text="Search",
            fg="green",
            command=self.search_web)
        
        self.quit = Button(self, 
            text="QUIT", fg="red",
            command=self.master.destroy)


        self.txt_label.grid(row=0,column=0)
        self.input_item_txt.grid(row=0,column=1)
        self.search.grid(row=2,column=1)
        self.quit.grid(row=2,column=0)

    """
        Event Driven actions
    """
    def search_web(self):
        search.search_web(self.input_item_txt.get())
        self.input_item_txt.delete(0, 'end')
    
    

