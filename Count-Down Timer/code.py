import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading

# Motivational quotes
quotes = [
    "Every second counts.",
    "Make today your masterpiece.",
    "You are closer than you think.",
    "Stay focused. Stay strong.",
    "Dreams don’t work unless you do."
]

# Function to calculate time difference
def calculate_time_difference(target_datetime):
    now = datetime.now()
    if target_datetime < now:
        return None
    delta = target_datetime - now
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return years, months, days, hours, minutes, seconds

# Function to update countdown
def update_countdown():
    while True:
        try:
            target = datetime.strptime(entry.get(), "%Y-%m-%d")
            result = calculate_time_difference(target)
            if result:
                years, months, days, hours, minutes, seconds = result
                countdown_label.config(
                    text=f"{years} Years {months} Months {days} Days\n"
                         f"{hours} Hours {minutes} Minutes {seconds} Seconds",
                    fg="cyan"
                )
                quote_label.config(text=random.choice(quotes))
            else:
                countdown_label.config(text="Time's up!", fg="red")
            time.sleep(1)
        except Exception as e:
            countdown_label.config(text="Invalid Date Format!", fg="red")
            break

# Start the countdown in a separate thread
def start_countdown():
    threading.Thread(target=update_countdown, daemon=True).start()

# Setting up GUI
root = tk.Tk()
root.title("Live Countdown Timer")
root.geometry("400x400")
root.configure(bg="black")

# Entry for Target Date
tk.Label(root, text="Enter Target Date (YYYY-MM-DD):", fg="white", bg="black", font=("Helvetica", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
entry.pack(pady=5)

# Start Button
start_button = tk.Button(root, text="Start Countdown", command=start_countdown, font=("Helvetica", 14), bg="green", fg="white")
start_button.pack(pady=10)

# Countdown Display
countdown_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), bg="black")
countdown_label.pack(pady=20)

# Motivational Quote Display
import random
quote_label = tk.Label(root, text="", font=("Helvetica", 10, "italic"), fg="yellow", bg="black", wraplength=350)
quote_label.pack(pady=10)

root.mainloop()
