import tkinter as tk
import random

# Truth & Dare Questions

truths = [
    "What is your biggest fear?",
    "What is the most embarrassing thing you’ve ever done?",
    "What is a secret you’ve never told anyone?",
    
    "Who was your first crush?",
    "What is a bad habit you want to break?",
    "What is the worst lie you ever told?",
    "What is something you regret doing?",
    "If you could erase one memory, what would it be?",
    "What’s the most childish thing you still do?",
    "Have you ever cheated in an exam?"
]

dares = [
    "Do 10 push-ups.",
    "Speak in a funny accent for 2 minutes.",
    "Dance for 20 seconds without music.",
    "Try to lick your elbow.",
    "Say 'I am the best!' 10 times loudly.",
    "Do your best animal impression.",
    "Spin around 10 times and try to walk straight.",
    "Hold a funny face for 30 seconds.",
    "Sing a random song loudly.",
    "Act like a robot for 15 seconds."
]

# -----------------------------
# Tkinter UI
# -----------------------------

root = tk.Tk()
root.title("Truth or Dare Game")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#ffe6cc")

title_label = tk.Label(
    root, text="Truth or Dare Game",
    font=("Arial", 24, "bold"),
    bg="#ffe6cc", fg="#cc3300"
)
title_label.pack(pady=20)

result_label = tk.Label(
    root, text="Click a button to begin!",
    font=("Arial", 14),
    wraplength=450,
    bg="#ffe6cc",
)
result_label.pack(pady=40)

# -----------------------------
# Button Functions
# -----------------------------

def show_truth():
    result_label.config(text="Truth:\n" + random.choice(truths))

def show_dare():
    result_label.config(text="Dare:\n" + random.choice(dares))

# -----------------------------
# Buttons
# -----------------------------

btn_frame = tk.Frame(root, bg="#ffe6cc")
btn_frame.pack()

truth_btn = tk.Button(
    btn_frame, text="Truth",
    font=("Arial", 16, "bold"),
    bg="#ffcc66", fg="black",
    width=10, command=show_truth
)
truth_btn.grid(row=0, column=0, padx=20, pady=20)

dare_btn = tk.Button(
    btn_frame, text="Dare",
    font=("Arial", 16, "bold"),
    bg="#ff9966", fg="black",
    width=10, command=show_dare
)
dare_btn.grid(row=0, column=1, padx=20, pady=20)

root.mainloop()

