"""
courses_backend.py — Backend module for Course Management
=========================================================
Self-contained, JSON-persisted. No external auth dependency.
Designed to integrate with any Tkinter frontend.

Usage:
    cm = CourseManager()
    cm.add_course(user, "Physics 101", "Intro course", pdf_source="C:/path/to/file.pdf")
    cm.enroll(user, "course_uuid")
    cm.download_pdf(user, "course_uuid", "C:/save/here.pdf")
"""

import json
import os
import shutil
import uuid
from datetime import datetime


class CourseManager:
    """Handles all course CRUD, enrollment, and PDF operations with JSON persistence."""

    def __init__(self, data_file="courses.json", pdf_dir="pdfs"):
        """
        Initialize the course manager.
        
        Args:
            data_file: Path to the JSON file storing course data.
            pdf_dir: Directory where uploaded PDFs are stored.
        """
        self.data_file = data_file
        self.pdf_dir = pdf_dir
        
        # Create PDF directory if it doesn't exist
        if not os.path.exists(self.pdf_dir):
            os.makedirs(self.pdf_dir)
        
        # Initialize data file if it doesn't exist
        if not os.path.exists(self.data_file):
            self._save_data({"courses": []})
    
    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    
    def _load_data(self):
        """Load course data from JSON file."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # Corrupted or missing file — start fresh
            print(f"Warning: {self.data_file} was corrupted. Starting fresh.")
            return {"courses": []}
    
    def _save_data(self, data):
        """Save course data to JSON file atomically."""
        tmp_file = self.data_file + ".tmp"
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp_file, self.data_file)
    
    def _find_course(self, courses, course_id):
        """Find a course by ID in the courses list."""
        for course in courses:
            if course["course_id"] == course_id:
                return course
        return None
    
    def _validate_user(self, user):
        """Ensure user dict has required keys."""
        return user and isinstance(user, dict) and "username" in user and "role" in user
    
    def _is_instructor(self, user):
        """Check if user has instructor role."""
        return self._validate_user(user) and user["role"] == "instructor"
    
    def _is_student(self, user):
        """Check if user has student role."""
        return self._validate_user(user) and user["role"] == "student"
    
    def _is_owner(self, course, username):
        """Check if user is the instructor who created the course."""
        return course.get("instructor") == username
    
    def _is_enrolled(self, course, username):
        """Check if a username is enrolled in the course."""
        return username in course.get("enrolled", [])
    
    # ------------------------------------------------------------------
    # Course CRUD
    # ------------------------------------------------------------------
    
    def add_course(self, user, name, description="", pdf_source=None):
        """
        Create a new course (instructor only).
        
        Args:
            user: Dict with 'username' and 'role' keys.
            name: Course name (required).
            description: Course description (optional).
            pdf_source: Full path to a PDF file to upload (optional).
        
        Returns:
            Course dict on success, None on failure.
        """
        if not self._is_instructor(user):
            print("Error: Only instructors can create courses.")
            return None
        
        if not name or not name.strip():
            print("Error: Course name is required.")
            return None
        
        course_id = str(uuid.uuid4())
        pdf_path = None
        
        # Handle PDF upload
        if pdf_source and os.path.exists(pdf_source):
            ext = os.path.splitext(pdf_source)[1].lower()
            if ext != ".pdf":
                print("Error: Only PDF files are allowed.")
                return None
            try:
                dest = os.path.join(self.pdf_dir, f"{course_id}.pdf")
                shutil.copy2(pdf_source, dest)
                pdf_path = f"{course_id}.pdf"
            except Exception as e:
                print(f"Error: Failed to copy PDF — {e}")
                return None
        
        course = {
            "course_id": course_id,
            "name": name.strip(),
            "description": description.strip(),
            "instructor": user["username"],
            "enrolled": [],
            "pdf_path": pdf_path,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        
        data = self._load_data()
        data["courses"].append(course)
        self._save_data(data)
        
        return course
    
    def edit_course(self, user, course_id, name=None, description=None, pdf_source=None):
        """
        Update course details (instructor + owner only).
        
        Args:
            user: Dict with 'username' and 'role' keys.
            course_id: ID of the course to edit.
            name: New course name (or None to keep unchanged).
            description: New description (or None to keep unchanged).
            pdf_source: New PDF file path (or None to keep current).
        
        Returns:
            True on success, False on failure.
        """
        if not self._is_instructor(user):
            print("Error: Only instructors can edit courses.")
            return False
        
        data = self._load_data()
        course = self._find_course(data["courses"], course_id)
        
        if not course:
            print("Error: Course not found.")
            return False
        
        if not self._is_owner(course, user["username"]):
            print("Error: You can only edit your own courses.")
            return False
        
        # Update fields
        if name is not None:
            if not name.strip():
                print("Error: Course name cannot be empty.")
                return False
            course["name"] = name.strip()
        
        if description is not None:
            course["description"] = description.strip()
        
        # Handle PDF replacement
        if pdf_source is not None:
            if not os.path.exists(pdf_source):
                print("Error: PDF file not found.")
                return False
            ext = os.path.splitext(pdf_source)[1].lower()
            if ext != ".pdf":
                print("Error: Only PDF files are allowed.")
                return False
            try:
                # Remove old PDF
                if course.get("pdf_path"):
                    old_pdf = os.path.join(self.pdf_dir, course["pdf_path"])
                    if os.path.exists(old_pdf):
                        os.remove(old_pdf)
                
                dest = os.path.join(self.pdf_dir, f"{course_id}.pdf")
                shutil.copy2(pdf_source, dest)
                course["pdf_path"] = f"{course_id}.pdf"
            except Exception as e:
                print(f"Error: Failed to copy PDF — {e}")
                return False
        
        course["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_data(data)
        return True
    
    def delete_course(self, user, course_id):
        """
        Delete a course and its associated PDF (instructor + owner only).
        
        Args:
            user: Dict with 'username' and 'role' keys.
            course_id: ID of the course to delete.
        
        Returns:
            True on success, False on failure.
        """
        if not self._is_instructor(user):
            print("Error: Only instructors can delete courses.")
            return False
        
        data = self._load_data()
        course = self._find_course(data["courses"], course_id)
        
        if not course:
            print("Error: Course not found.")
            return False
        
        if not self._is_owner(course, user["username"]):
            print("Error: You can only delete your own courses.")
            return False
        
        # Remove PDF file
        if course.get("pdf_path"):
            pdf_file = os.path.join(self.pdf_dir, course["pdf_path"])
            if os.path.exists(pdf_file):
                try:
                    os.remove(pdf_file)
                except Exception as e:
                    print(f"Warning: Could not remove PDF — {e}")
        
        # Remove course from list
        data["courses"] = [c for c in data["courses"] if c["course_id"] != course_id]
        self._save_data(data)
        return True
    
    # ------------------------------------------------------------------
    # Read operations
    # ------------------------------------------------------------------
    
    def get_all_courses(self):
        """Return all courses (no role restriction)."""
        data = self._load_data()
        return data["courses"]
    
    def get_course(self, course_id):
        """Return a single course by ID, or None."""
        data = self._load_data()
        return self._find_course(data["courses"], course_id)
    
    def get_enrolled_courses(self, user):
        """
        Return courses the user is enrolled in or owns.
        
        - Instructors see courses they created.
        - Students see courses they enrolled in.
        """
        if not self._validate_user(user):
            return []
        
        data = self._load_data()
        username = user["username"]
        role = user["role"]
        
        result = []
        for course in data["courses"]:
            if role == "instructor" and course.get("instructor") == username:
                result.append(course)
            elif role == "student" and self._is_enrolled(course, username):
                result.append(course)
        
        return result
    
    def is_enrolled(self, course_id, username):
        """Check if a username is enrolled in a given course."""
        course = self.get_course(course_id)
        if not course:
            return False
        return self._is_enrolled(course, username)
    
    # ------------------------------------------------------------------
    # Enrollment
    # ------------------------------------------------------------------
    
    def enroll(self, user, course_id):
        """
        Enroll a student in a course.
        
        Args:
            user: Dict with 'username' and 'role' keys (must be student).
            course_id: ID of the course.
        
        Returns:
            True on success, False on failure.
        """
        if not self._is_student(user):
            print("Error: Only students can enroll in courses.")
            return False
        
        data = self._load_data()
        course = self._find_course(data["courses"], course_id)
        
        if not course:
            print("Error: Course not found.")
            return False
        
        username = user["username"]
        
        if self._is_enrolled(course, username):
            print("Error: Already enrolled in this course.")
            return False
        
        course["enrolled"].append(username)
        self._save_data(data)
        return True
    
    def unenroll(self, user, course_id):
        """
        Unenroll a student from a course.
        
        Args:
            user: Dict with 'username' and 'role' keys (must be student).
            course_id: ID of the course.
        
        Returns:
            True on success, False on failure.
        """
        if not self._is_student(user):
            print("Error: Only students can unenroll from courses.")
            return False
        
        data = self._load_data()
        course = self._find_course(data["courses"], course_id)
        
        if not course:
            print("Error: Course not found.")
            return False
        
        username = user["username"]
        
        if not self._is_enrolled(course, username):
            print("Error: Not enrolled in this course.")
            return False
        
        course["enrolled"].remove(username)
        self._save_data(data)
        return True
    
    # ------------------------------------------------------------------
    # PDF operations
    # ------------------------------------------------------------------
    
    def upload_pdf(self, user, course_id, source_filepath):
        """
        Upload/replace a PDF for a course (instructor + owner only).
        Convenience wrapper around edit_course.
        
        Args:
            user: Dict with 'username' and 'role' keys.
            course_id: ID of the course.
            source_filepath: Full path to the PDF file.
        
        Returns:
            True on success, False on failure.
        """
        return self.edit_course(user, course_id, pdf_source=source_filepath)
    
    def download_pdf(self, user, course_id, destination_filepath):
        """
        Download a course PDF (enrolled students or instructor/owner).
        
        Args:
            user: Dict with 'username' and 'role' keys.
            course_id: ID of the course.
            destination_filepath: Where to save the file.
        
        Returns:
            True on success, False on failure.
        """
        if not self._validate_user(user):
            print("Error: Invalid user.")
            return False
        
        course = self.get_course(course_id)
        if not course:
            print("Error: Course not found.")
            return False
        
        username = user["username"]
        role = user["role"]
        
        # Must be enrolled, the instructor, or an admin (admin not implemented yet)
        is_authorized = (
            self._is_enrolled(course, username) or
            (role == "instructor" and self._is_owner(course, username))
        )
        
        if not is_authorized:
            print("Error: You are not enrolled in this course.")
            return False
        
        if not course.get("pdf_path"):
            print("Error: No PDF available for this course.")
            return False
        
        source = os.path.join(self.pdf_dir, course["pdf_path"])
        if not os.path.exists(source):
            print("Error: PDF file not found on server.")
            return False
        
        try:
            shutil.copy2(source, destination_filepath)
            return True
        except Exception as e:
            print(f"Error: Failed to download PDF — {e}")
            return False