#my etchasketch 응용 프로그램

from tkinter import *

### 변수 설정
canvas_height=400
canvas_width=600
canvas_color="black"

p1_x=canvas_width/2
p1_y=canvas_height/2
p1_color="green"
line_width=5
line_length=5

#### fuction

# user control
def p1_move_N(event):
    global p1_y

    canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width=line_width, fill=p1_color)
    p1_y=p1_y-line_length


### main
window=Tk()
window.title("myetchasketch")
canvas=Canvas(bg=canvas_color, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

window.bind("<Up>",p1_move_N)

window.mainloop()


