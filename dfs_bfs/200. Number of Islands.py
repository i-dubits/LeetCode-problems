#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

from IPython.core.debugger import set_trace
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph_with_explicit_edges(graph_dict):
    # Create a new graph from the dictionary
    G = nx.Graph(graph_dict)

    # Define positions for all nodes
    pos = nx.spring_layout(G)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')
    
    # Draw edges with enhanced styling
    nx.draw_networkx_edges(G, pos, width=9.5, edge_color='black', style='dashed')
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
    plt.axis('off')  # Turn off the axis
    plt.show()

class Solution:
    def numIslands(self, grid):
        self.grid = grid

        vert_dict = self.grid_to_graph(self.grid)
        self.marked = {k:0 for k in vert_dict.keys()}
        self.cc_count = 0

        for k in vert_dict.keys():
            if self.marked[k] == 0:
                self.cc_count += 1
                self.dfs(vert_dict, k)  

        return self.cc_count      


    def grid_to_graph(self, grid):
    
        m = len(grid) # number of rows
        n = len(grid[0]) # number of columns
        
        vert_dict = defaultdict(list)
        #set_trace()
        for i in range(m):      # i - row number
            for j in range(n):  # j - column number
                if grid[i][j] == '1':
                    
                    vert_dict[i*n+j]
                    if j - 1 >= 0 and grid[i][j-1] == '1':
                        vert_dict[i*n+j].append(i*n+j-1)
                        
                    if j + 1 < n and grid[i][j+1] == '1':
                        vert_dict[i*n+j].append(i*n+j+1)
                    
                    if i + 1 < m and grid[i+1][j] == '1':
                        vert_dict[i*n+j].append( (i+1)*n + j )
                    
                    if i - 1 >= 0 and grid[i-1][j] == '1':
                        vert_dict[i*n+j].append( (i-1)*n + j)
                        
        return vert_dict

    def dfs(self, graph, vert):
        #set_trace()
        for v in graph[vert]:
            if self.marked[v] == 0:
                self.marked[v] = 1
                self.dfs(graph, v)
               
grid = [["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
                    
















