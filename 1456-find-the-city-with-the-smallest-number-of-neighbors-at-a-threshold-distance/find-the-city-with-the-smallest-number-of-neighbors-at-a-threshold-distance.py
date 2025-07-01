class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        noofcities = []

        for i in range(n):
            cities = 0
            for j in range(n):
                if dist[i][j] != 0 and dist[i][j] <= distanceThreshold:
                    cities += 1
            noofcities.append(cities)
        
        mn = min(noofcities)
        ans = noofcities[0]

        for i in range(n):
            if noofcities[i] == mn:
                ans = i
        
        return ans
