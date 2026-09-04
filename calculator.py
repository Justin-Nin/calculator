import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = [ "÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_gray = "#3b3d45"
color_blue = "#4a69bd"
color_black = "#000000"
color_white = '#ffffff'
#window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Roboto", 45), background=color_black, foreground=color_white, anchor='e')

label.grid(row=0, column=0, columnspan=column_count, sticky='we')

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Roboto", 30),
                                width=column_count-1, height=1, 
                                command=lambda value=value: button_click(value))
        if value in top_symbols:
            button.configure(foreground=color_white, background=color_black)
        elif value in right_symbols:
            button.configure(foreground=color_white, background=color_blue)
        else:
            button.configure(foreground=color_white, background=color_gray)

        button.grid(row=row+1, column=column)
    
frame.pack()

def button_click(value):
    pass

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()

# fart