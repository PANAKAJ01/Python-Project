import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------- Functions ----------------
def new_file():
    text.delete(1.0, tk.END)
    root.title("Untitled - Text Editor")
    status_bar.config(text="New File Created")

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
        root.title(f"{file_path} - Text Editor")
        status_bar.config(text=f"Opened: {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text.get(1.0, tk.END))
        root.title(f"{file_path} - Text Editor")
        status_bar.config(text=f"Saved: {file_path}")
        messagebox.showinfo("Info", "File saved successfully!")

def cut_text():
    text.event_generate("<<Cut>>")

def copy_text():
    text.event_generate("<<Copy>>")

def paste_text():
    text.event_generate("<<Paste>>")

def undo_action():
    try:
        text.edit_undo()
    except:
        pass

def redo_action():
    try:
        text.edit_redo()
    except:
        pass

def update_status(event=None):
    row, col = text.index(tk.INSERT).split(".")
    status_bar.config(text=f"Line: {row}, Column: {int(col)+1}")

# ---------------- Root Window ----------------
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("900x600")

# ---------------- Menu Bar ----------------
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo_action)
edit_menu.add_command(label="Redo", command=redo_action)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Simple Text Editor\nBuilt with Tkinter"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# ---------------- Text Area with Scrollbar ----------------
text_frame = tk.Frame(root)
text_frame.pack(expand=True, fill=tk.BOTH)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(
    text_frame, wrap=tk.WORD, undo=True, font=("Consolas", 12), fg="black", yscrollcommand=scrollbar.set
)
text.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=text.yview)

# ---------------- Status Bar ----------------
status_bar = tk.Label(root, text="Ready", anchor=tk.W, relief=tk.SUNKEN)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

text.bind("<KeyRelease>", update_status)

root.mainloop()
