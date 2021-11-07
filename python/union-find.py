class Union_Find:
    def __init__(self, arr) -> None:
        self.parent = {}
        self.rank = {}
        self.arr = arr
        for item in arr:
            self.parent[item] = item
            self.rank[item] = 0

    def find(self, item) -> set:
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item1, item2) -> None:
        item1_root = self.find(item1)
        item2_root = self.find(item2)
        if item1_root == item2_root:
            return
        if self.rank[item1_root] > self.rank[item2_root]:
            self.parent[item2_root] = item1_root
        elif self.rank[item1_root] < self.rank[item2_root]:
            self.parent[item1_root] = item2_root
        else:
            self.parent[item1_root] = item2_root
            self.rank[item2_root] = self.rank[item2_root] + 1

    def print(self) -> None:
        print([self.find(i) for i in self.parent])
