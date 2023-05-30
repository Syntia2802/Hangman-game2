import tkinter as tk

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_next_prime():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def on_button_click():
    global color_index
    color = colors[color_index]
    label.config(text=str(next(next_prime)), fg=color)
    color_index = (color_index + 1) % len(colors)

next_prime = get_next_prime()
colors = ["red", "orange", "yellow", "green", "blue", "purple", "gold", "pink", "black", "brown"]
color_index = 0

root = tk.Tk()
root.title("Prime numbers")

label = tk.Label(root, text="2")
label.pack()

button = tk.Button(root, text="Next", command=on_button_click)
button.pack()

root.mainloop()
