import tkinter as tk
from datetime import datetime


def calculate_pages(start_time: str, end_time: str, start_page: int, end_page: int) -> str:
    """Return a friendly status message describing the current reading progress."""
    now = datetime.now()
    start_dt = datetime.strptime(start_time, "%H:%M")
    end_dt = datetime.strptime(end_time, "%H:%M")
    start_dt = now.replace(hour=start_dt.hour, minute=start_dt.minute, second=0, microsecond=0)
    end_dt = now.replace(hour=end_dt.hour, minute=end_dt.minute, second=0, microsecond=0)

    if end_dt <= start_dt:
        return "End time must be after the start time."

    if now < start_dt:
        minutes = int((start_dt - now).total_seconds() // 60)
        return f"Reading begins in {minutes} minute(s)."

    if now >= end_dt:
        return f"Reading session finished. Review final page {end_page}."

    total_minutes = (end_dt - start_dt).total_seconds()
    elapsed_minutes = (now - start_dt).total_seconds()
    progress = min(max(elapsed_minutes / total_minutes, 0), 1)

    total_pages = max(end_page - start_page, 0) + 1
    current_page = start_page + int(total_pages * progress)
    current_page = min(max(current_page, start_page), end_page)

    return f"Estimated position: page {current_page}."


def update_progress():
    message = calculate_pages(start_time, end_time, start_page, end_page)
    progress_label.config(text=message)

    now = datetime.now()
    end_dt = datetime.strptime(end_time, "%H:%M")
    end_dt = now.replace(hour=end_dt.hour, minute=end_dt.minute, second=0, microsecond=0)

    if now < end_dt:
        root.after(60000, update_progress)


# User input
start_time = input("Enter reading start time (e.g. 08:00): ")
end_time = input("Enter reading end time (e.g. 10:00): ")
start_page = int(input("Enter start page: "))
end_page = int(input("Enter end page: "))

print(f"Start {start_time} / End {end_time} / Pages {start_page}->{end_page}")

# Tkinter window setup
root = tk.Tk()
root.title("Reading Timer")
root.geometry("420x220")
root.resizable(False, False)

info_frame = tk.Frame(root)
info_frame.pack(pady=(20, 10))

time_label = tk.Label(info_frame, text=f"Start {start_time} / End {end_time}", font=("Helvetica", 12))
time_label.pack()

page_label = tk.Label(info_frame, text=f"Pages {start_page} -> {end_page}", font=("Helvetica", 12))
page_label.pack()

progress_label = tk.Label(root, text="Calculating progress...", font=("Helvetica", 14), wraplength=360, justify="center")
progress_label.pack(pady=20)

update_progress()

root.mainloop()
