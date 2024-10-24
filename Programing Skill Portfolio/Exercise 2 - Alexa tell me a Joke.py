# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:33:57 2024

@author: Earl
"""

import tkinter as tk
import random

# List of jokes
jokes = [
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
    ("Why don't scientists trust atoms?", "Because they make up everything!"),
    ("What do you call fake spaghetti?", "An impasta!"),
    ("Why did the bicycle fall over?", "Because it was two-tired!"),
    ("What did one wall say to the other wall?", "I'll meet you at the corner!"),
    ("Why was the math book sad?", "Because it had too many problems!"),
]

class JokeApp:
    def __init__(self, master):
        self.master = master
        master.title("Joke Teller")

        self.joke_label = tk.Label(master, text="", wraplength=300)
        self.joke_label.pack(pady=20)

        self.punchline_label = tk.Label(master, text="", wraplength=300)
        self.punchline_label.pack(pady=20)

        self.setup_button = tk.Button(master, text="Tell me a joke", command=self.display_joke)
        self.setup_button.pack(pady=10)

        self.punchline_button = tk.Button(master, text="Show punchline", command=self.show_punchline)
        self.punchline_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

        self.current_joke = None

    def display_joke(self):
        self.current_joke = random.choice(jokes)
        self.joke_label.config(text=self.current_joke[0])
        self.punchline_label.config(text="")
    
    def show_punchline(self):
        if self.current_joke:
            self.punchline_label.config(text=self.current_joke[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()
