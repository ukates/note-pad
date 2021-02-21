import tkinter as tk
from functools import partial
from tkinter.filedialog import askopenfilename, asksaveasfilename


# function to open a file
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


# function to safe file as .txt
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


# clear all text
def clear_all():
    txt_box.delete("1.0", tk.END)


# will change bg color of text box, font, and cursor depending on choice
def change_bg_color(color):
    txt_box.config(bg=color)
    if color == 'white':
        txt_box.config(foreground='black', cursor='plus black')
    else:
        txt_box.config(foreground='white', cursor='plus white')


# change font color
def change_font_color(color):
    txt_box.config(foreground=color)


# create window
window = tk.Tk()
window.title("NotePad")
# create text box and configure with base color and font
txt_box = tk.Text(window)
txt_box.configure(bg='slate gray', font='ariel 12', foreground='ghost white', insertbackground='ghost white',
                  cursor='plus black')
# place txt box widget and allow to be resized with window
txt_box.pack(side='left', fill='both', expand='YES')
# create menu bar from top
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.quit)
menu_bar.add_cascade(label='File', menu=file_menu)
# create edit tab on menu
edit = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Clear All', command=clear_all)
# create sub menu for bg color
bg_submenu = tk.Menu(edit)
bg_submenu.add_command(label="White", command=partial(change_bg_color, 'white'))
bg_submenu.add_command(label="Slate Gray", command=partial(change_bg_color, 'slate gray'))
bg_submenu.add_command(label="Black", command=partial(change_bg_color, 'black'))
edit.add_cascade(label='BG Color', menu=bg_submenu, underline=0)
# create sub menu for font color
font_submenu = tk.Menu(edit)
font_submenu.add_command(label="White", command=partial(change_font_color, 'white'))
font_submenu.add_command(label="Black", command=partial(change_font_color, 'black'))
font_submenu.add_command(label="Red", command=partial(change_font_color, 'red'))
edit.add_cascade(label='Font Color', menu=font_submenu, underline=0)
# add menu to window
window.config(menu=menu_bar)
# main loop to create window object
window.mainloop()
