import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_box.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_box.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_as():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_box.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


def clear_all():
    txt_box.delete("1.0", tk.END)


window = tk.Tk()
window.title("NotePad")

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.quit)
menu_bar.add_cascade(label='File', menu=file_menu)

edit = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Clear All', command=clear_all)

window.config(menu=menu_bar)

txt_box = tk.Text(window)
txt_box.configure(bg='ghost white', )
txt_box.pack(side='left', fill='both', expand='YES')

window.mainloop()
