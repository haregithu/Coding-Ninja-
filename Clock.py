import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")

clock_lable = tk.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
clock_lable.pack(anchor="center", fill= "both", expand="True")

def update_time():
    current_time = strftime("%H:%M:%S")
    clock_lable.config(text=current_time)
    clock_lable.after(1000, update_time)

update_time()
root.mainloop()    
