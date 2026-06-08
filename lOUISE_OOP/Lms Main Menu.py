import tkinter as tk
from tkinter import messagebox

# Color palette 
MAROON      = "#800000"
DARK_MAROON = "#5C0000"
GOLD        = "#D4AF37"
WHITE       = "#FFFFFF"
LIGHT_BG    = "#F4F4F4"
SIDEBAR_W   = 240       


class LMsApp:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("LMs Main Menu")
        self.root.geometry("1440x900")
        self.root.configure(bg=MAROON)
        self.root.resizable(False, False)

        # Frame references
        self.login_frame   = None  
        self.app_frame     = None   
        self.sidebar_frame = None  
        self.content_frame = None   

        # Tracks which nav button is currently highlighted
        self._nav_buttons = {}

        self.build_login_screen()

    def build_login_screen(self) -> None:
        # Outer frame fills the whole window
        self.login_frame = tk.Frame(self.root, bg=MAROON)
        self.login_frame.pack(expand=True, fill="both")

        # Inner card 
        inner = tk.Frame(self.login_frame, bg=WHITE, padx=60, pady=45,
                         relief="groove", bd=2)
        inner.place(relx=0.5, rely=0.5, anchor="center")

        # Header
        tk.Label(inner, text="Welcome to LMS", bg=WHITE, fg=MAROON, font=("Helvetica", 22, "bold")
                 ).grid(row=0, column=0, columnspan=2, pady=(16, 20))

        # Username
        tk.Label(inner, text="Username:", bg=WHITE, fg=MAROON, anchor="e", font=("Helvetica", 12), width=10
                 ).grid(row=1, column=0, sticky="e", pady=8)
        self.username_var = tk.StringVar()
        tk.Entry(inner, textvariable=self.username_var, width=24, font=("Helvetica", 11)
                 ).grid(row=1, column=1, sticky="w", padx=(8, 0), pady=8)

        # Password
        tk.Label(inner, text="Password:", bg=WHITE, fg=MAROON, anchor="e", font=("Helvetica", 12), width=10
                 ).grid(row=2, column=0, sticky="e", pady=8)
        self.password_var = tk.StringVar()
        tk.Entry(inner, textvariable=self.password_var, show="*", width=24, font=("Helvetica", 11)
                 ).grid(row=2, column=1, sticky="w", padx=(8, 0), pady=8)

        # Role dropdown
        tk.Label(inner, text="Role:", bg=WHITE, fg=MAROON, anchor="e", font=("Helvetica", 12), width=10
                 ).grid(row=3, column=0, sticky="e", pady=8)
        self.role_var = tk.StringVar(value="Student")
        role_opt = tk.OptionMenu(inner, self.role_var, "Student", "Instructor")
        role_opt.config(width=20, font=("Helvetica", 11), bg=WHITE, fg=MAROON, activebackground=MAROON, activeforeground=WHITE, relief="flat")

        role_opt["menu"].config(bg=WHITE, fg=MAROON, font=("Helvetica", 11))
        role_opt.grid(row=3, column=1, sticky="w", padx=(6, 0), pady=8)

        # Login button
        tk.Button(inner, text="Login", width=24, bg=MAROON, fg=GOLD, font=("Helvetica", 11, "bold"), relief="flat", cursor="hand2",activebackground=DARK_MAROON, activeforeground=GOLD, command=self.login
                  ).grid(row=4, column=0, columnspan=2, pady=(22, 4), ipady=6)

    #Login validation
    def login(self) -> None:
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        role     = self.role_var.get()

        if not username or not password or not role:
            messagebox.showerror(
                "Login Error",
                "All fields are required.\n"
                "Please enter your Username, Password, and select a Role.")
            return

        
        self.login_frame.destroy()
        self.login_frame = None
        self.show_main_menu(role)

    # Main menu: sidebar
    def show_main_menu(self, role: str) -> None:
        # Outer container holds both panels
        self.app_frame = tk.Frame(self.root, bg=MAROON)
        self.app_frame.pack(expand=True, fill="both")

        self.sidebar_frame = tk.Frame(self.app_frame,
                                      bg=DARK_MAROON, width=SIDEBAR_W)
        self.sidebar_frame.pack(side="left", fill="y")
        self.sidebar_frame.pack_propagate(False)   # ← keeps the fixed width

        # RIGHT CONTENT AREA 
        self.content_frame = tk.Frame(self.app_frame, bg=LIGHT_BG)
        self.content_frame.pack(side="left", fill="both", expand=True)

        # Build the two panels
        self._build_sidebar(role)
        self._show_dashboard(role)

    # Sidebar builder

    def _build_sidebar(self, role: str) -> None:
        # lms name
        tk.Label(self.sidebar_frame, text="Learning Management System",
                 bg=DARK_MAROON, fg=GOLD,
                 font=("Helvetica", 13, "bold")
                 ).pack(pady=(40, 4))

        tk.Label(self.sidebar_frame, text=f"Logged in as {role}",
                 bg=DARK_MAROON, fg=WHITE,
                 font=("Helvetica", 10)
                 ).pack(pady=(0, 18))

        # divider line
        tk.Frame(self.sidebar_frame, bg=MAROON, height=1
                 ).pack(fill="x", padx=18, pady=(0, 14))

        # Nav button base style
        nav_style = dict(
            bg=DARK_MAROON, fg=WHITE,
            font=("Helvetica", 11),
            relief="flat", bd=0,
            anchor="w", padx=24,
            cursor="hand2",
            activebackground=GOLD,
            activeforeground=MAROON,
        )

        self._nav_buttons = {}

        # Role-specific navigation items
        if role == "Student":
            nav_items = [("View Courses",       self.view_courses), ("View Assignments",   self.view_assignments), ("View Grades",        self.view_grades),
                ("Submit Assignments", self.submit_assignments),]
        else:
            nav_items = [("Manage Courses",    self.manage_courses), ("Create Assignments",self.create_assignments), ("Grade Submissions", self.grade_submissions),]

        for label, cmd in nav_items:
            btn = tk.Button(self.sidebar_frame, text=f"  {label}",
                            command=cmd, **nav_style)
            btn.pack(fill="x", ipady=11, pady=1)
            self._nav_buttons[label] = btn   # store for highlight toggling

        # Logout pinned to bottom 
        tk.Frame(self.sidebar_frame, bg=MAROON, height=1
                 ).pack(side="bottom", fill="x", padx=18, pady=(0, 4))

        tk.Button(self.sidebar_frame, text="  Logout",
                  command=self.logout,
                  bg=MAROON, fg=WHITE,
                  font=("Helvetica", 11, "bold"),
                  relief="flat", bd=0,
                  anchor="w", padx=24, cursor="hand2",
                  activebackground="#D9534F", activeforeground=WHITE,
                  ).pack(side="bottom", fill="x", ipady=11, pady=(0, 8))

    def _set_active(self, key: str) -> None:
        for name, btn in self._nav_buttons.items():
            if name == key:
                btn.config(bg=GOLD, fg=MAROON)      
            else:
                btn.config(bg=DARK_MAROON, fg=WHITE)  

    # Content area helpers
    def _show_dashboard(self, role: str) -> None:
        """Welcome screen shown immediately after login."""
        self._clear_content()

        self._content_header(f"Welcome, bopols na {role}!")

        body = tk.Frame(self.content_frame, bg=LIGHT_BG)
        body.pack(fill="both", expand=True)
        tk.Label(body,
                 text="Select a menu item from the sidebar to get started.",
                 bg=LIGHT_BG, fg="#888888", font=("Helvetica", 13)
                 ).place(relx=0.5, rely=0.5, anchor="center")

    def _show_content(self, title: str) -> None:
        self._clear_content()
        self._content_header(title)

        body = tk.Frame(self.content_frame, bg=LIGHT_BG)
        body.pack(fill="both", expand=True)
        tk.Label(body, text="Kayo na ata dito jay.",
                 bg=LIGHT_BG, fg="#888888", font=("Helvetica", 14)
                 ).place(relx=0.5, rely=0.5, anchor="center")

    def _content_header(self, title: str) -> None:
        """Top header bar with page title and a bottom border."""
        bar = tk.Frame(self.content_frame, bg=WHITE, height=72)
        bar.pack(fill="x")
        bar.pack_propagate(False)
        tk.Label(bar, text=title, bg=WHITE, fg=MAROON,
                 font=("Helvetica", 18, "bold")
                 ).pack(side="left", padx=32, pady=0)
        tk.Frame(bar, bg="#E0E0E0", height=1).pack(side="bottom", fill="x")

    def _clear_content(self) -> None:
        """Destroy all widgets in the content area before redrawing."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    
    # Logout

    def logout(self) -> None:
        self.app_frame.destroy()
        self.app_frame = None
        self.build_login_screen()
   
    # Features
    def view_courses(self):
        self._set_active("View Courses")
        self._show_content("View Courses")

    def view_assignments(self):
        self._set_active("View Assignments")
        self._show_content("View Assignments")

    def view_grades(self):
        self._set_active("View Grades")
        self._show_content("View Grades")

    def submit_assignments(self):
        self._set_active("Submit Assignments")
        self._show_content("Submit Assignments")

    def manage_courses(self):
        self._set_active("Manage Courses")
        self._show_content("Manage Courses")

    def create_assignments(self):
        self._set_active("Create Assignments")
        self._show_content("Create Assignments")

    def grade_submissions(self):
        self._set_active("Grade Submissions")
        self._show_content("Grade Submissions")

if __name__ == "__main__":
    root = tk.Tk()
    app = LMsApp(root)
    root.mainloop()