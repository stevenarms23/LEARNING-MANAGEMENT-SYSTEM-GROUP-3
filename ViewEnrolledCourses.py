import tkinter as tk
from tkinter import ttk
import os
from courses_backend import CourseManager

class PUP_LMS_Portal:
    def __init__(self, root):
        self.root = root
        self.root.title("PUP LMS — Course Catalog")
        self.root.geometry("1250x760")
        self.root.configure(bg="#f7ede2")

        # Visual Theme Style Guide Color Palette Mapping
        self.c_primary_dark = "#4a2c11"
        self.c_secondary_brown = "#84593c"
        self.c_bg = "#f7ede2"
        self.c_card_bg = "#fffbf7"
        self.c_text_dark = "#2b1a08"
        self.c_text_muted = "#7c6853"
        self.c_accent_tan = "#dac3b3"
        self.c_border = "#d1bead"

        # Initialize Storage Backend Systems
        self.backend = CourseManager()
        self.current_user = {"username": "Jeffrey Soriano", "role": "student"}
        
        # Self-healing clean database check
        self._seed_database_if_empty()
        self.setup_styles()
        
        self.main_container = tk.Frame(self.root, bg=self.c_bg)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Open up the course catalog layout grid instantly
        self.show_enrolled_courses_view()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(".", font=("Times New Roman", 10))
        self.style.configure("Filter.TLabel", background=self.c_accent_tan, foreground=self.c_primary_dark, font=("Times New Roman", 9, "bold"))
        self.style.configure("Count.TLabel", background=self.c_primary_dark, foreground="white", font=("Times New Roman", 10, "bold"))
        self.style.configure("TCombobox", font=("Times New Roman", 9))

    def clear_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def handle_enrollment_toggle(self, course_id, button_widget, count_label, canvas_bar):
        """Syncs selection switches seamlessly with the backend file system layers."""
        username = self.current_user["username"]
        is_enrolled = self.backend.is_enrolled(course_id, username)

        if is_enrolled:
            if self.backend.unenroll(self.current_user, course_id):
                # Since we are in the "My Enrolled Courses" view, unenrollment should drop the card instantly
                self.show_enrolled_courses_view()
                return
        else:
            if self.backend.enroll(self.current_user, course_id):
                button_widget.config(text="✓ ENROLLED", bg="#5e4431")
        
        updated_course = self.backend.get_course(course_id)
        enrolled_count = len(updated_course.get("enrolled", [])) if updated_course else 0
        max_cap = 45
        
        count_label.config(text=f"{enrolled_count} / {max_cap} enrolled")
        
        ratio = min(max(enrolled_count / max_cap, 0.0), 1.0)
        self._draw_progress(canvas_bar, ratio)

    def show_enrolled_courses_view(self):
        self.clear_container()
        
        enrolled_courses = self.backend.get_enrolled_courses(self.current_user)

        header = tk.Frame(self.main_container, bg=self.c_primary_dark, height=75)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)

        brand_frame = tk.Frame(header, bg=self.c_primary_dark)
        brand_frame.pack(side=tk.LEFT, padx=30, pady=10)

        tk.Label(brand_frame, text="PUP", bg="white", fg=self.c_primary_dark, font=("Times New Roman", 11, "bold"), width=4, height=2).pack(side=tk.LEFT, padx=(0, 15))
        
        title_frame = tk.Frame(brand_frame, bg=self.c_primary_dark)
        title_frame.pack(side=tk.LEFT)
        tk.Label(title_frame, text="Polytechnic University of the Philippines", bg=self.c_primary_dark, fg="white", font=("Times New Roman", 14)).pack(anchor="w")
        tk.Label(title_frame, text="LEARNING MANAGEMENT SYSTEM  •  MY ENROLLED COURSES", bg=self.c_primary_dark, fg="#c9b097", font=("Times New Roman", 8, "bold")).pack(anchor="w")

        nav_frame = tk.Frame(header, bg=self.c_primary_dark)
        nav_frame.pack(side=tk.RIGHT, padx=30)

        for item in ["Dashboard", "My Courses", "Schedule", "Grades", "Courses"]:
            is_active = (item == "My Courses")
            bg_c = self.c_secondary_brown if is_active else self.c_primary_dark
            fg_c = "white" if is_active else "#dcd0c4"
            tk.Label(nav_frame, text=item, bg=bg_c, fg=fg_c, font=("Times New Roman", 10), padx=12, pady=8).pack(side=tk.LEFT, padx=2)

        body_wrapper = tk.Frame(self.main_container, bg=self.c_bg)
        body_wrapper.pack(fill=tk.BOTH, expand=True, padx=35, pady=15)

        title_row = tk.Frame(body_wrapper, bg=self.c_bg)
        title_row.pack(fill=tk.X, pady=(0, 10))

        title_left = tk.Frame(title_row, bg=self.c_bg)
        title_left.pack(side=tk.LEFT)
        tk.Label(title_left, text="My Enrolled Courses", font=("Times New Roman", 22, "bold"), bg=self.c_bg, fg=self.c_primary_dark).pack(anchor="w")
        self.lbl_summary = tk.Label(title_left, text=f"You are currently enrolled in {len(enrolled_courses)} courses", font=("Times New Roman", 10, "italic"), bg=self.c_bg, fg=self.c_text_muted)
        self.lbl_summary.pack(anchor="w")

        badge_frame = tk.Frame(title_row, highlightbackground=self.c_border, highlightthickness=1, bg="white", padx=12, pady=4)
        badge_frame.pack(side=tk.RIGHT)
        
        tk.Label(badge_frame, text="2nd Semester", bg="white", fg=self.c_primary_dark, font=("Times New Roman", 9)).pack()
        tk.Label(badge_frame, text="AY 2026-2027", bg="white", fg=self.c_primary_dark, font=("Times New Roman", 9, "bold")).pack()

        controls_bar = tk.Frame(body_wrapper, bg=self.c_bg)
        controls_bar.pack(fill=tk.X, pady=(0, 15))

        self.search_entry = tk.Entry(controls_bar, width=34, bg="white", fg=self.c_text_dark, 
                                     highlightbackground=self.c_border, highlightthickness=1, bd=0, font=("Times New Roman", 10))
        self.search_entry.pack(side=tk.LEFT, padx=(0, 12), ipady=4)

        self.search_entry.bind("<KeyRelease>", self.execute_live_search)
        self.search_entry.insert(0, "Search enrolled title, code, or instructor...")
        self.search_entry.bind("<FocusIn>", lambda e: self.search_entry.delete(0, tk.END) if self.search_entry.get() == "Search enrolled title, code, or instructor..." else None)

        self.lbl_count_badge = ttk.Label(controls_bar, text=f"{len(enrolled_courses)} Enrolled", style="Count.TLabel", padding=(10, 4))
        self.lbl_count_badge.pack(side=tk.LEFT)

        self.grid_frame = tk.Frame(body_wrapper, bg=self.c_bg)
        self.grid_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        for c_idx in range(3):
            self.grid_frame.columnconfigure(c_idx, weight=1)

        self.render_course_grid(enrolled_courses)

        footer = tk.Frame(self.main_container, bg=self.c_primary_dark, height=30)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        footer.pack_propagate(False)
        tk.Label(footer, text="© 2026 Polytechnic University of the Philippines  •  Registrar's Office  •  All Rights Reserved", bg=self.c_primary_dark, fg="#c9b097", font=("Times New Roman", 8)).pack(pady=6)

    def render_course_grid(self, target_courses):
        """Generates formatted grid rows iteratively from dataset arrays cleanly."""
        for child in self.grid_frame.winfo_children():
            child.destroy()

        if not target_courses:
            no_res_lbl = tk.Label(
                self.grid_frame, 
                text="⚠️ You are NOT enrolled in any course", 
                font=("Times New Roman", 14, "bold"), 
                bg=self.c_bg, 
                fg=self.c_secondary_brown
            )
            no_res_lbl.grid(row=0, column=0, columnspan=3, pady=60, sticky="ew")
            return

        for idx, course in enumerate(target_courses):
            card = tk.Frame(self.grid_frame, highlightbackground=self.c_border, highlightthickness=1, bg=self.c_card_bg, padx=15, pady=15)
            
            max_cols = 3
            row_pos = idx // max_cols
            col_pos = idx % max_cols
            card.grid(row=row_pos, column=col_pos, padx=8, pady=5, sticky="nsew")

            raw_title = course.get("name", "Untitled Course")
            
            if "—" in raw_title:
                code_part = raw_title.split("—")[0].strip()
                title_part = raw_title.split("—")[1].strip()
            else:
                code_part = "COURSE"
                title_part = raw_title

            card_head = tk.Frame(card, bg=self.c_card_bg)
            card_head.pack(fill=tk.X, pady=(0, 2))
            tk.Label(card_head, text=code_part, bg=self.c_card_bg, fg=self.c_primary_dark, font=("Times New Roman", 11, "bold")).pack(side=tk.LEFT)
            tk.Label(card_head, text="MY CLASS", bg="#5e4431", fg="white", font=("Times New Roman", 8, "bold"), padx=5, pady=1).pack(side=tk.RIGHT)

            tk.Label(card, text=title_part, bg=self.c_card_bg, fg=self.c_primary_dark, font=("Times New Roman", 11, "bold"), wraplength=270, justify="left").pack(anchor="w", pady=(0, 2))
            tk.Label(card, text="Engineering Core" if "103" in code_part or "105" in code_part else "Mathematics & Sciences", bg=self.c_accent_tan, fg=self.c_primary_dark, font=("Times New Roman", 8, "bold"), padx=5, pady=1).pack(anchor="w", pady=(0, 8))

            meta_frame = tk.Frame(card, bg=self.c_card_bg)
            meta_frame.pack(fill=tk.X, pady=(0, 8))
            tk.Label(meta_frame, text=f"•  Instructor:  {course.get('instructor', 'Assigned Staff')}", bg=self.c_card_bg, fg=self.c_text_dark, font=("Times New Roman", 9)).pack(anchor="w", pady=1)
            
            if "103" in code_part:
                sched_txt = "TH/TH 7:30AM-10:30AM / 10:30AM-1:30PM"
            elif "104" in code_part:
                sched_txt = "F/F 7:30AM-9:00AM / 9:00AM-10:30AM"
            else:
                sched_txt = "M/S 6:00PM-9:00PM / 2:00PM-5:00PM"
            tk.Label(meta_frame, text=f"◷  Schedule:  {sched_txt}", bg=self.c_card_bg, fg=self.c_text_dark, font=("Times New Roman", 9), wraplength=270, justify="left").pack(anchor="w", pady=1)

            lec_v, lab_v, unit_v = "3.0", "0.0", "3.0"
            if "LEC:" in course.get("description", ""):
                try:
                    desc_body = course["description"]
                    lec_v = desc_body.split("LEC:")[1].split("|")[0]
                    lab_v = desc_body.split("LAB:")[1].split("|")[0]
                    unit_v = desc_body.split("UNITS:")[1].split("]")[0]
                except IndexError:
                    pass

            unit_table = tk.Frame(card, bg=self.c_card_bg)
            unit_table.pack(fill=tk.X, pady=(0, 8))
            for label, value in [("LEC", lec_v), ("LAB", lab_v), ("UNITS", unit_v)]:
                box = tk.Frame(unit_table, bg=self.c_accent_tan, padx=6, pady=2)
                box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=1)
                tk.Label(box, text=label, bg=self.c_accent_tan, fg=self.c_text_muted, font=("Times New Roman", 8, "bold")).pack()
                tk.Label(box, text=str(value), bg=self.c_accent_tan, fg=self.c_primary_dark, font=("Times New Roman", 10, "bold")).pack()

            enr_frame = tk.Frame(card, bg=self.c_card_bg)
            enr_frame.pack(fill=tk.X, pady=(0, 4))
            tk.Label(enr_frame, text="ENROLLMENT CAPACITY", bg=self.c_card_bg, fg=self.c_text_muted, font=("Times New Roman", 8, "bold")).pack(anchor="w")
            
            canvas_bar = tk.Canvas(enr_frame, bg="#e6dfd7", height=5, highlightthickness=0, bd=0)
            canvas_bar.pack(fill=tk.X, pady=2)
            
            enrolled_count = len(course.get("enrolled", []))
            max_cap = 45
            
            ratio = min(max(enrolled_count / max_cap, 0.0), 1.0)
            canvas_bar.bind("<Configure>", lambda e, c=canvas_bar, r=ratio: self._draw_progress(c, r))
            
            lbl_capacity = tk.Label(enr_frame, text=f"{enrolled_count} / {max_cap} enrolled", bg=self.c_card_bg, fg=self.c_text_muted, font=("Times New Roman", 9))
            lbl_capacity.pack(anchor="e")

            clean_desc = course.get("description", "").split("[LEC:")[0].strip()
            tk.Label(card, text=clean_desc, bg=self.c_card_bg, fg=self.c_text_muted, font=("Times New Roman", 9), wraplength=265, justify="left").pack(anchor="w", fill=tk.BOTH, expand=True, pady=(0, 10))

            # Enrollment Toggle Action (Since they see this view, they are enrolled; clicking unenrolls them)
            btn_action = tk.Button(card, text="UNENROLL", font=("Times New Roman", 9, "bold"), bg=self.c_secondary_brown, fg="white", bd=0, pady=5, cursor="hand2")
            btn_action.config(command=lambda cid=course["course_id"], b=btn_action, l=lbl_capacity, bar=canvas_bar: self.handle_enrollment_toggle(cid, b, l, bar))
            btn_action.pack(fill=tk.X, side=tk.BOTTOM)

    def execute_live_search(self, event=None):
        """Filters dashboard listings dynamically on character keys typing events."""
        query = self.search_entry.get().strip().lower()
        if query == "search enrolled title, code, or instructor...":
            query = ""

        # CHANGED: Ensure search also filters only within enrolled items
        all_records = self.backend.get_enrolled_courses(self.current_user)
        filtered_results = []

        for course in all_records:
            if query in course.get("name", "").lower() or query in course.get("description", "").lower() or query in course.get("instructor", "").lower():
                filtered_results.append(course)

        self.lbl_summary.config(text=f"You are currently enrolled in {len(filtered_results)} courses")
        self.lbl_count_badge.config(text=f"{len(filtered_results)} Enrolled")
        self.render_course_grid(filtered_results)

    def _draw_progress(self, canvas, ratio):
        canvas.delete("all")
        width = canvas.winfo_width()
        if width > 1 and ratio > 0:
            canvas.create_rectangle(0, 0, int(width * ratio), 5, fill=self.c_secondary_brown, width=0)

if __name__ == "__main__":
   
    if os.path.exists("courses.json"):
        try:
            with open("courses.json", "r") as f:
                chk = f.read()
                if "cmpe" not in chk.lower() or "instructor" not in chk.lower():
                    os.remove("courses.json")
        except:
            pass

    root = tk.Tk()
    app = PUP_LMS_Portal(root)
    root.mainloop()
