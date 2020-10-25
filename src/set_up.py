
from src.ui_builder import build_gui as bg

def set_up_ui():
    
    root = bg.Tk()
    icon = bg.PhotoImage(file="images/icon.png")
    root.iconphoto(False, icon)
    root.geometry("500x200")
    root.title("web Search")
    app = bg.GuiFrame(master=root)
    app.mainloop()

set_up_ui()
