import math
import unittest
import pathing


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
    
    def test_check_path(self):
        graph = [(0, 0), [1]], [(50, -200), [0, 2]], [(50, -300), [1, 3]], [(200, -500), [2]]
        path = [1, 2, 3]  
        assert pathing.check_path(graph, path)

    def test_dfs_path(self):
        graph = [[(0, 0), [1, 2, 3]],
        [(50, -100), [0, 3, 4]],
        [(100, 0), [0, 4, 5]], 
        [(100, -200), [0, 1, 5]],
        [(200, 0), [1, 2, 5, 6]],  
        [(150, -300), [2, 3, 4, 6]], 
        [(300, 100), [4, 5, 7]],    
        [(350, 50), [6]]]
        path = [0,3,5,6,7]
        dfs_path = pathing.dfs(graph, 0, 7)
        assert path == dfs_path, "Failed to navigate path using DFS"

    def test_bfs_path(self):
        graph = [[(0, 0), [1, 2, 3]],
        [(50, -100), [0, 3, 4]],
        [(100, 0), [0, 4, 5]], 
        [(100, -200), [0, 1, 5]],
        [(200, 0), [1, 2, 5, 6]],  
        [(150, -300), [2, 3, 4, 6]], 
        [(300, 100), [4, 5, 7]],    
        [(350, 50), [6]]]
        path = [0,1,4,6,7]
        bfs_path = pathing.bfs(graph, 0, 7)
        assert path == bfs_path, "Failed to navigate path using BFS"

    def test_dfs_path_fail(self):
        #disconnected nodes
        graph = [
        [(0, 0), [1, 2]],
        [(1, 0), [0]],
        [(0, 1), [0]],
        [(10, 10), [4]], 
        [(11, 10), [3]], 
        [(20, 20), []], 
        [(30, 30), [7]], 
        [(31, 30), [6]]]
        path = None
        dfs_path = pathing.dfs(graph, 0, 7)   
        assert path == dfs_path, "Failed to not find path using DFS" 

    def test_dfs_path_fail(self):
        #disconnected nodes
        graph = [
        [(0, 0), [1, 2]],
        [(1, 0), [0]],
        [(0, 1), [0]],
        [(10, 10), [4]], 
        [(11, 10), [3]], 
        [(20, 20), []], 
        [(30, 30), [7]], 
        [(31, 30), [6]]]
        path = None
        dfs_path = pathing.bfs(graph, 0, 7)   
        assert path == dfs_path, "Failed to not find path using BFS" 

if __name__ == '__main__':
    unittest.main()
