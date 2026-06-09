import tkinter as tk
from tkinter import ttk, font


BG_DARK      = "#F5EFE6"   
BG_CARD      = "#FAF6F0"  
BG_CARD2     = "#EDE5D8"   
MAROON       = "#714329"   
MAROON_DEEP  = "#4A2A18"   
MAROON_LIGHT = "#B08463"   
GOLD         = "#714329"   
GOLD_DARK    = "#4A2A18"
GOLD_PALE    = "#FAF6F0"
GOLD_SUBTLE  = "#B9937B"
WHITE        = "#FAF6F0"
GRAY         = "#A08878"
GRAY_LIGHT   = "#7A6050"
BORDER       = "#D0B9A7"
BORDER_GOLD  = "#B08463"

# Text colors
TEXT_DARK    = "#3A2010"  
TEXT_MID     = "#714329"   
TEXT_LIGHT   = "#B9937B"   
ACCENT       = "#714329"   
ACCENT2      = "#B08463"   
CHIP_BG      = "#D0B9A7"   
CHIP_FG      = "#4A2A18"
STATUS_OPEN_BG  = "#714329"
STATUS_OPEN_FG  = "#FAF6F0"
STATUS_FULL_BG  = "#D0B9A7"
STATUS_FULL_FG  = "#7A6050"
BTN_BG       = "#714329"
BTN_FG       = "#FAF6F0"
BTN_HOV      = "#4A2A18"
NAV_BG       = "#3A2010"
NAV_FG       = "#D0B9A7"
NAV_ACTIVE_BG = "#714329"
NAV_ACTIVE_FG = "#FAF6F0"
BAR_FILL     = "#B08463"
BAR_WARN     = "#714329"
BAR_BG       = "#D0B9A7"


COURSES = [
    {
        "code": "CMPE 103",
        "title": "Object Oriented Programming",
        "instructor": "Avena, Godofredo",
        "schedule": "TH/TH  7:30AM-10:30AM / 10:30AM-1:30PM",
        "units": 2,
        "lec": 0.0,
        "lab": 6.0,
        "enrolled": 38,
        "capacity": 45,
        "status": "Open",
        "category": "Engineering Core",
        "description": "Object-oriented programming concepts: classes, objects, inheritance, polymorphism, and encapsulation.",
    },
    {
        "code": "CMPE 104",
        "title": "Discrete Mathematics",
        "instructor": "Lacatan, Luisito",
        "schedule": "F/F  7:30AM-9:00AM / 9:00AM-10:30AM",
        "units": 3,
        "lec": 3.0,
        "lab": 0.0,
        "enrolled": 40,
        "capacity": 45,
        "status": "Open",
        "category": "Mathematics & Sciences",
        "description": "Logic, set theory, combinatorics, graph theory, Boolean algebra, and mathematical proofs for engineers.",
    },
    {
        "code": "CMPE 105",
        "title": "Computer Hardware Fundamentals",
        "instructor": "Avila, John Paul",
        "schedule": "M/S  6:00PM-9:00PM / 2:00PM-5:00PM",
        "units": 2,
        "lec": 0.0,
        "lab": 6.0,
        "enrolled": 35,
        "capacity": 40,
        "status": "Open",
        "category": "Engineering Core",
        "description": "Computer components, motherboards, processors, memory systems, storage devices, and hardware troubleshooting.",
    },
    {
        "code": "CWTS 002",
        "title": "Civic Welfare Training Service 2",
        "instructor": "Rodriguez, Arnold",
        "schedule": "SUN/SUN  8:00AM-12:00PM / 1:00PM-6:00PM",
        "units": 3,
        "lec": 3.0,
        "lab": 0.0,
        "enrolled": 45,
        "capacity": 45,
        "status": "Full",
        "category": "General Education",
        "description": "Community service, civic responsibility, and social awareness through organized welfare programs.",
    },
    {
        "code": "GEED 005",
        "title": "Purposive Communication / Malayuning Komunikasyon",
        "instructor": "Caguia, Christopher Armand",
        "schedule": "M  1:30PM-4:30PM",
        "units": 3,
        "lec": 3.0,
        "lab": 0.0,
        "enrolled": 42,
        "capacity": 45,
        "status": "Open",
        "category": "General Education",
        "description": "Academic and professional communication, multimodal texts, and purposive writing for diverse audiences.",
    },
    {
        "code": "MATH 103",
        "title": "Calculus 2",
        "instructor": "Costales, Jeffrey",
        "schedule": "T  10:30AM-1:30PM",
        "units": 3,
        "lec": 3.0,
        "lab": 0.0,
        "enrolled": 38,
        "capacity": 45,
        "status": "Open",
        "category": "Mathematics & Sciences",
        "description": "Integral calculus, techniques of integration, applications of definite integrals, and infinite series.",
    },
    {
        "code": "PATHFIT 2",
        "title": "Physical Activity Towards Health and Fitness 2",
        "instructor": "De la Cruz, Wes",
        "schedule": "T  2:00PM-4:00PM",
        "units": 2,
        "lec": 2.0,
        "lab": 0.0,
        "enrolled": 44,
        "capacity": 45,
        "status": "Open",
        "category": "General Education",
        "description": "Health-related fitness activities, physical wellness, and lifestyle management for college students.",
    },
    {
        "code": "PHYS 013",
        "title": "Physics for Engineers (Calculus-based)",
        "instructor": "Bisa, Elizabeth",
        "schedule": "S/S  7:30AM-10:30AM / 10:30AM-1:30PM",
        "units": 4,
        "lec": 3.0,
        "lab": 0.0,
        "enrolled": 40,
        "capacity": 45,
        "status": "Open",
        "category": "Mathematics & Sciences",
        "description": "Mechanics, thermodynamics, waves, and optics using calculus-based approaches for engineering students.",
    },
    {
        "code": "STAT 012",
        "title": "Engineering Data Analysis",
        "instructor": "Bengo, Manuelito",
        "schedule": "F  10:30AM-1:30PM",
        "units": 3,
        "lec": 3.0,
        "lab": 0.0,
        "enrolled": 36,
        "capacity": 45,
        "status": "Open",
        "category": "Mathematics & Sciences",
        "description": "Probability, descriptive and inferential statistics, regression analysis, and data interpretation for engineers.",
    },
]

CATEGORIES = ["All Categories", "Engineering Core", "Mathematics & Sciences", "General Education"]


class LMSCourseBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PUP LMS — Course Catalog")
        self.geometry("1140x760")
        self.minsize(900, 620)
        self.configure(bg=BG_DARK)
        self.resizable(True, True)

        self._setup_fonts()
        self._build_ui()
        self._render_cards(COURSES)

    def _setup_fonts(self):
        self.fn_brand    = font.Font(family="Palatino Linotype", size=16, weight="bold")
        self.fn_subbrand = font.Font(family="Trebuchet MS",      size=8,  weight="bold")
        self.fn_heading  = font.Font(family="Palatino Linotype", size=20, weight="bold")
        self.fn_subhead  = font.Font(family="Palatino Linotype", size=13, weight="bold")
        self.fn_label    = font.Font(family="Trebuchet MS",      size=8,  weight="bold")
        self.fn_body     = font.Font(family="Trebuchet MS",      size=9)
        self.fn_code     = font.Font(family="Trebuchet MS",      size=11, weight="bold")
        self.fn_tiny     = font.Font(family="Trebuchet MS",      size=8)
        self.fn_btn      = font.Font(family="Trebuchet MS",      size=9,  weight="bold")
        self.fn_title    = font.Font(family="Palatino Linotype", size=11, weight="bold")
        self.fn_nav      = font.Font(family="Trebuchet MS",      size=9)

    def _build_navbar(self, parent):
        nav_wrap = tk.Frame(parent, bg=BORDER, pady=0)
        nav_wrap.pack(fill="x")

        nav = tk.Frame(nav_wrap, bg=NAV_BG, height=68)
        nav.pack(fill="x", pady=(0, 1))
        nav.pack_propagate(False)

        # Left warm-tan accent bar
        tk.Frame(nav, bg=ACCENT2, width=5).pack(side="left", fill="y")

        # Logo circle
        logo_canvas = tk.Canvas(nav, width=46, height=46,
                                bg=NAV_BG, highlightthickness=0)
        logo_canvas.pack(side="left", padx=(12, 8), pady=10)
        logo_canvas.create_oval(2, 2, 44, 44, outline=ACCENT2, width=2, fill=MAROON)
        logo_canvas.create_text(23, 23, text="PUP", fill=GOLD_PALE,
                                font=("Trebuchet MS", 9, "bold"))

        # Brand text
        brand_frame = tk.Frame(nav, bg=NAV_BG)
        brand_frame.pack(side="left", pady=10)

        tk.Label(brand_frame,
                 text="Polytechnic University of the Philippines",
                 font=self.fn_brand, bg=NAV_BG, fg=GOLD_PALE).pack(anchor="w")
        tk.Label(brand_frame,
                 text="LEARNING MANAGEMENT SYSTEM  •  COURSE CATALOG",
                 font=self.fn_subbrand, bg=NAV_BG, fg=ACCENT2).pack(anchor="w")

        # Nav links
        links_frame = tk.Frame(nav, bg=NAV_BG)
        links_frame.pack(side="right", padx=16)

        for label in ("Dashboard", "My Courses", "Schedule", "Grades"):
            btn = tk.Label(links_frame, text=label, font=self.fn_nav,
                           bg=NAV_BG, fg=NAV_FG,
                           padx=12, pady=22, cursor="hand2")
            btn.pack(side="left")
            btn.bind("<Enter>", lambda e, b=btn: b.config(fg=GOLD_PALE, bg=MAROON))
            btn.bind("<Leave>", lambda e, b=btn: b.config(fg=NAV_FG, bg=NAV_BG))

        active = tk.Label(links_frame, text="Courses", font=self.fn_btn,
                          bg=NAV_ACTIVE_BG, fg=NAV_ACTIVE_FG,
                          padx=14, pady=22, cursor="hand2")
        active.pack(side="left")

    def _build_header(self, parent):
        hdr = tk.Frame(parent, bg=BG_DARK, pady=22)
        hdr.pack(fill="x", padx=32)

        left = tk.Frame(hdr, bg=BG_DARK)
        left.pack(side="left")

        accent_row = tk.Frame(left, bg=BG_DARK)
        accent_row.pack(anchor="w")

        tk.Frame(accent_row, bg=ACCENT, width=4, height=52).pack(side="left")
        title_block = tk.Frame(accent_row, bg=BG_DARK, padx=12)
        title_block.pack(side="left")

        tk.Label(title_block, text="Available Courses",
                 font=self.fn_heading, bg=BG_DARK, fg=TEXT_DARK).pack(anchor="w")
        self.subtitle_var = tk.StringVar(value=f"Showing {len(COURSES)} courses this semester")
        tk.Label(title_block, textvariable=self.subtitle_var,
                 font=self.fn_body, bg=BG_DARK, fg=TEXT_LIGHT).pack(anchor="w")

        #  Semester badge
        badge_wrap = tk.Frame(hdr, bg=BORDER, padx=1, pady=1)
        badge_wrap.pack(side="right", anchor="center")
        tk.Label(badge_wrap,
                 text="  2nd Semester  \n  AY 2025–2026  ",
                 font=self.fn_label, bg=BG_CARD, fg=TEXT_MID,
                 padx=14, pady=8, justify="center").pack()

    def _build_toolbar(self, parent):
        bar = tk.Frame(parent, bg=BG_CARD2, pady=10)
        bar.pack(fill="x")

        # Thin top/bottom border lines
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

        inner = tk.Frame(bar, bg=BG_CARD2)
        inner.pack(padx=32)

        # Search box
        search_border = tk.Frame(inner, bg=BORDER, padx=1, pady=1)
        search_border.pack(side="left")

        search_bg = tk.Frame(search_border, bg=BG_CARD)
        search_bg.pack()

        tk.Label(search_bg, text="  🔍", font=self.fn_body,
                 bg=BG_CARD, fg=TEXT_MID).pack(side="left")

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self._on_filter_change)
        search_entry = tk.Entry(search_bg, textvariable=self.search_var,
                                bg=BG_CARD, fg=TEXT_DARK, insertbackground=ACCENT,
                                relief="flat", font=self.fn_body, width=30)
        search_entry.pack(side="left", ipady=8, padx=(0, 12))
        search_entry.insert(0, "Search by title, code, or instructor…")
        search_entry.config(fg=TEXT_LIGHT)

        def on_focus_in(e):
            if search_entry.get() == "Search by title, code, or instructor…":
                search_entry.delete(0, "end")
                search_entry.config(fg=TEXT_DARK)

        def on_focus_out(e):
            if not search_entry.get():
                search_entry.insert(0, "Search by title, code, or instructor…")
                search_entry.config(fg=TEXT_LIGHT)

        search_entry.bind("<FocusIn>", on_focus_in)
        search_entry.bind("<FocusOut>", on_focus_out)

        tk.Frame(inner, bg=BORDER, width=1, height=36).pack(side="left", padx=14)

        tk.Label(inner, text="CATEGORY", font=self.fn_label,
                 bg=BG_CARD2, fg=TEXT_LIGHT).pack(side="left", padx=(0, 6))

        self.category_var = tk.StringVar(value="All Categories")
        self.category_var.trace_add("write", self._on_filter_change)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Earth.TCombobox",
                        fieldbackground=BG_CARD, background=MAROON,
                        foreground=TEXT_DARK, arrowcolor=ACCENT,
                        selectbackground=CHIP_BG, selectforeground=CHIP_FG,
                        padding=6, font=("Trebuchet MS", 9))
        style.map("Earth.TCombobox",
                  fieldbackground=[("readonly", BG_CARD)],
                  foreground=[("readonly", TEXT_DARK)])

        cat_combo = ttk.Combobox(inner, textvariable=self.category_var,
                                  values=CATEGORIES, state="readonly",
                                  width=22, style="Earth.TCombobox")
        cat_combo.pack(side="left")

        tk.Frame(inner, bg=BORDER, width=1, height=36).pack(side="left", padx=14)

        self.show_open_only = tk.BooleanVar(value=False)
        self.show_open_only.trace_add("write", self._on_filter_change)

        style.configure("Earth.TCheckbutton",
                        background=BG_CARD2, foreground=TEXT_MID,
                        focuscolor=BG_CARD2)
        style.map("Earth.TCheckbutton",
                  background=[("active", BG_CARD2)],
                  foreground=[("active", ACCENT)])

        ttk.Checkbutton(inner, text="Open Only",
                        variable=self.show_open_only,
                        style="Earth.TCheckbutton").pack(side="left")

        self.count_var = tk.StringVar(value=f"{len(COURSES)} courses")
        tk.Label(inner, textvariable=self.count_var,
                 font=self.fn_label, bg=ACCENT, fg=GOLD_PALE,
                 padx=10, pady=5).pack(side="right")

        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

    def _build_card_area(self, parent):
        wrapper = tk.Frame(parent, bg=BG_DARK)
        wrapper.pack(fill="both", expand=True, padx=24, pady=(14, 8))

        self.canvas = tk.Canvas(wrapper, bg=BG_DARK, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        sb_style = ttk.Style()
        sb_style.configure("Earth.Vertical.TScrollbar",
                            troughcolor=BG_DARK, background=ACCENT2,
                            arrowcolor=MAROON, bordercolor=BG_DARK,
                            lightcolor=BORDER, darkcolor=MAROON_LIGHT)

        scrollbar = ttk.Scrollbar(wrapper, orient="vertical",
                                   command=self.canvas.yview,
                                   style="Earth.Vertical.TScrollbar")
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.card_frame = tk.Frame(self.canvas, bg=BG_DARK)
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.card_frame, anchor="nw")

        self.card_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _build_footer(self, parent):
        footer_wrap = tk.Frame(parent, bg=BORDER, pady=0)
        footer_wrap.pack(fill="x", side="bottom")

        footer = tk.Frame(footer_wrap, bg=NAV_BG, height=32)
        footer.pack(fill="x", pady=(1, 0))
        footer.pack_propagate(False)

        tk.Label(footer,
                 text="© 2026  Polytechnic University of the Philippines  •  Registrar's Office  •  All Rights Reserved",
                 font=self.fn_tiny, bg=NAV_BG, fg=ACCENT2).pack(expand=True)

    def _build_ui(self):
        self._build_navbar(self)
        self._build_header(self)
        self._build_toolbar(self)
        self._build_card_area(self)
        self._build_footer(self)

    def _make_card(self, parent, course, col, row):
        CARD_W = 320
        PAD    = 10

        outer = tk.Frame(parent, bg=BORDER, padx=1, pady=1)
        outer.grid(row=row, column=col, padx=PAD, pady=PAD, sticky="nsew")

        card = tk.Frame(outer, bg=BG_CARD, padx=18, pady=14)
        card.pack(fill="both", expand=True)

        # Warm brown top accent
        tk.Frame(card, bg=ACCENT, height=3).pack(fill="x", pady=(0, 12))

        # Header row
        top_row = tk.Frame(card, bg=BG_CARD)
        top_row.pack(fill="x")

        tk.Label(top_row, text=course["code"],
                 font=self.fn_code, bg=BG_CARD, fg=ACCENT).pack(side="left")

        status_bg = STATUS_OPEN_BG if course["status"] == "Open" else STATUS_FULL_BG
        status_fg = STATUS_OPEN_FG if course["status"] == "Open" else STATUS_FULL_FG
        tk.Label(top_row, text=f"  {course['status'].upper()}  ",
                 font=self.fn_label, bg=status_bg, fg=status_fg,
                 padx=4, pady=3).pack(side="right")

        # Title
        tk.Label(card, text=course["title"],
                 font=self.fn_title, bg=BG_CARD, fg=TEXT_DARK,
                 wraplength=CARD_W - 36, justify="left").pack(anchor="w", pady=(8, 3))

        # Category chip
        tk.Label(card, text=f"  {course['category']}  ",
                 font=self.fn_tiny, bg=CHIP_BG, fg=CHIP_FG,
                 pady=3).pack(anchor="w", pady=(0, 10))

        # Divider
        tk.Frame(card, bg=BORDER, height=1).pack(fill="x", pady=(0, 8))

        # Info rows
        def info_row(icon, label, value):
            f = tk.Frame(card, bg=BG_CARD)
            f.pack(fill="x", pady=3)
            tk.Label(f, text=icon, font=self.fn_tiny,
                     bg=BG_CARD, fg=ACCENT2, width=2).pack(side="left")
            tk.Label(f, text=f"{label}  ", font=self.fn_label,
                     bg=BG_CARD, fg=TEXT_LIGHT).pack(side="left")
            tk.Label(f, text=value, font=self.fn_body,
                     bg=BG_CARD, fg=TEXT_MID).pack(side="left")

        info_row("▸", "Instructor", course["instructor"])
        info_row("◷", "Schedule",   course["schedule"])

        # Lec / Lab / Units row
        llu_f = tk.Frame(card, bg=BG_CARD)
        llu_f.pack(fill="x", pady=3)
        for lbl, val in [("LEC", str(course["lec"])), ("LAB", str(course["lab"])), ("UNITS", str(course["units"]))]:
            box = tk.Frame(llu_f, bg=CHIP_BG, padx=8, pady=4)
            box.pack(side="left", padx=(0, 6))
            tk.Label(box, text=lbl, font=self.fn_label, bg=CHIP_BG, fg=TEXT_LIGHT).pack()
            tk.Label(box, text=val, font=self.fn_code,  bg=CHIP_BG, fg=TEXT_DARK).pack()

        # Enrollment bar
        enroll_f = tk.Frame(card, bg=BG_CARD)
        enroll_f.pack(fill="x", pady=(10, 4))

        pct = course["enrolled"] / course["capacity"]
        bar_color = BAR_FILL if pct < 0.85 else BAR_WARN

        tk.Label(enroll_f, text="ENROLLMENT",
                 font=self.fn_label, bg=BG_CARD, fg=TEXT_LIGHT).pack(anchor="w")

        bar_canvas = tk.Canvas(enroll_f, bg=BAR_BG, height=7, highlightthickness=0)
        bar_canvas.pack(fill="x", pady=(4, 2))

        def draw_bar(event, c=bar_canvas, p=pct, bc=bar_color):
            w = c.winfo_width()
            c.delete("all")
            c.create_rectangle(0, 0, int(w * p), 7, fill=bc, outline="")

        bar_canvas.bind("<Configure>", draw_bar)

        tk.Label(enroll_f,
                 text=f"{course['enrolled']} / {course['capacity']} enrolled",
                 font=self.fn_tiny, bg=BG_CARD, fg=TEXT_LIGHT).pack(anchor="e")

        # Description
        tk.Label(card, text=course["description"],
                 font=self.fn_tiny, bg=BG_CARD, fg=GRAY_LIGHT,
                 wraplength=CARD_W - 36, justify="left").pack(anchor="w", pady=(8, 12))

        # Enroll button
        can_enroll = course["status"] == "Open"
        b_bg  = BTN_BG  if can_enroll else CHIP_BG
        b_fg  = BTN_FG  if can_enroll else GRAY
        b_txt = "Enroll Now  →" if can_enroll else "Course Full"

        btn = tk.Label(card, text=b_txt, font=self.fn_btn,
                       bg=b_bg, fg=b_fg, pady=9,
                       cursor="hand2" if can_enroll else "arrow")
        btn.pack(fill="x")

        if can_enroll:
            btn.bind("<Enter>",    lambda e, b=btn: b.config(bg=BTN_HOV))
            btn.bind("<Leave>",    lambda e, b=btn: b.config(bg=BTN_BG))
            btn.bind("<Button-1>", lambda e, c=course: self._enroll(c))

        # Card hover
        def card_enter(e, o=outer): o.config(bg=ACCENT)
        def card_leave(e, o=outer): o.config(bg=BORDER)
        for w in [card, outer, top_row]:
            w.bind("<Enter>", card_enter)
            w.bind("<Leave>", card_leave)

    def _render_cards(self, courses):
        for w in self.card_frame.winfo_children():
            w.destroy()

        COLS = 3
        for i, course in enumerate(courses):
            col = i % COLS
            row = i // COLS
            self._make_card(self.card_frame, course, col, row)
            self.card_frame.columnconfigure(col, weight=1)

        if not courses:
            tk.Label(self.card_frame,
                     text="No courses match your search.",
                     font=self.fn_subhead, bg=BG_DARK, fg=GRAY,
                     pady=80).grid(row=0, column=0, columnspan=COLS, sticky="nsew")

        self.count_var.set(f"{len(courses)} course{'s' if len(courses) != 1 else ''}")
        self.subtitle_var.set(
            f"Showing {len(courses)} course{'s' if len(courses) != 1 else ''} this semester")

        self.card_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.yview_moveto(0)

    def _on_filter_change(self, *args):
        raw = self.search_var.get().strip().lower()
        query = "" if raw == "search by title, code, or instructor…" else raw
        category  = self.category_var.get()
        open_only = self.show_open_only.get()

        filtered = [
            c for c in COURSES
            if (query in c["title"].lower()
                or query in c["instructor"].lower()
                or query in c["code"].lower()
                or query in c["description"].lower())
            and (category == "All Categories" or c["category"] == category)
            and (not open_only or c["status"] == "Open")
        ]
        self._render_cards(filtered)

    def _enroll(self, course):
        popup = tk.Toplevel(self)
        popup.title("Enrollment Confirmation")
        popup.geometry("440x280")
        popup.configure(bg=BG_CARD)
        popup.resizable(False, False)
        popup.grab_set()

        tk.Frame(popup, bg=ACCENT, height=4).pack(fill="x")

        tk.Label(popup, text="Confirm Enrollment",
                 font=self.fn_subhead, bg=BG_CARD, fg=TEXT_DARK).pack(pady=(20, 6))
        tk.Label(popup, text=f"{course['code']}  —  {course['title']}",
                 font=self.fn_btn, bg=BG_CARD, fg=TEXT_MID,
                 wraplength=380).pack()
        tk.Label(popup, text=f"Instructor:  {course['instructor']}",
                 font=self.fn_body, bg=BG_CARD, fg=TEXT_LIGHT).pack(pady=2)
        tk.Label(popup, text=f"Schedule:  {course['schedule']}",
                 font=self.fn_body, bg=BG_CARD, fg=TEXT_LIGHT).pack()

        tk.Frame(popup, bg=BORDER, height=1).pack(fill="x", padx=32, pady=16)

        btn_row = tk.Frame(popup, bg=BG_CARD)
        btn_row.pack()

        cancel = tk.Label(btn_row, text="  Cancel  ", font=self.fn_btn,
                          bg=CHIP_BG, fg=TEXT_MID, padx=14, pady=8, cursor="hand2")
        cancel.pack(side="left", padx=10)
        cancel.bind("<Button-1>", lambda e: popup.destroy())

        ok = tk.Label(btn_row, text="  Confirm Enrollment  ", font=self.fn_btn,
                      bg=BTN_BG, fg=BTN_FG, padx=14, pady=8, cursor="hand2")
        ok.pack(side="left", padx=10)
        ok.bind("<Button-1>", lambda e: [popup.destroy(), self._show_success(course)])
        ok.bind("<Enter>", lambda e: ok.config(bg=BTN_HOV))
        ok.bind("<Leave>", lambda e: ok.config(bg=BTN_BG))

    def _show_success(self, course):
        popup = tk.Toplevel(self)
        popup.title("Enrolled!")
        popup.geometry("380x220")
        popup.configure(bg=BG_CARD)
        popup.resizable(False, False)
        popup.grab_set()

        tk.Frame(popup, bg=ACCENT, height=4).pack(fill="x")
        tk.Label(popup, text="✓  Enrollment Successful",
                 font=self.fn_subhead, bg=BG_CARD, fg=TEXT_DARK).pack(pady=(24, 8))
        tk.Label(popup,
                 text=f"You are now enrolled in\n{course['code']}  —  {course['title']}",
                 font=self.fn_body, bg=BG_CARD, fg=TEXT_MID,
                 justify="center").pack()

        close = tk.Label(popup, text="  Close  ", font=self.fn_btn,
                         bg=BTN_BG, fg=BTN_FG, padx=16, pady=8, cursor="hand2")
        close.pack(pady=22)
        close.bind("<Button-1>", lambda e: popup.destroy())

if __name__ == "__main__":
    app = LMSCourseBrowser()
    app.mainloop()
