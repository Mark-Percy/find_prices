
from src.ui_builder import build_gui as bg


class SetUp:
    def __init__(self):
        self.gui = self.set_up_ui()
        

    def set_up_ui(self):
        
        root = bg.Tk()
        icon = bg.PhotoImage(file="images/icon.png")
        root.iconphoto(False, icon)
        root.geometry("500x200")
        root.title("web Search")
        app = bg.GuiFrame(master=root)
        app.mainloop()
        return app
