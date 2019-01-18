from turtle import *
import time

def setting():
    pensize(4)
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)

def nose(x, y):
    penup()
    goto(x, y)
    pendown()
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            left(3)
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)
            fd(a)
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x, y):
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x, y):
    begin_poly()
    color((255, 155, 192), "white")
    pu()
    seth(90)
    fd(-20)
    seth(0)
    fd(-95)
    pd()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()
    end_poly()
    lefteye = get_poly()
    addshape('lefteye', lefteye)
    begin_poly()
    color((255, 155, 192), "white")
    pu()
    seth(90)
    fd(-25)
    seth(0)
    fd(40)
    pd()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()
    end_poly()
    addshape('righteye', get_poly())

def cheek(x, y):
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x, y):
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def body():
    color("red", (255, 99, 71))
    pu()
    seth(90)
    fd(-20)
    seth(0)
    fd(-78)
    pd()
    begin_fill()
    seth(-130)
    circle(100, 10)
    circle(300, 30)
    seth(0)
    fd(230)
    seth(90)
    circle(300, 30)
    circle(100, 3)
    color((255, 155, 192), (255, 100, 100))
    seth(-135)
    circle(-80, 63)
    circle(-150, 24)
    end_fill()


def hand():
    color((255, 155, 192))
    pu()
    seth(90)
    fd(-40)
    seth(0)
    fd(-27)
    pd()
    seth(-160)
    circle(300, 15)
    pu()
    seth(90)
    fd(15)
    seth(0)
    fd(0)
    pd()
    seth(-10)
    circle(-20, 90)
    pu()
    seth(90)
    fd(30)
    seth(0)
    fd(237)
    pd()
    seth(-20)
    circle(-300, 15)
    pu()
    seth(90)
    fd(20)
    seth(0)
    fd(0)
    pd()
    seth(-170)
    circle(20, 90)


def foot():
    pensize(10)
    color((240, 128, 128))
    pu()
    seth(90)
    fd(-75)
    seth(0)
    fd(-180)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)
    pensize(10)
    color((240, 128, 128))
    pu()
    seth(90)
    fd(40)
    seth(0)
    fd(90)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)


def tail():
    begin_poly()
    pensize(4)
    color((255, 155, 192))
    pu()
    seth(90)
    fd(70)
    seth(0)
    fd(95)
    pd()
    seth(0)
    circle(70, 20)
    circle(10, 330)
    circle(70, 30)
    end_poly()
    t = get_poly()
    s = Shape("compound")
    s.addcomponent(t,'white','white')
    addshape('tail', s)


def whoareyou():
    penup()
    goto(-300, 200)
    pendown()
    write("啥", font=("黑体", 24, "bold"))
    time.sleep(1)
    penup()
    setheading(0)
    forward(40)
    pendown()
    write("是", font=("黑体", 24, "bold"))
    time.sleep(1)
    penup()
    forward(40)
    pendown()
    write("佩", font=("黑体", 24, "bold"))
    time.sleep(1)
    penup()
    forward(40)
    pendown()
    write("齐", font=("黑体", 24, "bold"))
    time.sleep(1)

def whoami():
    penup()
    goto(150, 200)
    pendown()
    write("这", font=("黑体", 24, "bold"))
    time.sleep(1)
    penup()
    setheading(0)
    forward(40)
    pendown()
    write("是", font=("黑体", 24, "bold"))
    time.sleep(1)
    penup()
    forward(40)
    pendown()
    write("佩", font=("黑体", 24, "bold"))
    time.sleep(1)
    penup()
    forward(40)
    pendown()
    write("齐", font=("黑体", 24, "bold"))
    time.sleep(1)


def main():
    setting()
    whoareyou()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(-10, 70)
    cheek(80, 10)
    mouth(-20, 30)
    body()
    hand()
    foot()
    tail()
    whoami()
    done()


if __name__ == '__main__':
    main()
