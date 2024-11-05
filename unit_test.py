import math
import unittest
import graph_data
import global_game_data
from pathing import get_bfs_path, get_dfs_path
from permutation import find_hamiltonian_cycles, get_perms_sjt


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

    def test_bfs_path_2(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 4}

        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 3]],
                1: [(1, 0), [0, 2]],
                2: [(2, 0), [1, 4]],
                3: [(0, -1), [0, 4]],
                4: [(1, -1), [3, 2]]
            }
        }
 
        expected_path = [0, 3, 4]
        result_path = get_bfs_path()
        self.assertEqual(result_path, expected_path, "the BFS path wasn't right")

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
 
        expected_path = [0, 3, 4, 2, 4]
        result_path = get_dfs_path()
        self.assertEqual(result_path, expected_path, "the DFS path wasn't right")

    def test_dfs_path_2(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 4}

        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 3]],
                1: [(1, 0), [0, 2]],
                2: [(2, 0), [1, 4]],
                3: [(0, -1), [0, 4]],
                4: [(1, -1), [3, 2]]
            }
        }
 
        expected_path = [0, 3, 4]
        result_path = get_dfs_path()
        self.assertEqual(result_path, expected_path, "the DFS path wasn't right")

    def test_hamiltonian_cycle(self):
        global_game_data.current_graph_index = 0
        graph_data.graph_data = [[(0,0), [1,2]], [(0,1), [2,0]], [(0,2), [1,0]]]
        expected_cycles_graph_0 = [[1,1]]
        result_cycles_graph_0 = find_hamiltonian_cycles(graph_data.graph_data)
        self.assertEqual(result_cycles_graph_0, expected_cycles_graph_0, "Hamiltonian cycles for graph 0 are incorrect")

    def test_hamiltonian_cycle_2(self):
        global_game_data.current_graph_index = 0
        graph_data.graph_data =[[(0,0), [1]], [(0,1), [0]]]
        expected_cycles_graph_0 = -1
        result_cycles_graph_0 = find_hamiltonian_cycles(graph_data.graph_data)
        self.assertEqual(result_cycles_graph_0, expected_cycles_graph_0, "Hamiltonian cycles for graph 0 are incorrect")

    def test_hamiltonian_cycle_3(self):
        global_game_data.current_graph_index = 0
        graph_data.graph_data = [[(0,0), [1,3]], [(0,1), [0,2]], [(0,2), [1,3]], [(0,3), [2,0]]]
        expected_cycles_graph_0 = [[1,2,1],[2,1,2]]
        result_cycles_graph_0 = find_hamiltonian_cycles(graph_data.graph_data)
        self.assertEqual(result_cycles_graph_0, expected_cycles_graph_0, "Hamiltonian cycles for graph 0 are incorrect")

    def test_hamiltonian_cycle_4(self):
        global_game_data.current_graph_index = 0
        graph_data.graph_data = [[(1,2), [1]], [(3,6), [0,2,3]], [(39,1), [1,3]], [(21, 2), [1,2]], [(2910, 2), [3]]]
        expected_cycles_graph_0 = [[1, 2, 3, 1], [1, 3, 2, 1], [3, 1, 2, 3], [3, 2, 1, 3], [2, 3, 1, 2], [2, 1, 3, 2]]
        result_cycles_graph_0 = find_hamiltonian_cycles(graph_data.graph_data)
        self.assertEqual(result_cycles_graph_0, expected_cycles_graph_0, "Hamiltonian cycles for graph 0 are incorrect")

    def test_sjt_4(self):
        expected = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 4, 2, 3], [4, 1, 2, 3], 
                    [4, 1, 3, 2], [1, 4, 3, 2], [1, 3, 4, 2], [1, 3, 2, 4], 
                    [3, 1, 2, 4], [3, 1, 4, 2], [3, 4, 1, 2], [4, 3, 1, 2], 
                    [4, 3, 2, 1], [3, 4, 2, 1], [3, 2, 4, 1], [3, 2, 1, 4], 
                    [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 3, 1], [4, 2, 3, 1], 
                    [4, 2, 1, 3], [2, 4, 1, 3], [2, 1, 4, 3], [2, 1, 3, 4]]
        result = get_perms_sjt(4)
        self.assertEqual(result, expected, "sjt didnt work")

    def test_sjt_3(self):
        expected = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        result = get_perms_sjt(3)
        self.assertEqual(result, expected, "sjt didnt work")

if __name__ == '__main__':
    unittest.main()
