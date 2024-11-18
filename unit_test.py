import math
import unittest
import graph_data
import global_game_data
from pathing import get_bfs_path, get_dfs_path, get_dijkstra_path, dijkstra, get_a_star_path
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

    def test_dijkstra_path(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 4}
        
        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 2]],
                1: [(10, 10), [0, 7]],
                2: [(2, 0), [3, 0]],
                3: [(3, 0), [4, 2]],
                4: [(4, 0), [3, 5]],
                5: [(5, 0), [6, 4]],
                6: [(6, 0), [5, 7]],
                7: [(7, 0), [6, 1]],
            }
        }
 
        expected_path = [0, 2, 3, 4, 5, 6, 7]
        result_path = get_dijkstra_path()
        self.assertEqual(result_path, expected_path, "the dijsktra path wasn't right")

    def test_dijkstra_path_2(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 4}
        
        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 5]],
                1: [(1, 0), [0, 2]],
                2: [(1, 1), [1, 3]],
                3: [(1, 2), [4, 2]],
                4: [(2, 2), [3, 5,6]],
                5: [(0, 2), [0, 4]],
                6: [(3, 2), [4]],
            }
        }
 
        expected_path = [0, 5, 4, 6]
        result_path = get_dijkstra_path()
        self.assertEqual(result_path, expected_path, "the dijsktra path wasn't right")

    def test_dijkstra(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 4}
        
        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 2]],
                1: [(10, 10), [0, 7]],
                2: [(2, 0), [3, 0]],
                3: [(3, 0), [4, 2]],
                4: [(4, 0), [3, 5]],
                5: [(5, 0), [6, 4]],
                6: [(6, 0), [5, 7]],
                7: [(7, 0), [6, 1]],
            }
        }
        start_node = 0
        target_node = 4
        result_path = dijkstra(graph_data.graph_data[0], start_node, target_node, is_a_star=False)

        expected_path = [0, 2, 3, 4]
        self.assertEqual(result_path, expected_path, "the first half of the djikstra path was wrong")

    def test_dijkstra_2(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 4}
        
        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 2]],
                1: [(10, 10), [0, 7]],
                2: [(2, 0), [3, 0]],
                3: [(3, 0), [4, 2]],
                4: [(4, 0), [3, 5]],
                5: [(5, 0), [6, 4]],
                6: [(6, 0), [5, 7]],
                7: [(7, 0), [6, 1]],
            }
        }
        start_node = 4
        target_node = 7
        result_path = dijkstra(graph_data.graph_data[0], start_node, target_node, is_a_star=False)

        expected_path = [4, 5, 6, 7]
        self.assertEqual(result_path, expected_path, "the second half of the djikstra path was wrong")

    def test_a_star_path(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 4}
        
        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 2]],
                1: [(10, 10), [0, 7]],
                2: [(2, 0), [3, 0]],
                3: [(3, 0), [4, 2]],
                4: [(4, 0), [3, 5]],
                5: [(5, 0), [6, 4]],
                6: [(6, 0), [5, 7]],
                7: [(7, 0), [6, 1]],
            }
        }
 
        expected_path = [0, 2, 3, 4, 5, 6, 7]
        result_path = get_a_star_path()
        self.assertEqual(result_path, expected_path, "the a star path wasn't right")

    def test_a_star_path_2(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 4}
        
        graph_data.graph_data = {
            0: {
                0: [(0, 0), [1, 5]],
                1: [(1, 0), [0, 2]],
                2: [(1, 1), [1, 3]],
                3: [(1, 2), [4, 2]],
                4: [(2, 2), [3, 5,6]],
                5: [(0, 2), [0, 4]],
                6: [(3, 2), [4]],
            }
        }
 
        expected_path = [0, 5, 4, 6]
        result_path = get_a_star_path()
        self.assertEqual(result_path, expected_path, "the a star path wasn't right")

if __name__ == '__main__':
    unittest.main()
