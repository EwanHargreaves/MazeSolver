from window import Window
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(win,num_rows = 5, num_cols = 5)
    maze.break_entrance_and_exit()
    maze.break_wall_r(0,0)
    maze.reset_cells_visited()
    win.wait_for_close()


main()