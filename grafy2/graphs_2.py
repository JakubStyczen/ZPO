#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, NamedTuple, Set, Dict
from collections import namedtuple
import networkx as nx


VertexID = int

AdjList = Dict[VertexID, List[VertexID]]

Distance = int

EdgeID = int

def neighbors(adjlist: AdjList, start_vertex: VertexID, max_distance: Distance) -> Set[VertexID]:
    Ver_dist = namedtuple('Ver_dist', "idx, dist")
    visited = []
    queue = []
    queue.append(Ver_dist(start_vertex, 0))
    while queue:
        u = queue.pop(0)
        if u.dist > max_distance:
            break
        visited.append(u.idx)
        if u.idx not in adjlist.keys():
            continue
        for v in adjlist[u.idx]:
            if v not in visited:
                queue.append(Ver_dist(v, u.dist + 1))
    return set(visited[1:])
 
# Nazwana krotka reprezentująca segment ścieżki.
class TrailSegmentEntry(NamedTuple):
    start_vertex: VertexID
    end_vertex: VertexID
    edge_id: EdgeID
    edge_weight: float
 
 
Trail = List[TrailSegmentEntry]
 
 
def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.
 
    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """
    if filepath:
        G = nx.MultiDiGraph()
        
        list_of_nodes = []
        
        with open(filepath, 'r') as file:
            for line in file.readlines():
                if line.strip():
                    va, vb, w = line.strip().split(' ')
                    list_of_nodes.append((int(va),int(vb),float(w)))
                    
        G.add_weighted_edges_from(list_of_nodes)
        return G
 
 
def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.
 
    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """
    trail_list = []
    shortest_path = nx.dijkstra_path(g,v_start, v_end)
    for i in range(len(shortest_path) - 1):
        start_vertex, end_vertex = shortest_path[i], shortest_path[i+1]
        min_edge_idx, min_weight = 0, 1
        
        for edge_idx, weight_dct in g[start_vertex][end_vertex].items():
            if weight_dct['weight'] < min_weight:
                min_weight = weight_dct['weight']
                min_edge_idx = edge_idx
        trail_list.append(TrailSegmentEntry(start_vertex, end_vertex, min_edge_idx, min_weight))
    
    return trail_list

 
def trail_to_str(trail: Trail) -> str:
    """Wyznacz reprezentację tekstową ścieżki.
 
    :param trail: ścieżka
    :return: reprezentacja tekstowa ścieżki
    """
    total = 0
    str_rep = ""
    for trail_seg in trail[:-1]:
        str_rep += f'{trail_seg.start_vertex} -[{trail_seg.edge_id}: {trail_seg.edge_weight}]-> '
        total += trail_seg.edge_weight
    last = trail[-1]
    total += last.edge_weight
    str_rep += f'{last.start_vertex} -[{last.edge_id}: {last.edge_weight}]-> {last.end_vertex}  (total = {total})'
    
    return str_rep