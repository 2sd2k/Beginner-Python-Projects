import tkinter as tk
import math

calculation = ""
cursor_pos = 0


def update_display():
    global calculation, cursor_pos
    # Create display string with cursor
    display_text = calculation[:cursor_pos] + "|" + calculation[cursor_pos:]
    text_result.config(state="normal")
    text_result.delete(0, "end")
    text_result.insert(0, display_text)
    text_result.config(state="readonly")

def add_to_calculation(symbol):
    global calculation, cursor_pos
    # Insert symbol at cursor position
    calculation = calculation[:cursor_pos] + str(symbol) + calculation[cursor_pos:]
    cursor_pos += 1
    update_display()


def evaluate_calculation():
    global calculation, cursor_pos
    try:
        # Add implicit multiplication for patterns like "9cos(5)", "9√(16)", and "5e^2"
        import re
        processed = re.sub(r'(\d)(sin|cos|tan|√|log|ln|e\^)\(', r'\1*\2(', calculation)
        processed = re.sub(r'(\d)(π)', r'\1*\2', processed)
        # Replace √ with sqrt for evaluation
        processed = processed.replace('√', 'sqrt')
        # Replace ^ with ** for exponentiation
        processed = processed.replace('^', '**')
        calculation = str(eval(processed, {"__builtins__": None},
                                            {"sqrt": math.sqrt, "pow": pow, "sin": math.sin, 
                                             "cos": math.cos, "tan": math.tan, "e": math.e,
                                             "log": math.log10, "ln": math.log, "π": math.pi}))
        cursor_pos = len(calculation)
        update_display()
    except:
        clear_field()
        text_result.config(state="normal")
        text_result.insert(0, "Error")
        text_result.config(state="readonly")


def clear_field():
    global calculation, cursor_pos
    calculation = ""
    cursor_pos = 0
    update_display()

def backspace():
    global calculation, cursor_pos
    if cursor_pos > 0:
        calculation = calculation[:cursor_pos-1] + calculation[cursor_pos:]
        cursor_pos -= 1
        update_display()

def sin_value():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "sin(" + calculation[cursor_pos:] + ")"
    cursor_pos += 4
    update_display()

def cos_value():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "cos(" + calculation[cursor_pos:] + ")"
    cursor_pos += 4
    update_display()

def tan_value():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "tan(" + calculation[cursor_pos:] + ")"
    cursor_pos += 4
    update_display()

def sqr_root():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "√(" + calculation[cursor_pos:] + ")"
    cursor_pos += 2
    update_display()

def e_power():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "e^(" + calculation[cursor_pos:] + ")"
    cursor_pos += 3
    update_display()

def x_power():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "^(" + calculation[cursor_pos:] + ")"
    cursor_pos += 2
    update_display()

def log_value():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "log(" + calculation[cursor_pos:] + ")"
    cursor_pos += 4
    update_display()

def natural_log():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "ln(" + calculation[cursor_pos:] + ")"
    cursor_pos += 3
    update_display()

def pi_value():
    global calculation, cursor_pos
    calculation = calculation[:cursor_pos] + "π" + calculation[cursor_pos:]
    cursor_pos += 1
    update_display()

def move_cursor_left():
    global cursor_pos
    if cursor_pos > 0:
        cursor_pos -= 1
        update_display()

def move_cursor_right():
    global cursor_pos
    if cursor_pos < len(calculation):
        cursor_pos += 1
        update_display()

def on_key_press(event):
    key = event.keysym
    
    # Numbers
    if key in "0123456789":
        add_to_calculation(key)
    # Plus key
    elif key == "plus":
        add_to_calculation("+")
    # Minus key
    elif key == "minus":
        add_to_calculation("-")
    # Multiply key
    elif key == "asterisk":
        add_to_calculation("*")
    # Divide key
    elif key == "slash":
        add_to_calculation("/")
    # Left parenthesis
    elif key == "parenleft":
        add_to_calculation("(")
    # Right parenthesis
    elif key == "parenright":
        add_to_calculation(")")
    # Decimal point
    elif key == "period":
        add_to_calculation(".")
    # Enter key evaluates
    elif key == "Return":
        evaluate_calculation()
    # Backspace key
    elif key == "BackSpace":
        backspace()
    # Escape or Delete key clears
    elif key in ["Escape", "Delete"]:
        clear_field()
    # Arrow keys for cursor movement
    elif key == "Left":
        move_cursor_left()
    elif key == "Right":
        move_cursor_right()
    # Letter keys for functions
    elif key == "e":
        add_to_calculation("e")
    elif key == "l":
        add_to_calculation("l")
    elif key == "o":
        add_to_calculation("o")
    elif key == "g":
        add_to_calculation("g")
    elif key == "n":
        add_to_calculation("n")
    elif key == "asciicircum":  # ^ key
        add_to_calculation("^")


# --- UI Setup ---
root = tk.Tk()
root.title("Python Calculator")

text_result = tk.Entry(root, font=("Arial", 24), justify="right", bd=8, relief="ridge", state="readonly")
text_result.grid(row=0, column=0, columnspan=5, pady=10, sticky="nsew")

# Button layout
buttons = [
    ("√", 1, 0), ("sin", 1, 1), ("cos", 1, 2), ("tan", 1, 3), ("CE", 1, 4),
    ("eˣ", 2, 0), ("7", 2, 1), ("8", 2, 2), ("9", 2, 3), ("/", 2, 4),
    ("xʸ", 3, 0), ("4", 3, 1), ("5", 3, 2), ("6", 3, 3), ("*", 3, 4),
    ("log", 4, 0), ("1", 4, 1), ("2", 4, 2), ("3", 4, 3), ("-", 4, 4),
    ("ln", 5, 0), ("0", 5, 1), (".", 5, 2), ("(-)", 5, 3), ("+", 5, 4),
    ("π", 6, 0), ("DEL", 6, 1), ("(", 6, 2), (")", 6, 3), ("=", 6, 4)    
]

#Connect each button with its respective function
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=evaluate_calculation, bg="#4CAF50", fg="white")
    elif text == "CE":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=clear_field, bg="#f44336", fg="white")
    elif text == "DEL":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=backspace)
    elif text == "sin":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=sin_value)
    elif text == "cos":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=cos_value)
    elif text == "tan":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=tan_value)
    elif text == "√":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=sqr_root)
    elif text == "eˣ":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=e_power)
    elif text == "xʸ":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=x_power)
    elif text == "log":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=log_value)
    elif text == "ln":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=natural_log)
    elif text == "π":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=pi_value)  
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: add_to_calculation(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# --- Make grid cells expand when window resizes ---
for i in range(7):   # 0–5 rows (entry + 5 button rows)
    root.grid_rowconfigure(i, weight=1)
for j in range(5):   # 4 columns
    root.grid_columnconfigure(j, weight=1)

# Bind keyboard events
root.bind("<KeyPress>", on_key_press)
root.focus_set()  # Ensure the window can receive keyboard events

# Initial display
update_display()

root.mainloop()