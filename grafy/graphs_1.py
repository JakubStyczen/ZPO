#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adjlist = {}

    for idx, row in enumerate(adjmat, start=1):
        connection_list = []
        for jdx, elem in enumerate(row, start=1):
            if elem > 0:
                for _ in range(elem):
                    connection_list.append(jdx)
        if connection_list:
            adjlist[idx] = connection_list  
    return adjlist

def dfs_recursive_function(G:Dict[int, List[int]], s: int, visited: List[int]):
    if s in visited:
        return []
    visited.append(s)
    if s in G.keys():
        for s_neighbour in G[s]:
            if s_neighbour not in visited:
                dfs_recursive_function(G, s_neighbour, visited)
    return visited

def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    return dfs_recursive_function(G, s, [])

def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack = []
    stack.append(s)
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if v in G.keys():
                neiV = G[v]
                neiV.reverse()
                for v_neighbour in neiV:
                    stack.append(v_neighbour)
    return visited

def dfs_recursive_function_acyclic(G:Dict[int, List[int]], s: int, visited: List[int]):
    if s in visited:
        return True
    visited.append(s)
    if s in G.keys():
        for s_neighbour in G[s]:
            if dfs_recursive_function_acyclic(G, s_neighbour, visited[:]):
                return True
        return False



def is_acyclic(G:Dict[int, List[int]]) -> bool:
    visited = []

    for v in list(G.keys()):
        visited.append(v)
        if v in G.keys():
            for v_neighbour in G[v]:
                if dfs_recursive_function_acyclic(G, v_neighbour,visited[:]):
                    return False
            visited.remove(v)
    return True
    

