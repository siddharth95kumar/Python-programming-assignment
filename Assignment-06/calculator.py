import tkinter as tk

# --------------- Window setup ---------------
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("340x420")      # window size (optional)
root.resizable(False, False)  # fixed size

# StringVar display ke liye (Entry me dikhega)
expr = tk.StringVar()

# --------------- Display (Entry) ---------------
entry = tk.Entry(root, textvariable=expr, font=('Arial', 22), bd=10, relief='sunken', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='we')

# --------------- Functions ---------------
def add_to_expression(char):
    """Button press se expression me character jodna."""
    expr.set(expr.get() + str(char))

def clear_expression():
    """C button — poora clear."""
    expr.set('')

def backspace():
    """⌫ button — last character hatao."""
    expr.set(expr.get()[:-1])

def evaluate_expression():
    """= button — expression evaluate karo (error handle ke saath)."""
    try:
        # agar user ne unicode ×/÷ use kiya ho toh convert kar do
        expression = expr.get().replace('×', '*').replace('÷', '/')
        # NOTE: simple local calculator: eval use kiya hai.
        result = eval(expression)
        expr.set(str(result))
    except Exception:
        expr.set('Error')

# --------------- Buttons layout ---------------
# Make grid expandable-looking by assigning weights
for r in range(1, 6):
    root.grid_rowconfigure(r, weight=1)
for c in range(4):
    root.grid_columnconfigure(c, weight=1)

# Row buttons (rows 1..4)
rows = [
    ['C', '⌫', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
]

for r_index, row in enumerate(rows, start=1):
    for c_index, ch in enumerate(row):
        if ch == 'C':
            cmd = clear_expression
        elif ch == '⌫':
            cmd = backspace
        elif ch == '=':
            cmd = evaluate_expression
        else:
            # digits/operators
            cmd = lambda ch=ch: add_to_expression(ch)

        btn = tk.Button(root, text=ch, font=('Arial', 18), command=cmd)
        btn.grid(row=r_index, column=c_index, sticky='nsew', padx=3, pady=3)

# Last row: 0 (spans 2 cols), '.', '='
btn0 = tk.Button(root, text='0', font=('Arial', 18), command=lambda: add_to_expression('0'))
btn0.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=3, pady=3)

btndot = tk.Button(root, text='.', font=('Arial', 18), command=lambda: add_to_expression('.'))
btndot.grid(row=5, column=2, sticky='nsew', padx=3, pady=3)

btneq = tk.Button(root, text='=', font=('Arial', 18), command=evaluate_expression)
btneq.grid(row=5, column=3, sticky='nsew', padx=3, pady=3)

# --------------- Keyboard support (optional) ---------------
def on_key(event):
    ch = event.char
    # allow digits, operators and parentheses
    if ch in '0123456789.+-*/%()':
        add_to_expression(ch)
    elif event.keysym == 'Return':
        evaluate_expression()
    elif event.keysym == 'BackSpace':
        backspace()
    elif event.keysym == 'Escape':
        clear_expression()

root.bind('<Key>', on_key)

# Start the app
entry.focus_set()  # cursor in entry by default
root.mainloop()
