import tkinter as tk 
from tkinter import *

class LMsApp: 
    def __init__(self, root: tk.Tk): 
        self.root = root 
        self.root.title("LMs Main Menu")
        self.root.geometry("1440x900")
        self.root.configure(bg="#800000")
        self.root.resizable(False, False)

        self.login_fram = None
        self.main_frame = None

        self.build_login_screen()

    def build_login_screen(self) -> None:
        #container frame for the login screen
    
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(expand=True, fill="both")

        inner = tk.Frame(self.login_frame, bg="#FFFFFF", padx=60, pady=45, relief="groove", bd=2)
        inner.place(relx=0.5, rely=0.5,anchor="center")

        #header label
        tk.Label(inner, text="Welcome to LMS", bg="#FFFFFF", fg="#800000", font=("Helvetica", 22, "bold"),).grid(row=0, column=0, columnspan=2, pady=(16, 16))

        #Username label and entry
        tk.Label(inner, text="Username:", bg="#FFFFFF", fg="#800000", anchor="e", font=("Helvetica", 12), width=10,).grid(row=1, column=0, sticky="e", pady=6)
        self.username_var = tk.StringVar()
        tk.Entry(inner, textvariable=self.username_var, width=22,).grid(row=1, column=1, sticky="w", padx=(6, 0), pady=6)

        #password mo bajijay
        tk.Label(inner, text="Password:", bg="#FFFFFF", fg="#800000", anchor="e", font=("Helvetica", 12), width=10,).grid(row=2, column=0, sticky="e", pady=6)
        self.password_var = tk.StringVar()
        tk.Entry(inner, textvariable=self.password_var, width=22, show="*").grid(row=2, column=1, sticky="w", padx=(6, 0), pady=6)

        tk.Label(inner, text="Role:", bg="#FFFFFF", fg="#800000", anchor="e", width=10,).grid(row=3, column=0, sticky="e", pady=6)

        self.role_var = tk.StringVar(value="Student")
        role_option = tk.OptionMenu(inner, self.role_var, "Student", "Instructor")
        role_option.config(width=20)
        role_option.grid(row=3, column=1, sticky="w", padx=(6, 0), pady=6)

        tk.Button(inner, text="Login",width=22, bg="#4A90D9", fg="white", font=("Helvetica", 10, "bold"), relief="flat",cursor="hand2",
            command=self.login,).grid(row=4, column=0, columnspan=2, pady=(18, 0))
        
    def login(self) -> None:
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        role     = self.role_var.get()

        if not username or not password or not role:    
            tk.messagebox.showerror("Login Error",
                "All fields are required.\n"
                "Please enter your Username, Password, and select a Role.")
            return
        
        self.login_frame.destroy()
        self.login_frame = None
        self.show_main_menu(role)
    
    def show_main_menu(self, role: str) -> None:
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")

        tk.Label(self.main_frame, text=f"Welcome, {role}!", font=("Helvetica", 14, "bold"),).pack(pady=(0, 14))
        btn_style = dict(width=20, pady=3, font=("Helvetica", 10, "bold"))

        if role == "Student":
            tk.Button(self.main_frame, text="View Courses", command=self.view_courses, **btn_style,).pack(pady=4)
            tk.Button(self.main_frame, text="View Assignments", command=self.view_assignments, **btn_style,).pack(pady=4)
            tk.Button(self.main_frame, text="View Grades", command=self.view_grades, **btn_style,).pack(pady=4)
            tk.Button(self.main_frame, text="Submit Assignments", command=self.submit_assignments, **btn_style,).pack(pady=4)

        elif role == "Instructor":
            tk.Button(self.main_frame, text="Manage Courses", command=self.manage_courses, **btn_style,).pack(pady=4)
            tk.Button(self.main_frame, text="Create Assignments", command=self.create_assignments, **btn_style,).pack(pady=4)
            tk.Button(self.main_frame, text="Grade Submissions", command=self.grade_submissions, **btn_style,).pack(pady=4)
        
        tk.Button(self.main_frame, text="Logout", command=self.logout, width=26, pady=3, bg="#D9534F", fg="white", font=("Helvetica", 10, "bold"), relief="flat", cursor="hand2").pack(pady=(14, 0))

    def logout(self) -> None:
        self.main_frame.destroy()
        self.main_frame = None
        self.build_login_screen()

    def view_courses(self) -> None:
        tk.messagebox.showinfo("View Courses", "Kayo na ata dito jay.")
    def view_assignments(self) -> None:
        tk.messagebox.showinfo("View Assignments", "Kayo na ata dito jay.")
    def view_grades(self) -> None:
        tk.messagebox.showinfo("View Grades", "Kayo na ata dito jay.") 
    def submit_assignments(self) -> None:
        tk.messagebox.showinfo("Submit Assignments", "Kayo na ata dito jay.")
    def manage_courses(self) -> None:
        tk.messagebox.showinfo("Manage Courses", "Kayo na ata dito jay.")
    def create_assignments(self) -> None:
        tk.messagebox.showinfo("Create Assignments", "Kayo na ata dito jay.")
    def grade_submissions(self) -> None:    
        tk.messagebox.showinfo("Grade Submissions", "Kayo na ata dito jay.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LMsApp(root)
    root.mainloop()

    