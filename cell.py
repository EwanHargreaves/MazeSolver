from point import Point
from line import Line
import time

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win =window
        self._setup = None
        self._visited = False
    
    def set_points(self,point1,point2):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y
        self._setup = True

    def draw(self):
        if not self._setup: raise ValueError("Points for cell not set before draw")
        if not self._win: return #testing

        top_left = Point(self._x1,self._y1)
        top_right = Point(self._x2,self._y1)
        bottom_left = Point(self._x1,self._y2)
        bottom_right = Point(self._x2,self._y2)

        colour = lambda wall_state: "black" if wall_state else "white"

        left_wall = Line(top_left,bottom_left)
        self._win.draw_line(left_wall,colour(self.has_left_wall))

        right_wall = Line(top_right,bottom_right)
        self._win.draw_line(right_wall,colour(self.has_right_wall))

        top_wall = Line(top_left,top_right)
        self._win.draw_line(top_wall,colour(self.has_top_wall))

        bottom_wall = Line(bottom_left,bottom_right)
        self._win.draw_line(bottom_wall,colour(self.has_bottom_wall))


        
    def draw_move(self, to_cell, undo=False):
        if not self._win: return #testing
        start_point = self.get_centre_point()
        end_point = to_cell.get_centre_point()
        colour = "gray" if undo else "red"
        self._win.draw_line(Line(start_point,end_point),colour)
        self._win.redraw()
        time.sleep(0.05)
    
    def get_centre_point(self):
        return Point((self._x1 + self._x2)/2,(self._y1 + self._y2)/2)



