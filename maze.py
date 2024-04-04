from cell import Cell
from point import Point
import time
import random

class Maze:
    def __init__(
            self,
            window=None,
            x1=10, y1=10,
            num_rows=19, num_cols=26,
            cell_size_x=30, cell_size_y=30,seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        self.create_cells()
        self._seed = random.seed(seed)
    
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

    def break_wall_r(self, i, j):
            self.all_cells[i][j]._visited = True

            while True:
                left = [i-1,j] if i-1 >= 0 else None
                right = [i+1,j] if i+1 < len(self.all_cells) else None
                up = [i,j-1] if j-1 >= 0 else None
                down = [i,j+1] if j+1 < len(self.all_cells[0]) else None
                directions = [up,down,left,right]

                unvisited_directions = list(filter(lambda x: x and not self.all_cells[x[0]][x[1]]._visited, directions))

                if not unvisited_directions:
                    self.draw_cell(self.all_cells[i][j],0.05)
                    return

                random_direction = random.choice(unvisited_directions)

                if random_direction == left:
                    self.all_cells[i][j].has_left_wall = False
                    self.all_cells[i-1][j].has_right_wall = False

                if random_direction == right:
                    self.all_cells[i][j].has_right_wall = False
                    self.all_cells[i+1][j].has_left_wall = False

                if random_direction == up:
                    self.all_cells[i][j].has_top_wall = False
                    self.all_cells[i][j-1].has_bottom_wall = False

                if random_direction == down:
                    self.all_cells[i][j].has_bottom_wall = False
                    self.all_cells[i][j+1].has_top_wall = False
                    
                self.break_wall_r(random_direction[0],random_direction[1])
                

    def draw_all_cells(self):
        if self.all_cells is None: raise ValueError("Cells list not set before draw")
        if self._win is None : return #Testing

        for cell_col in self.all_cells:
            for cell in cell_col:
                self.draw_cell(cell,0.005)
    
    def draw_cell(self,cell,speed = None):
        cell.draw()
        if self._win: self._win.redraw()
        if speed: time.sleep(speed)
            
    def break_entrance_and_exit(self):
        self.all_cells[0][0].has_left_wall = False
        self.all_cells[-1][-1].has_right_wall = False

        if self._win:
            self.all_cells[0][0].draw()
            self.all_cells[-1][-1].draw()
    
    def reset_cells_visited(self):
        for cell_coll in self.all_cells:
            for cell in cell_coll:
                cell._visited = False
