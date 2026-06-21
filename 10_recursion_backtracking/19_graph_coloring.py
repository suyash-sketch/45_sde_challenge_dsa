class Solution:
    def is_safe(self, node, color, graph:list , n, col):
        for k in range(n):
            if k != node and graph[k][node] == 1 and color[k] == col:
                return False
        return True
            
    
    def solve(self, node, color, m, N, graph : list):
        if node == N:
            return True

        for i in range(1, m + 1):
            if self.is_safe(node, color, graph, N, i):
                color[node] = i
                if self.solve(node + 1, color, m, N, graph):
                    return True
                color[node] = 0
        return False
       
        
    def graph_coloring(self, graph:list, m, N):
        color = [0] * N

        if self.solve(0, color, m, N, graph):
            return True
        return False


N = 4  # Number of nodes
m = 3  # Maximum number of colors

    # Create a sample graph with edges (0,1), (1,2), (2,3), (3,0), (0,2)
graph = [[False] * 101 for _ in range(101)]
graph[0][1] = graph[1][0] = True
graph[1][2] = graph[2][1] = True
graph[2][3] = graph[3][2] = True
graph[3][0] = graph[0][3] = True
graph[0][2] = graph[2][0] = True

    # Output if the graph can be colored with at most m colors
sol = Solution()

print(sol.graph_coloring(graph, m, N))