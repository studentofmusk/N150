class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        else:
            self.data = data

    def print_tree(self) -> None:
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

tree = Node(8)
tree.insert(3)
tree.insert(11)
tree.insert(4)
tree.insert(9)
tree.print_tree()