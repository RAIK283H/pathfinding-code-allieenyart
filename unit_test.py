import math
import unittest
import graph_data
import global_game_data
from pathing import get_bfs_path, get_dfs_path


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_dfs_path(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 2}

        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 3]],
                1: [(1, 0), [0, 2]],
                2: [(2, 0), [1, 4]],
                3: [(0, -1), [0, 4]],
                4: [(1, -1), [3, 2]]
            }
        }
 
    expected_path = [0, 1, 2, 4]
    result_path = get_dfs_path()
    self.assertEqual(result_path, expected_path, "the DFS path wasn't right")

    def test_bfs_path(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 2}

        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 3]],
                1: [(1, 0), [0, 2]],
                2: [(2, 0), [1, 4]],
                3: [(0, -1), [0, 4]],
                4: [(1, -1), [3, 2]]
            }
        }
 
    expected_path = [0, 1, 2, 4]
    result_path = get_bfs_path()
    self.assertEqual(result_path, expected_path, "the BFS path wasn't right")




if __name__ == '__main__':
    unittest.main()
