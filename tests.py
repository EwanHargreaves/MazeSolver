import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(None,0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            len(m1.all_cells),
            num_cols
        )
        self.assertEqual(
            len(m1.all_cells[0]),
            num_rows
        )
    
    def test_entrance_and_exit(self):
        m1 = Maze(None,0,0,5,5,10,10)
        m1.break_entrance_and_exit()
        self.assertEqual(
            m1.all_cells[0][0].has_left_wall,
            False
        )
        self.assertEqual(
            m1.all_cells[-1][-1].has_right_wall,
            False
        )
    
if __name__ == "__main__":
    unittest.main()