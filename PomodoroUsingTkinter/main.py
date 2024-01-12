from tkinter import *

# --------------------------------------- CONSTANTS --------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BRAKE_MIN = 20
reps = 0
checkmark = ""
timer = None

# --------------------------------- TIMER RESET -------------------------------------- #


def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")

# --------------------------------- TIMER MECHANISM ---------------------------------- #


def start_timer():
    global reps
    global checkmark
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BRAKE_MIN * 60
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Long Brake", fg=YELLOW)
        count_down(long_brake_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Brake", fg=GREEN)
        count_down(short_break_sec)
    elif reps % 2 != 0:
        timer_label.config(text="Work", fg=RED)
        count_down(work_sec)


# --------------------------------- COUNTDOWN MECHANISM ------------------------------ #


def count_down(count):
    global checkmark
    global timer
    min_count = count // 60
    sec_count = count % 60
    if min_count < 10:
        min_count = f"0{min_count}"
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark += "✔"
            checkmark_label.config(text=checkmark)
        elif reps % 8 == 0:
            pass


# --------------------------------- UI SETUP ----------------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=PINK)

canvas = Canvas(width=350, height=338, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato1.png")
canvas.create_image(175, 169, image=tomato_img)
timer_text = canvas.create_text(175, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=PINK, font=(FONT_NAME, 50, "normal"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 20, "normal"))
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
