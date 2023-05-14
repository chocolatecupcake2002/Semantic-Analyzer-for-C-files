import tkinter as tk
from tkinter import filedialog
import subprocess
import os

# Color scheme
BG_COLOR = "#2b2d42"  # Dark blue
FG_COLOR = "#fff"  # White
BUTTON_BG_COLOR = "#8d99ae"  # Light blue
BUTTON_FG_COLOR = "#000"  # Black
OUTPUT_BG_COLOR = "#fff"  # White
OUTPUT_FG_COLOR = "#000"  # Black

def compile_source():
    source_file = filedialog.askopenfilename(filetypes=[("C Files", "*.txt")])
    if source_file:
        command = ["python", "compiler.py", source_file]
        cwd = os.path.dirname(os.path.abspath(__file__))
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
        output_text.delete(1.0, tk.END)  # Clear the previous output
        output_text.insert(tk.END, result.stdout)
        if result.stderr:
            output_text.insert(tk.END, result.stderr)

# Create the GUI window
window = tk.Tk()
window.title("C Compiler")
window.configure(bg=BG_COLOR)

# Create a label for the semantic analyzer
label = tk.Label(window, text="Semantic Analyzer", font=("Arial", 16), bg=BG_COLOR, fg=FG_COLOR)
label.pack(pady=10)

# Create a button to select the source file
select_file_button = tk.Button(window, text="Select Source File", command=compile_source, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
select_file_button.pack(pady=10)

# Create an output area
output_text = tk.Text(window, height=30, width=70, bg=OUTPUT_BG_COLOR, fg=OUTPUT_FG_COLOR)
output_text.pack(padx=10, pady=10)

# Run the GUI event loop
window.mainloop()
