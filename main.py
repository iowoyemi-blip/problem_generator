# File: main.py

import tkinter as tk
from tkinter import ttk
from problem_generator import TOPICS # Import our topics dictionary

# --- Global variables to hold the current problem and answer ---
current_problem = ""
current_answer = ""

# --- Functions to handle button clicks ---
def handle_generate():
    """Gets a new problem and displays it."""
    global current_problem, current_answer
    
    # Get the selected topic from the dropdown
    selected_topic = topic_selector.get()
    
    # Get the corresponding generator function from the TOPICS dictionary
    generator_func = TOPICS[selected_topic]
    
    # Generate a new problem and answer
    current_problem, current_answer = generator_func()
    
    # Update the labels on the screen
    problem_label.config(text=current_problem)
    answer_label.config(text="") # Hide the old answer

def handle_show_answer():
    """Displays the answer to the current problem."""
    answer_label.config(text=f"Answer: {current_answer}")


# --- Set up the main application window ---
window = tk.Tk()
window.title("Algebra I 'Do Now' Generator")
window.geometry("500x350") # Set the window size

# --- Create and place the UI elements ---
# Frame for better organization
main_frame = ttk.Frame(window, padding="20")
main_frame.pack(expand=True, fill="both")

# Title Label
title_label = ttk.Label(main_frame, text="Select a Topic", font=("Helvetica", 16))
title_label.pack(pady=10)

# Dropdown menu for topic selection
topic_selector = ttk.Combobox(main_frame, values=list(TOPICS.keys()), font=("Helvetica", 12))
topic_selector.pack(pady=10)
topic_selector.current(0) # Set the default selection to the first item

# Generate Problem Button
generate_button = ttk.Button(main_frame, text="Generate Problem", command=handle_generate)
generate_button.pack(pady=10)

# Label to display the problem
problem_label = ttk.Label(main_frame, text="Click 'Generate Problem' to start!", font=("Helvetica", 14, "bold"))
problem_label.pack(pady=20)

# Show Answer Button
answer_button = ttk.Button(main_frame, text="Show Answer", command=handle_show_answer)
answer_button.pack(pady=5)

# Label to display the answer
answer_label = ttk.Label(main_frame, text="", font=("Helvetica", 14))
answer_label.pack(pady=10)

# --- Start the application ---
window.mainloop()