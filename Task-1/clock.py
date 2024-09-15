import tkinter as tk
import time


root = tk.Tk()
root.title("Digital Clock")

root.geometry("400x150")


time_label = tk.Label(root, font=('Arial', 48), bg='black', fg='cyan')
time_label.pack(pady=20)

def update_time():
    current_time = time.strftime('%H:%M:%S %p')  
    time_label.config(text=current_time)
    root.after(1000, update_time)  


update_time()


root.mainloop()
