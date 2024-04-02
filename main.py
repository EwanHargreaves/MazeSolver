from window import Window
from point import Point
from line import Line

def main():
    width = 800
    height = 600
    win = Window(width, height)
    
    point1 = Point(0,0)
    point2 = Point(width, height)
    line = Line(point1, point2)
    win.draw_line(line, "black")

    win.wait_for_close()


main()