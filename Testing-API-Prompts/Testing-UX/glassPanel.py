import tkinter as tk

def on_button_click():
    """Changes the button text to 'Successful'."""
    button.config(text="Successful")

# --- Main Application Window ---
root = tk.Tk()
root.title("Glass Panel")  # Title is not visible in frameless mode

# --- Panel Appearance ---
# Make the window frameless for a panel-like appearance
root.overrideredirect(True)

# Set window transparency (0.0 = fully transparent, 1.0 = fully opaque)
# This makes the entire panel semi-transparent
root.attributes('-alpha', 0.85)  # Adjust 0.85 for desired "glassiness"

# Set a background color for the panel.
# This color will appear semi-transparent due to the -alpha attribute.
root.config(bg="#D0D0D0")  # A light grey

# --- Button Widget ---
button = tk.Button(
    root,
    text="Click here",
    command=on_button_click,
    font=("Arial", 14, "bold"),
    bg="#EAEAEA",          # Button background color
    fg="#333333",          # Button text color
    activebackground="#C0C0C0", # Button background color when clicked
    activeforeground="#000000", # Button text color when clicked
    relief=tk.FLAT,
    padx=20,
    pady=10,
    cursor="hand2"
)
# Place the button in the center of the panel
button.pack(expand=True, padx=40, pady=30)

# --- Draggability for the Frameless Window ---
# These functions allow the frameless window to be moved with the mouse.

def start_move(event):
    """Records the initial mouse position."""
    root.x = event.x
    root.y = event.y

def do_move(event):
    """Moves the window based on mouse movement."""
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

# Bind mouse events for dragging to the root window (the panel itself)
root.bind("<ButtonPress-1>", start_move)
root.bind("<B1-Motion>", do_move)

# Set initial size and position of the panel
root.geometry("300x200+300+300")  # width x height + x_offset + y_offset

root.mainloop()