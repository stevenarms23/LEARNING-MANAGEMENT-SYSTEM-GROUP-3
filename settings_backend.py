# settings_backend.py - My settings module for LMS

import json
import os

class SettingsManager:
    def __init__(self, settings_file="lms_settings.json"):
        # The file where settings are saved
        self.settings_file = settings_file
        
        # Default settings (what the app starts with)
        self.default_settings = {
            "theme": "light",           # light or dark mode
            "font_size": 12,            # text size
            "language": "English",      # English or Spanish
            "confirm_delete": True,     # ask before deleting?
            "confirm_enroll": True,     # ask before enrolling?
            "auto_save": True,          # auto save changes?
            "default_download_folder": os.path.expanduser("~/Downloads"),
            "show_notifications": True,  # show popups?
            "compact_view": False        # show less info?
        }
        
        # Load saved settings or use defaults
        self.settings = self.load_settings()
    
    def load_settings(self):
        # Load settings from JSON file if it exists
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    saved = json.load(f)
                    # Merge with defaults
                    merged = self.default_settings.copy()
                    merged.update(saved)
                    return merged
            except:
                return self.default_settings.copy()
        return self.default_settings.copy()
    
    def save_settings(self):
        # Save settings to JSON file
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
            return True
        except:
            return False
    
    def get(self, key):
        # Get a setting value
        return self.settings.get(key, self.default_settings.get(key))
    
    def set(self, key, value):
        # Change a setting value
        if key in self.settings:
            self.settings[key] = value
            self.save_settings()
            return True
        return False
    
    def reset_all(self):
        # Reset everything to defaults
        self.settings = self.default_settings.copy()
        self.save_settings()
    
    def get_all(self):
        # Return all settings
        return self.settings.copy()


# Test
if __name__ == "__main__":
    s = SettingsManager()
    print("Theme:", s.get("theme"))
    print("Font size:", s.get("font_size"))
    print("Confirm delete:", s.get("confirm_delete"))
    
    # Change a setting
    s.set("theme", "dark")
    print("New theme:", s.get("theme"))
    
    # Reset
    s.reset_all()
    print("Reset theme:", s.get("theme"))