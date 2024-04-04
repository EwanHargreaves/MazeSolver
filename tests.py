import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 5
        num_rows = 6
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
        self.assertFalse(
            m1.all_cells[0][0].has_left_wall
        )
        self.assertFalse(
            m1.all_cells[-1][-1].has_right_wall
        )
    
    def test_reset_cells_visited(self):
        m1 = Maze(num_rows=3,num_cols=3)
        m1.break_entrance_and_exit()
        m1.break_wall_r(0,0)
        m1.reset_cells_visited()
        for cell_coll in m1.all_cells:
            for cell in cell_coll:
                self.assertFalse(cell._visited)
    
if __name__ == "__main__":
    unittest.main()