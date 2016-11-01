# 이 클래스는 tale의 처리 공간을 2d 직사각형으로 정의합니다.
from tkinter import *

class Table:
    ### 생성자
    def __init__(self, window, colour = "black", net_colour="green",
                 width=600, height=400, vertical_net=False, horizontal_net=False):
        self.width=width
        self.height=height
        self.colour=colour


        self.canvas = Canvas(window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.pack()

#캔버스에 네트 추가
        if (vertical_net):
            self.canvas.create_line(self.width/2,0, self.width/2,
                            self.height,width=2, fill=net_colour, dash=(15,23))

        if (horizontal_net):
            self.canvas.create_line(0, self.height/2, self.width, self.height/2,
                                width=2, fill=net_colour, dash=(15,23))

#캔바스에 직사각형을 추가하는 도구
        def draw_rectangle(self, rectangle):
            x1=rectangle.x_posn
            x2=rectangle.x_posn+rectangle.width
            y1=rectangle.y_posn
            y2=rectangle.y_posn+rectangle.height
            c=rectangle.colour
            return self.canvas.create_rec   (x1, y1, x2, y2, fill=c)

# 캔바스에 타원을 추ㅏ하는 도구
        def draw_oval(self, oval):
            x1=oval.x_posn
            x2=oval.x_posn+oval.width
            y1=oval.y_posn
            y2=oval.y_posn+oval.height
            c=oval.colour
            return self.canvas.create_oval(x1, y1, x2, y2, fill=c)

# 캔바스에 아이템을 조작할 수 있는 도구
        def move_item(self, item, x1, y1, x2, y2):
            self.canvas.coords(item, x1, y1, x2, y2)

        def remove_item(self, item):
            self.canvas.delete(item)

        def change_item_colour(self, item, c):
            self.canvas.itemconfigure(item,fill=c)