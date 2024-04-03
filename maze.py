from cell import Cell
from point import Point
import time

class Maze:
    def __init__(
            self,
            window=None,
            x1=10, y1=10,
            num_rows=19, num_cols=26,
            cell_size_x=30, cell_size_y=30
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        self.create_cells()
    
    def create_cells(self):
        self.all_cells = []
        for col in range(self._num_cols):
            cell_col =[]
            for row in range(self._num_rows):
                cell = Cell(self._win)

                x1 = self._x1 + self._cell_size_x * col
                y1 = self._y1 + self._cell_size_y * row
                point1 = Point(x1,y1)

                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                point2 = Point(x2,y2)
                
                cell.set_points(point1,point2)
                cell_col.append(cell)
            self.all_cells.append(cell_col)
        
        self.draw_all_cells()

        

    def draw_all_cells(self):
        if self.all_cells is None: raise ValueError("Cells list not set before draw")

        if self._win is None : return #Testing
        for cell_col in self.all_cells:
            for cell in cell_col:
                cell.draw()
                self._win.redraw()
                #time.sleep(0.05)
            
    def break_entrance_and_exit(self):
        self.all_cells[0][0].has_left_wall = False
        self.all_cells[-1][-1].has_right_wall = False

        if self._win:
            self.all_cells[0][0].draw()
            self.all_cells[-1][-1].draw()

                

    