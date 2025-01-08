# PROGRAM K01-MIF2123-F02

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : graph.py
# Topik     : Makalah Matematika Diskrit 2024 (IF1220-24)
# Tanggal   : Rabu, 8 Januari 2025
# Deskripsi : Subprogram F02 - Graph Type Struct

# KAMUS
# Node , Edge , Graph : class

# ALGORITMA
import heapq , math

class Node:
    def __init__(self , info , x , y) :
        self.info = info
        self.x = x
        self.y = y

    def constructNode(self , info , x , y) :
        self.info = info
        self.x = x
        self.y = y
        return self

class Edge:
    def __init__(self , info , node1 , node2 , weight) :
        self.info = info
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    
    def constructEdge(self , x , ujung1 , ujung2 , weight) :
        self.info = x
        self.node1 = ujung1
        self.node2 = ujung2
        self.weight = weight
        return self

class Graph :
    def __init__(self , list_of_node , list_of_edge , matrix) :
        self.nodes = list_of_node
        self.edges = list_of_edge
        self.graph = matrix

    def constructGraph(self , list_node , list_edge) :
        self.nodes = list_node
        self.edges = list_edge
        matrix = [[0 for _ in range (len(list_node))] for _ in range (len(list_node))]
        for i in range (len(list_edge)) :
            matrix[list_edge[i][1]][list_edge[i][2]] = 1
            matrix[list_edge[i][2]][list_edge[i][1]] = 1
        self.graph = matrix
        return self
    
    def dijkstra(self , start_index , goal_index) :
        num_nodes = len(self.nodes)
        distances = [float('inf')] * num_nodes
        distances[start_index] = 0
        priority_queue = [(0 , start_index)]
        while (priority_queue) :
            current_distance , current_index = heapq.heappop(priority_queue)
            if (current_index == goal_index) :
                return distances[goal_index]
            elif (current_distance > distances[current_index]) :
                continue
            else :
                for i in range (num_nodes) :
                    if (self.graph[current_index][i] != 0) :
                        distance = current_distance + self.graph[current_index][i]
                        if (distance < distances[i]) :
                            distances[i] = distance
                            heapq.heappush(priority_queue , (distance , i))
        return distances[goal_index]
    
    def a_star(self , start_index , goal_index) :
        def euclidean_heuristic(node1 , node2) :
            return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
        
        num_nodes = len(self.nodes)
        distances = [float('inf')] * num_nodes
        distances[start_index] = 0
        priority_queue = [(euclidean_heuristic(self.nodes[start_index] , self.nodes[goal_index]) , start_index)]
        while (priority_queue) :
            _ , current_index = heapq.heappop(priority_queue)
            if (current_index == goal_index) :
                return distances[goal_index]
            for i in range (num_nodes) :
                if (self.graph[current_index][i] != 0) :
                    distance = distances[current_index] + self.graph[current_index][i]
                    if (distance < distances[i]) :
                        distances[i] = distance
                        f_value = distance + euclidean_heuristic(self.nodes[i] , self.nodes[goal_index])
                        heapq.heappush(priority_queue , (f_value , i))
        return distances[goal_index]
    
    def is_tree(self) :
        def dfs(current_index , parent_index) :
            visited[current_index] = True
            for i in range (len(self.nodes)) :
                if (self.graph[current_index][i] != 0) :
                    if (not(visited[i])):
                        if (not(dfs(i , current_index))) :
                            return False
                    elif (i != parent_index) :
                        return False
            return True
        
        visited = [False] * len(self.nodes)
        if (not(dfs(0 , -1))) :
            return False
        else :
            return all(visited)
    
    def prim(self) :
        num_nodes = len(self.nodes)
        in_mst = [False] * num_nodes
        min_edge = [(float('inf') , -1)] * num_nodes
        min_edge[0] = (0 , -1)
        total_weight = 0
        mst_edges = []
        for _ in range (num_nodes) :
            u = -1
            for i in range (num_nodes) :
                if ((not(in_mst[i])) and ((u == -1) or (min_edge[i][0] < min_edge[u][0]))) :
                    u = i
            if ((min_edge[u][1] == -1) and (u != 0)) :
                return None
            else :
                in_mst[u] = True
                total_weight += min_edge[u][0]
                if (min_edge[u][1] != -1) :
                    mst_edges.append((u , min_edge[u][1] , min_edge[u][0]))
                for v in range (num_nodes) :
                    if ((self.graph[u][v] != 0) and (not(in_mst[v])) and (self.graph[u][v] < min_edge[v][0])) :
                        min_edge[v] = (self.graph[u][v] , u)
        return mst_edges , total_weight
    
    def kruskal(self) :
        class UnionFind :
            def __init__(self , size) :
                self.parent = list(range(size))
                self.rank = [0] * size
            
            def find(self , p) :
                if (self.parent[p] != p) :
                    self.parent[p] = self.find(self.parent[p])
                return self.parent[p]
            
            def union(self , p , q) :
                rootP = self.find(p)
                rootQ = self.find(q)
                if (rootP != rootQ) :
                    if (self.rank[rootP] < self.rank[rootQ]) :
                        self.parent[rootP] = rootQ
                    elif (self.rank[rootP] > self.rank[rootQ]) :
                        self.parent[rootQ] = rootP
                    else :
                        self.parent[rootQ] = rootP
                        self.rank[rootP] += 1
                    return True
                return False
        
        edges = []
        for u in range (len(self.nodes)) :
            for v in range (u + 1 , len(self.nodes)) :
                if (self.graph[u][v] != 0) :
                    edges.append((self.graph[u][v] , u , v))
        edges.sort()
        uf = UnionFind(len(self.nodes))
        mst_edges = []
        total_weight = 0
        for (weight , u , v) in (edges) :
            if (uf.union(u , v)) :
                mst_edges.append((u , v , weight))
                total_weight += weight
        if (len(mst_edges) != len(self.nodes) - 1) :
            return None
        else :
            return mst_edges , total_weight