import math
import unittest
import pathing
import permutation


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

    def test_bfs_path_fail(self):
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
        bfs_path = pathing.bfs(graph, 0, 7)   
        assert path == bfs_path, "Failed to not find path using BFS" 

    def test_sjt(self):
        graph = [
        [(0,0), [1,2]],
        [(0,200), [0,3]],
        [(200,200), [0,3]],
        [(200,0), [1,2]]]
        all_perms = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 3, 1, 2], [3, 0, 1, 2], [3, 0, 2, 1], [0, 3, 2, 1], [0, 2, 3, 1], [0, 2, 1, 3], [2, 0, 1, 3], [2, 0, 3, 1], [2, 3, 0, 1], [3, 2, 0, 1], [3, 2, 1, 0], [2, 3, 1, 0], [2, 1, 3, 0], [2, 1, 0, 3], [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 2, 0], [3, 1, 2, 0], [3, 1, 0, 2], [1, 3, 0, 2], [1, 0, 3, 2], [1, 0, 2, 3]]
        sjt_perms = permutation.sjt_permutations(graph)
        assert all_perms == sjt_perms, "Failed to produce all permutations"
    
    def test_sjt_empty_graph(self):
        graph = []
        all_perms = []
        sjt_perms = permutation.sjt_permutations(graph)
        assert all_perms == sjt_perms, "Failed to produce [] with empty graph"

    def test_hamilitonian(self):
        graph = [
        [(0,0), [1,2]],
        [(0,200), [0,3]],
        [(200,200), [0,3]],
        [(200,0), [1,2]]]
        cycles = [[0, 1, 3, 2, 0], [0, 2, 3, 1, 0], [2, 0, 1, 3, 2], [3, 2, 0, 1, 3], [2, 3, 1, 0, 2], [1, 3, 2, 0, 1], [3, 1, 0, 2, 3], [1, 0, 2, 3, 1]]
        sjt_perms = permutation.sjt_permutations(graph)
        perms = permutation.find_hamilition_cycles(graph, sjt_perms)
        assert cycles == perms, "Failed to produce all permutations"

    def test_optimal_cycle(self):
        graph = [
        [(0,0), [1,2]],
        [(0,200), [0,3]],
        [(200,200), [0,3]],
        [(200,0), [1,2]]]
        best_cycles = [[0, 1, 3, 2, 0], [0, 2, 3, 1, 0], [2, 0, 1, 3, 2], [3, 2, 0, 1, 3], [2, 3, 1, 0, 2], [1, 3, 2, 0, 1], [3, 1, 0, 2, 3], [1, 0, 2, 3, 1]]
        sjt_perms = permutation.sjt_permutations(graph)
        perms = permutation.find_hamilition_cycles(graph, sjt_perms)
        best_perms = permutation.find_optimal_ham_cycles(perms, graph)
        assert best_cycles == best_perms, "Failed to produce all permutations"

    def test_dijkstra(self):
        graph = [[(0, 0), [1, 2, 3]],
        [(50, -100), [0, 3, 4]],
        [(100, 0), [0, 4, 5]], 
        [(100, -200), [0, 1, 5]],
        [(200, 0), [1, 2, 5, 6]],  
        [(150, -300), [2, 3, 4, 6]], 
        [(300, 100), [4, 5, 7]],    
        [(350, 50), [6]]]
        path = [0,2,4,6,7]
        dijkstra_path = pathing.dijkstra_path(graph, 0, 7)
        assert path == dijkstra_path, "Failed to navigate path using Dijkstra's Path"

    def test_dijkstra_fail(self):
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
        dijkstra_path= pathing.dijkstra_path(graph, 0, 7)   
        assert path == dijkstra_path, "Failed to not find path using Dijkstra" 


    def test_euclidean_distance(self):
        coord1 = (10,0)
        coord2 = (20,0)
        eclid = pathing.euclidean_distance(coord1, coord2)
        assert eclid == 10, "Failed to calculate the correct euclidean distance"



if __name__ == '__main__':
    unittest.main()
