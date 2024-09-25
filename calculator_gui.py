import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Entry widget to display calculations
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, insertwidth=4, bg="powder blue", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button definitions
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create buttons and place them in the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18),
                      command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:  # Reset column value after 4 buttons
                col_val = 0
                row_val += 1

        # Clear button
        tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear).grid(row=row_val, column=0)

    def on_button_click(self, char):
        if char == '=':
            try:
                # Evaluate the expression and show the result
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            # Append the character to the entry
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text + char)

    def clear(self):
        self.entry.delete(0, tk.END)  # Clear the entry field

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
