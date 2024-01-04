import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap.constants import *

window= ()
lebar=500
tinggi=400
x =500
y =100

screenwidth =window.winfo_screenwidth()
screenhight =window.winfo_screenhight()

newx = int((screenwidth/2) - (lebar/2))
newy = int((screenhight/2) - (tinggi/2)-100)

window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")

window.mainloop()

root = ttk.Window(themename="darkly")

def open_dialog():
    app = ttk.Toplevel(title="My Toplevel")
    app.mainloop()

open_button = ttk.Button(root, text="Open", 
                         command=open_dialog, bootstyle=SUCCESS)
open_button.pack(side=LEFT, padx=5, pady=10)

exit_button = ttk.Button(root, text="Exit", 
                         command=open_dialog, bootstyle=(INFO, OUTLINE))
exit_button.pack(side=LEFT, padx=5, pady=10)

root.mainloop()


