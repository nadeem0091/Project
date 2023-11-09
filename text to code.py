import tkinter as tk
from tkinter import ttk
import pyperclip
import csv
import webbrowser

# Function to generate HTML output
def generate_html_output():
    user_input = input_field.get()
    output_text.delete(1.0, tk.END)
    html_code = description_to_html_code.get(user_input)
    if html_code is None:
        output_text.insert(tk.END, "The description was not found in the dataset.")
    else:
        output_text.insert(tk.END, html_code)

# Function to copy output to clipboard
def copy_output():
    output = output_text.get(1.0, tk.END)
    pyperclip.copy(output)

# Function to open the HTML in a web browser
def open_in_browser():
    user_input = input_field.get()
    html_code = description_to_html_code.get(user_input)
    if html_code:
        # Save the HTML to a temporary file
        with open("temp.html", "w") as temp_file:
            temp_file.write(html_code)
        # Open the HTML file in a web browser
        webbrowser.open("temp.html")
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "HTML not found in the dataset.")

# Load the dataset
def load_dataset(file_path):
    dataset = {}
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            text_description = row[0]
            html_code = row[1]
            dataset[text_description] = html_code
    return dataset

# Create the main window
root = tk.Tk()
root.title("HTML Code Generator")

# Style the GUI
style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
style.configure("TEntry", background="#fff", font=("Arial", 12))
style.configure("TButton", background="#007bff", foreground="white", font=("Arial", 12))
style.configure("TText", background="#fff", font=("Arial", 12))

# Main frame
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=tk.BOTH, expand=1)

# Input section
input_label = ttk.Label(main_frame, text="Enter a description:")
input_label.grid(row=0, column=0, sticky=tk.W, pady=5)

input_field = ttk.Entry(main_frame, width=50)
input_field.grid(row=0, column=1, sticky=tk.E, pady=5)

generate_button = ttk.Button(main_frame, text="Generate HTML", command=generate_html_output)
generate_button.grid(row=1, column=0, sticky=tk.W, pady=5)

# Output section
output_text = tk.Text(main_frame, height=10, width=60, wrap="word")
output_text.grid(row=2, column=0, columnspan=2, sticky=tk.EW, pady=5)

# Action buttons
copy_button = ttk.Button(main_frame, text="Copy Output", command=copy_output)
copy_button.grid(row=3, column=0, sticky=tk.W, pady=5)

open_in_browser_button = ttk.Button(main_frame, text="Open in Browser", command=open_in_browser)
open_in_browser_button.grid(row=3, column=1, sticky=tk.E, pady=5)

# Load the dataset
file_path = "D:\project\dataset HTMLTOCODE.csv"  # replace with the actual path to your dataset CSV file
description_to_html_code = load_dataset(file_path)

# Run the Tkinter event loop
root.mainloop()
