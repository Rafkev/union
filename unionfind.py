class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Example usage
if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(0, 4)

    print(uf.connected(0, 2))  # False
    print(uf.connected(0, 4))  # True
