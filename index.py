import tkinter as tk
from tkinter import ttk
from collections import defaultdict
import random
# Function to detect rhymes (basic multi-syllable matching)
def find_rhymes(text):
    words = text.split()
    rhymes = defaultdict(list)
    # Group words by their last 2 characters (basic rhyme logic)
    for i, word in enumerate(words):
        key = word[-2:].lower()  # Use the last 2 characters for simplicity
        rhymes[key].append((word, i))
    return {k: v for k, v in rhymes.items() if len(v) > 1}
# Function to apply color coding to rhymes
def highlight_rhymes():
    text = input_text.get("1.0", "end-1c")  # Get input text
    input_text.tag_remove("highlight", "1.0", "end")  # Clear previous highlights
    rhymes = find_rhymes(text)
    colors = {}
    # Generate a unique color for each rhyme group
    for rhyme_group in rhymes.keys():
        if rhyme_group not in colors:
            colors[rhyme_group] = f"#{random.randint(0, 0xFFFFFF):06x}"
    # Apply highlighting for each rhyme group
    for rhyme_group, words in rhymes.items():
        color = colors[rhyme_group]
        for word, index in words:
            start_idx = f"1.0 + {sum(len(w) + 1 for w in text.split()[:index])} chars"
            end_idx = f"{start_idx} + {len(word)} chars"
            input_text.tag_add(rhyme_group, start_idx, end_idx)
            input_text.tag_config(rhyme_group, background=color)
# GUI Setup
root = tk.Tk()
root.title("Multi-Syllable Rhyme Highlighter")
root.geometry("800x600")
# Input Text Area
input_text = tk.Text(root, wrap="word", font=("Arial", 14), height=20)
input_text.pack(padx=10, pady=10, fill="both", expand=True)
# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(fill="x", pady=5)
highlight_button = ttk.Button(button_frame, text="Highlight Rhymes", command=highlight_rhymes)
highlight_button.pack(side="left", padx=5)
root.mainloop()
