import tkinter as tk
import random
def dice():
    x=random.randint(1,6)
    label["text"]=f"{x}"
    
window = tk.Tk()
button=tk.Button(master=window,text="ROLL",command=dice)
button.pack()
label = tk.Label(master=window,text=" ")
label.pack()


window.mainloop()
