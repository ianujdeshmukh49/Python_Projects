from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    window.after_cancel(timer)
    canvas.itemconfig(time_label,text="00:00")
    global reps
    reps = 0 
    timer_label.config(text="Timer",fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked():
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps+=1

    if reps%8 == 0:
        timer_label.config(text="Break!",fg=RED)
        count_down(long_break_sec)
    elif reps%2 == 0:
        timer_label.config(text="Break!",fg=PINK)
        count_down(1)
    else:
        timer_label.config(text="Work",fg=GREEN)
        count_down(1)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
import math

def count_down(count):

    minutes = math.floor(count/60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(time_label,text=f"{minutes}:{seconds}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_clicked()
        temp = int(reps/2)
        tick_label.config(text="✔️"*temp)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)



# Canvas setup
canvas = Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)

# Image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
time_label = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


# Buttons

start_button = Button(text="start",command=start_clicked)
start_button.grid(column=0,row=8)


reset_button = Button(text="reset",command=reset_clicked)
reset_button.grid(column=4,row=8)

#Labels
# text="✔️"
tick_label = Label(fg=GREEN,bg=YELLOW,font=("Arial",15,"bold"))
tick_label.grid(column=2,row=9)

timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=("Arial",35,"bold"))
timer_label.grid(column=2,row=0)


window.mainloop()