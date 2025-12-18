import tkinter as tk

# Functions 
def update_display(value):
    if display_var.get() == "0":
        display_var.set(value)
    else:
        display_var.set(display_var.get() + value)

def clear_display():
    display_var.set("0")

def calculate_result():
    try:
        display_var.set(str(eval(display_var.get())))
    except:
        display_var.set("Error")

#  Main TK Window 
root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

#  Display 
display_var = tk.StringVar(value="0")

display = tk.Label(
    root,
    textvariable=display_var,
    font=("Segoe UI", 28),
    bg="#2d2d2d",
    fg="white",
    anchor="e",
    padx=15,
    pady=20
)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button Styles / Colors
btn_font = ("Segoe UI", 16)
btn_bg = "#3a3a3a"
btn_fg = "white"
op_bg = "#ff9500"
eq_bg = "#34c759"
clr_bg = "#ff3b30"

def create_button(text, row, col, bg=btn_bg, cmd=None, colspan=1):
    b = tk.Button(
        root,
        text=text,
        font=btn_font,
        bg=bg,
        fg=btn_fg,
        bd=0,
        activebackground="#555555",
        command=cmd
    )
    b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Buttons Layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3, op_bg),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3, op_bg),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3, op_bg),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2, eq_bg), ("+", 4, 3, op_bg),
]

for btn in buttons:
    text, row, col = btn[:3]
    color = btn[3] if len(btn) > 3 else btn_bg

    if text == "=":
        create_button(text, row, col, color, calculate_result)
    else:
        create_button(text, row, col, color, lambda t=text: update_display(t))

# Clear Button
create_button("C", 5, 0, clr_bg, clear_display, colspan=4)

# Grid Configuration 
for i in range(6):
    root.rowconfigure(i, weight=1)

for j in range(4):
    root.columnconfigure(j, weight=1)

root.mainloop()
