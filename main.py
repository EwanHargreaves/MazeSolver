from window import Window
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(win)
    maze.break_entrance_and_exit()
    maze.break_wall_r(0,0)
    maze.reset_cells_visited()
    maze.solve()
    win.wait_for_close()


main()