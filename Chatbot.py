import tkinter as tk
from tkinter import scrolledtext
import random

def get_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input:
        return random.choice([
            "Hi there!",
            "Hello!",
            "Hey! How can I help you?"
        ])

    # How are you
    elif "how are you" in user_input:
        return random.choice([
            "I'm doing great, thanks!",
            "All good! What about you?",
            "I'm fine, thanks for asking!"
        ])

    # Name
    elif "your name" in user_input:
        return "I'm a Python chatbot."

    # Creator
    elif "who built you" in user_input or "who made you" in user_input:
        return "I was built by Muhammad Ahmad Raza."

    # Year
    elif "year" in user_input or "what year" in user_input:
        return "I exist in the modern era of technology 😄"

    # Top fields
    elif "top fields" in user_input or "best fields" in user_input:
        return ("Some top fields right now are:\n"
                "- Artificial Intelligence\n"
                "- Cybersecurity\n"
                "- Data Science\n"
                "- Software Development\n"
                "- Cloud Computing")

    # Earn money
    elif "earn money" in user_input or "make money" in user_input:
        return ("You can earn money by:\n"
                "- Freelancing (Fiverr, Upwork)\n"
                "- Learning programming\n"
                "- Starting a YouTube channel\n"
                "- Blogging or affiliate marketing\n"
                "- Selling digital skills")

    # Help
    elif "help" in user_input:
        return "You can ask me about greetings, my creator, top fields, or ways to earn money."

    # Exit
    elif "bye" in user_input:
        return "Goodbye! 👋 Have a great day!"

    # Default
    else:
        return "Sorry, I don't understand that."


def send_message():
    user_input = entry.get().strip()
    if user_input == "":
        return

    chat_box.config(state='normal')

    chat_box.insert(tk.END, "You: ", "user_tag")
    chat_box.insert(tk.END, user_input + "\n")

    response = get_response(user_input)
    chat_box.insert(tk.END, "Bot: ", "bot_tag")
    chat_box.insert(tk.END, response + "\n\n")

    chat_box.config(state='disabled')
    chat_box.yview(tk.END)

    entry.delete(0, tk.END)


# ===== GUI =====
window = tk.Tk()
window.title("Chatbot")
window.geometry("500x520")
window.configure(bg="#1e1e1e")

header_frame = tk.Frame(window, bg="#1e1e1e")
header_frame.pack(pady=10)

inner_frame = tk.Frame(header_frame, bg="#1e1e1e")
inner_frame.pack(anchor="center")

logo = tk.Label(inner_frame, text="🤖",
                font=("Arial", 18),
                bg="#1e1e1e", fg="white")
logo.pack(side=tk.LEFT, padx=5)

title = tk.Label(inner_frame, text="Chatbot",
                 font=("Arial", 16, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(side=tk.LEFT)

chat_box = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    state='disabled',
    bg="#2d2d2d",
    fg="white",
    font=("Arial", 10)
)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_box.tag_config("user_tag", foreground="#4CAF50")  #Green
chat_box.tag_config("bot_tag", foreground="#2196F3")   #Blue

frame = tk.Frame(window, bg="#1e1e1e")
frame.pack(fill=tk.X, padx=10, pady=5)

entry = tk.Entry(
    frame,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

send_btn = tk.Button(
    frame,
    text="Send",
    command=send_message,
    bg="#4CAF50",
    fg="white"
)
send_btn.pack(side=tk.RIGHT)

window.bind('<Return>', lambda event: send_message())

window.mainloop()
