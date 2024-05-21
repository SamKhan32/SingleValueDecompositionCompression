from tkinter import *
from tkinter import ttk



def spin(*args):
    print("button pressed")

def main():
    
    root = Tk()
    root.title("Snake's Slots")
    """PhotoImages for labels"""
    slotMachineImage = PhotoImage(file="slotGame//res/slotmachine.png")
    cherryImage = PhotoImage(file="slotGame//res/cherry.png")
    cherryImage = PhotoImage(file="slotGame//res/seven.png")
    barImage = PhotoImage(file="slotGame//res/bar.png")
    spinUnpressed = PhotoImage(file="slotGame\\res\spinUnpressed.png")
    """Widget Creation"""
    frame  = ttk.Frame(root,height=500,width=1500,padding="0.5i") 
    slotMachine = ttk.Label(frame, image=slotMachineImage)
    slot1 = ttk.Label(slotMachine, image = barImage)
    slot2 = ttk.Label(slotMachine, image = barImage)
    slot3 = ttk.Label(slotMachine, image = barImage)
    spinButton = ttk.Button(frame, image = spinUnpressed,command="spin")
    
    """Set Grid layout here"""
    frame.grid(column=0,row=0,sticky="N")
    slotMachine.grid(column=0,row=0,sticky="N")
    slot1.grid(column=0,row=0,sticky="W")
    slot2.grid(column=1,row=0,sticky="W")
    slot3.grid(column=2,row=0,sticky="W")
    spinButton.grid(column=1,row=0,sticky="W")
    """make the padding for loop"""
    children = frame.winfo_children()
    for child in children:
        child.grid_configure(padx=10,pady=10)
    root.mainloop()
main()



