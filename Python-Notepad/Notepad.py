import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo('Info', "File saved successfully!")

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# ---------------- Buttons ----------------
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, pady=5)

new_btn = tk.Button(button_frame, text="New", command=new_file)
new_btn.pack(side=tk.LEFT, padx=5)

open_btn = tk.Button(button_frame, text="Open", command=open_file)
open_btn.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(button_frame, text="Save", command=save_file)
save_btn.pack(side=tk.LEFT, padx=5)

# ---------------- Text Area ----------------
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="black")
text.pack(expand=tk.YES, fill=tk.BOTH)

# ---------------- Menu ----------------
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label='Option', menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
