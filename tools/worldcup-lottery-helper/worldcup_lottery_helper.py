import webbrowser
import datetime
import time
import tkinter as tk
from tkinter import messagebox

REGISTRATION_URL = "https://regnyctix.com/"

# Edit these values before running.
# Do not commit your real private info if the repository is public.
YOUR_INFO = {
    "First Name": "Tony",
    "Last Name": "",
    "Email": "your_email@example.com",
    "Phone": "your_phone_number",
    "Address": "your NYC address",
    "City": "New York",
    "State": "NY",
    "ZIP": "your_zip_code",
}

# Opens the official site slightly before the daily registration time.
# Default: 9:59:50 AM local computer time.
OPEN_HOUR = 9
OPEN_MINUTE = 59
OPEN_SECOND = 50


def wait_until_open_time():
    print("NYC World Cup lottery helper running...")
    print(f"Official page will open at {OPEN_HOUR:02d}:{OPEN_MINUTE:02d}:{OPEN_SECOND:02d} local time.")

    while True:
        now = datetime.datetime.now()
        target = now.replace(
            hour=OPEN_HOUR,
            minute=OPEN_MINUTE,
            second=OPEN_SECOND,
            microsecond=0,
        )

        if now >= target:
            break

        remaining = target - now
        print(f"Time remaining: {remaining}", end="\r")
        time.sleep(0.5)


def show_info_window():
    root = tk.Tk()
    root.title("NYC World Cup Lottery Info Helper")
    root.geometry("560x440")

    tk.Label(
        root,
        text="Copy/paste your info quickly into the official registration form.",
        font=("Arial", 13, "bold"),
    ).pack(pady=10)

    tk.Label(
        root,
        text="This tool does not auto-submit, bypass queues, or create multiple entries.",
        font=("Arial", 10),
    ).pack(pady=2)

    text_box = tk.Text(root, height=16, width=65)
    text_box.pack(padx=10, pady=10)

    for key, value in YOUR_INFO.items():
        text_box.insert(tk.END, f"{key}: {value}\n")

    def copy_all():
        root.clipboard_clear()
        root.clipboard_append(text_box.get("1.0", tk.END))
        messagebox.showinfo("Copied", "Your info was copied to clipboard.")

    tk.Button(root, text="Copy All Info", command=copy_all, height=2).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    wait_until_open_time()
    webbrowser.open(REGISTRATION_URL)
    print("\a")
    time.sleep(1)
    show_info_window()
