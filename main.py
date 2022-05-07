from tkinter import *
from tkinter import ttk


def home():
    global home_frame
    home_frame = ttk.Frame(root, padding=30)
    home_frame.grid()

    # Title Label
    ttk.Label(home_frame, text="Welcome to the Most Dangerous Writing App!", font=('Impact', '40', 'normal')).grid(
        column=0,
        row=0, columnspan=2)

    # Description Label
    ttk.Label(home_frame, text="If you stop writing, all of your progress will be lost. Be careful.",
              font=('Verdana', '20', 'normal'), padding=10).grid(column=0, row=1, columnspan=2)

    # Ready Button
    ttk.Button(home_frame, text="Ready?", command=lambda: start('', txt_box), padding=30).grid(column=0, row=3)

    # Quit Game Button
    ttk.Button(home_frame, text="Quit", command=root.destroy, padding=30).grid(column=1, row=3)


def start(str, txt_box):
    print("Start Function Called")
    home_frame.destroy()


    window_width = 800
    window_height = 700
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    start_frame = ttk.Frame(root, padding=30)
    start_frame.grid()

    if n == 0:
        # Title Label
        ttk.Label(start_frame, text="Welcome to the Most Dangerous Writing App!", font=('Impact', '40', 'normal')).grid(
            column=0,
            row=0, columnspan=2)

        # Description Label
        ttk.Label(start_frame, text="If you stop writing, all of your progress will be lost. Be careful.",
                  font=('Verdana', '20', 'normal'), padding=10).grid(column=0, row=1, columnspan=2)

    # Input
    if txt_box == None:
        textBox = Text(start_frame, width=66, height=25, font=('American Typewriter', '16', 'normal'))
    else:
        textBox = txt_box

    textBox.grid(column=0, row=2)
    textBox.insert(1.0, str)
    textBox.after(10000, lambda: update_typing(str_input=textBox.get(1.0, 'end-1c'), text_box=textBox))
    textBox.focus()

    # Quit Game Button
    ttk.Button(start_frame, text="Quit", command=root.destroy, padding=30).grid(column=0, row=4)


def update_typing(str_input, text_box):
    global n, prev_str
    print(f"str_input:{str_input}")
    print(f"prev_str:{prev_str}")
    if n == 0:
        print("If statement started")
        prev_str = str_input
        print(f"prev_str:{prev_str}")
        n += 1
    elif n > 0:
        print("elif started")
        if str_input == prev_str:
            print(f"str_input:{str_input}")
            print(f'pre_input:{prev_str}')
            str_input = ''
            prev_str = ''
        else:
            prev_str = str_input
    text_box.delete(1.0, 'end-1c')
    start(str_input, text_box)


txt_box = None
prev_str = ''
n = 0
root = Tk()
root.title("Most Dangerous Writing")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 800
window_height = 250
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

home()

root.mainloop()
