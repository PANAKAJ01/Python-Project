from tkinter import *
from time import strftime
import datetime
root = Tk()
root.title("Digital Clock with Date")
def time_date():
    
    current_time = strftime('%H:%M:%S %p')  # 12-hour format
    time_label.config(text=current_time)
    
    today = datetime.date.today()
    date_label.config(text=today.strftime("%A, %d %B %Y"))      
    # Update every 1000ms (1 second)
    time_label.after(1000, time_date)

time_label = Label(root, font=('Arial', 50, 'bold'), background='black', foreground='cyan')
time_label.pack(anchor='center', pady=10)

date_label = Label(root, font=('Arial', 25), background='black', foreground='white')
date_label.pack(anchor='center')

time_date()
root.mainloop()


