import tkinter as tk
from tkinter import ttk, messagebox

# =========================
# Color Palette
# =========================
MAROON      = "#800000"
DARK_MAROON = "#5C0000"
GOLD        = "#D4AF37"
WHITE       = "#FFFFFF"
LIGHT_BG    = "#F4F4F4"
SIDEBAR_W   = 240

# =========================
# Main Window
# =========================
root = tk.Tk()
root.title("Course Management")
root.geometry("1100x650")
root.configure(bg=LIGHT_BG)

# =========================
# Sidebar
# =========================
sidebar = tk.Frame(root, bg=MAROON, width=SIDEBAR_W)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

title_lbl = tk.Label(
    sidebar,
    text="LMS",
    font=("Segoe UI", 22, "bold"),
    bg=MAROON,
    fg=GOLD
)
title_lbl.pack(pady=30)

menu_btn = tk.Button(
    sidebar,
    text="Course Menu",
    bg=DARK_MAROON,
    fg=WHITE,
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padx=20,
    pady=10
)
menu_btn.pack(fill="x", padx=15, pady=5)

# =========================
# Main Content
# =========================
content = tk.Frame(root, bg=LIGHT_BG)
content.pack(fill="both", expand=True)

header = tk.Label(
    content,
    text="Course Management",
    bg=LIGHT_BG,
    fg=MAROON,
    font=("Segoe UI", 24, "bold")
)
header.pack(pady=20)

# =========================
# Form Frame
# =========================
form_frame = tk.Frame(content, bg=WHITE)
form_frame.pack(fill="x", padx=20, pady=10)

# Course Code
tk.Label(
    form_frame,
    text="Course Code",
    bg=WHITE,
    font=("Segoe UI", 11)
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

course_code = ttk.Entry(form_frame, width=35)
course_code.grid(row=0, column=1, padx=10, pady=10)

# Course Name
tk.Label(
    form_frame,
    text="Course Name",
    bg=WHITE,
    font=("Segoe UI", 11)
).grid(row=1, column=0, padx=10, pady=10, sticky="w")

course_name = ttk.Entry(form_frame, width=35)
course_name.grid(row=1, column=1, padx=10, pady=10)

# Instructor
tk.Label(
    form_frame,
    text="Instructor",
    bg=WHITE,
    font=("Segoe UI", 11)
).grid(row=2, column=0, padx=10, pady=10, sticky="w")

instructor = ttk.Entry(form_frame, width=35)
instructor.grid(row=2, column=1, padx=10, pady=10)

# =========================
# Course Table
# =========================
table_frame = tk.Frame(content, bg=WHITE)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = ("Code", "Course Name", "Instructor")

course_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)

for col in columns:
    course_table.heading(col, text=col)
    course_table.column(col, anchor="center")

course_table.pack(fill="both", expand=True, padx=10, pady=10)

# =========================
# Functions
# =========================
def add_course():
    code = course_code.get()
    name = course_name.get()
    prof = instructor.get()

    if not code or not name or not prof:
        messagebox.showwarning(
            "Missing Information",
            "Please complete all fields."
        )
        return

    course_table.insert(
        "",
        "end",
        values=(code, name, prof)
    )

    course_code.delete(0, tk.END)
    course_name.delete(0, tk.END)
    instructor.delete(0, tk.END)

def delete_course():
    selected = course_table.selection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Select a course first."
        )
        return

    course_table.delete(selected)

# =========================
# Buttons
# =========================
btn_frame = tk.Frame(content, bg=LIGHT_BG)
btn_frame.pack(pady=10)

add_btn = tk.Button(
    btn_frame,
    text="Add Course",
    bg=MAROON,
    fg=WHITE,
    font=("Segoe UI", 11, "bold"),
    width=15,
    command=add_course
)
add_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(
    btn_frame,
    text="Delete Course",
    bg=GOLD,
    fg="black",
    font=("Segoe UI", 11, "bold"),
    width=15,
    command=delete_course
)
delete_btn.grid(row=0, column=1, padx=10)

root.mainloop()