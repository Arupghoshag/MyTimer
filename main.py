from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    min1 = int(minute.get())
    sec1 = int(sec.get())
    count_down((min1 * 60) + sec1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        canvas.itemconfig(timer_text, text="✓", fill=GREEN, font=(FONT_NAME, 35, "bold"))

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="TIMER", font=("Arial", 24, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

minute = Entry(width=15)
minute.insert(END, string="min")
minute.grid(column=1, row=3)

sec = Entry(width=15)
sec.insert(END, string="sec")
sec.grid(column=1, row=4)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=5)

window.mainloop()
