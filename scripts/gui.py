from main import *
#from folders import folder
import tkinter as tk
from tkinter import filedialog , messagebox

def browse_folder():
    global user_path
    selected_path = filedialog.askdirectory()
    display_path.delete(0, tk.END)
    display_path.insert(0, selected_path)
    user_path= selected_path



root = tk.Tk()
root.title("Automated File Organizer")
root.geometry("500x250")
root.resizable(False,False)

#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

Welcome_label = tk.Label(root , text="File Organizer Pro Plus" , font=("Arial",16)) 
Welcome_label.grid(row=0, column=0,sticky="n", pady=10 , columnspan=3 ,padx=10)

#Display Entry and browse button
path_frame= tk.Frame(root)
path_frame.grid(row=1, column=0, columnspan=3)

display_path = tk.Entry(path_frame, width= 40, justify="left" ,borderwidth=2 )
display_path.grid(row=1, column=0 , sticky="e" , columnspan=2, padx=10)

button_browse= tk.Button(path_frame, text="Browse",command=browse_folder   , borderwidth=2) 
button_browse.grid(row=1, column= 2 , sticky="w" , columnspan=1 )

#buttons
btn_frame = tk.Frame(root)
btn_frame.grid(row=2 , column=0 , columnspan=3)
button_start = tk.Button(btn_frame, text="Organize" ,command=lambda:[folder(user_path),Main.run_organizer()] , font=("Arial") ,background="light green")
button_start.grid(row=2 , column=0 , padx=0 ,pady=5)

#label
label=tk.Label(btn_frame,text="") .grid(row=2 , column=1)


root.mainloop()