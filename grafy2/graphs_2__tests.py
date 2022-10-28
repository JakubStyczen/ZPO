import unittest
import networkx as nx
from graphs_2 import find_min_trail, trail_to_str


class TestFunctions(unittest.TestCase):

    def test_sum_of_edges(self):
        G = nx.MultiDiGraph()
        G.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.4), (2, 3, 0.3), (1, 3, 1.0)])
        trail = find_min_trail(G,1,3)
        total = 0
        for trail_seg in trail:
            total += trail_seg.edge_weight
        
        self.assertEqual(total, nx.dijkstra_path_length(G, 1, 3))

        
if __name__ == '__main__':
    unittest.main()