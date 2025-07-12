import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg
import random
import string

# App dimensions and password constraints
WIDTH, HEIGHT = 550, 340
MIN_LEN, MAX_LEN = 4, 80

# Character pools
CHAR_POOLS = {
    "upper": string.ascii_uppercase,
    "lower": string.ascii_lowercase,
    "nums": string.digits,
    "symbols": string.punctuation
}

def create_password(length, level):
    """
    Generate a secure password based on the length and selected strength level.
    """
    char_base = []
    required = []

    # Always include upper and lower case letters
    char_base.extend(CHAR_POOLS["upper"])
    char_base.extend(CHAR_POOLS["lower"])

    if level == "low":
        required.extend([
            random.choice(CHAR_POOLS["upper"]),
            random.choice(CHAR_POOLS["lower"])
        ])
    elif level == "medium":
        char_base.extend(CHAR_POOLS["nums"])
        required.extend([
            random.choice(CHAR_POOLS["upper"]),
            random.choice(CHAR_POOLS["lower"]),
            random.choice(CHAR_POOLS["nums"])
        ])
    elif level == "high":
        char_base.extend(CHAR_POOLS["nums"])
        char_base.extend(CHAR_POOLS["symbols"])
        required.extend([
            random.choice(CHAR_POOLS["upper"]),
            random.choice(CHAR_POOLS["lower"]),
            random.choice(CHAR_POOLS["nums"]),
            random.choice(CHAR_POOLS["symbols"])
        ])
    else:
        return "Error: Invalid strength level."

    if len(required) > length:
        return "Error: Length too short for selected strength."

    # Fill the rest of the password length with characters from the base pool
    extra_chars = [random.choice(char_base) for _ in range(length - len(required))]
    final_pass = required + extra_chars
    random.shuffle(final_pass)
    return "".join(final_pass)

def launch_window():
    """
    Creates and configures the main application window.
    """
    window = tk.Tk()
    window.title("SecurePass Generator")
    window.resizable(False, False)
    
    # Center the window on the screen
    x = (window.winfo_screenwidth() - WIDTH) // 2
    y = (window.winfo_screenheight() - HEIGHT) // 2
    window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
    
    ttk.Style().theme_use("clam")

    # --- KEY CHANGE 1 ---
    # Configure the window's grid. This allows the main content frame 
    # to be centered within the window space.
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    return window

def build_ui(window):
    """
    Builds and places all the UI widgets in the window.
    """
    # --- KEY CHANGE 2 ---
    # The main frame is now placed in the centered grid cell of the window.
    # We remove `sticky="nsew"` so the frame doesn't stretch, and it will
    # be centered automatically. Padding is increased for better spacing.
    frame = ttk.Frame(window, padding=20)
    frame.grid(row=0, column=0)

    # --- UI Elements ---
    
    # Title
    ttk.Label(frame, text="Password Forge", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Length Input
    ttk.Label(frame, text="Length:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)
    len_entry = ttk.Entry(frame, width=5, font=("Arial", 12))
    len_entry.insert(0, "12")
    len_entry.grid(row=1, column=1, sticky="w")

    # Strength Radio Buttons
    ttk.Label(frame, text="Strength:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5, padx=(0, 10))
    strength = tk.StringVar(value="high")
    radio_frame = ttk.Frame(frame)
    # The radio buttons now correctly align under the "Strength" label
    radio_frame.grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 15))

    for text, val in [("Low (aA)", "low"), ("Medium (aA1)", "medium"), ("High (aA1#)", "high")]:
        ttk.Radiobutton(radio_frame, text=text, variable=strength, value=val).pack(side="left", padx=(0, 15))

    # Generated Password Output
    ttk.Label(frame, text="Generated Password:", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 5))
    output = ttk.Entry(frame, width=40, font=("Courier New", 12), state="readonly")
    output.grid(row=5, column=0, columnspan=2, sticky="ew")

    # --- Callback Functions ---

    def generate():
        """Generates the password and displays it."""
        try:
            length = int(len_entry.get())
            if not (MIN_LEN <= length <= MAX_LEN):
                msg.showwarning("Input Error", f"Password length must be between {MIN_LEN} and {MAX_LEN}.")
                return

            password = create_password(length, strength.get())

            if password.startswith("Error:"):
                msg.showerror("Generation Error", password)
                return

            output.config(state="normal")
            output.delete(0, tk.END)
            output.insert(0, password)
            output.config(state="readonly")

        except ValueError:
            msg.showwarning("Input Error", "Please enter a valid number for password length.")
        except Exception as err:
            msg.showerror("Error", str(err))

    def copy_password():
        """Copies the generated password to the clipboard."""
        password = output.get()
        if not password:
            msg.showwarning("No Password", "Generate a password first before copying.")
            return
        window.clipboard_clear()
        window.clipboard_append(password)
        msg.showinfo("Copied", "Password copied to clipboard!")

    # --- KEY CHANGE 3 ---
    # A container for the buttons to place them side-by-side.
    # This makes the layout more compact and reduces vertical whitespace.
    button_container = ttk.Frame(frame)
    button_container.grid(row=6, column=0, columnspan=2, pady=(20, 0))

    # Add buttons to the container
    ttk.Button(button_container, text="FORGE PASSWORD", command=generate).pack(side="left", padx=5)
    ttk.Button(button_container, text="COPY PASSWORD", command=copy_password).pack(side="left", padx=5)

    return len_entry, strength, output

if __name__ == "__main__":
    root = launch_window()
    build_ui(root)
    root.mainloop()
