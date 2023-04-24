import tkinter as tk
from tkinter import *


frame = tk.Tk()
frame.title('Bezdione')

window_width = 1000
window_height = 800

# screen dimenisons
screen_width = frame.winfo_screenwidth()
screen_height = frame.winfo_screenheight()

# center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
ButtonStart = tk.Button(frame, text="Start", fg="green",width=30, command=quit)
ButtonStart.place(x=750,y=30)


frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
ButtonExit = tk.Button(frame, text="Exit", fg="red",width=30, command=quit)
ButtonExit.place(x=750,y=90)

frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
ButtonClear = tk.Button(frame, text="Clear the screen",font=('Helvetica 18 bold', 9), fg="red",width=30, command=quit)
ButtonClear.place(x=750,y=60)

label = Label(frame, text='Server info')
label.place(x=350,y=5)

TextContainer = Text(frame, height = 45, width = 90)
TextContainer.pack(side=tk.LEFT)

frame.mainloop()
