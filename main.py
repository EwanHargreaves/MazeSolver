from window import Window
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(win)
    maze.break_entrance_and_exit()
    win.wait_for_close()


main()