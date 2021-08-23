# Binary Tree
# Used for Binary Search operation
# Used For Implementing Sets (de-duplication)
# Used for Sorting = Inorder Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left is not None:
                self.left.add_node(data)
            else:
                self.left = Node(data)

        else:
            if self.right is not None:
                self.right.add_node(data)
            else:
                self.right = Node(data)

    def tree_search(self, val):
        if val == self.data:
            # print(self.data, "found")
            return True

        if val < self.data:
            if self.left is not None:
                # print(self.left.data, "--search left--")
                return self.left.tree_search(val)
            else:
                return False

        if val > self.data:
            if self.right is not None:
                # print(self.right.data, "--search right--")
                return self.right.tree_search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def cal_sum(self):
        sum_tree = 0
        sum_tree += self.data
        if self.left:
            sum_tree += self.left.cal_sum()
        if self.right:
            sum_tree += self.right.cal_sum()

        return sum_tree

    def print_tree(self):
        if self is not None:
            print(self.data)

            if self.left is not None:
                print(f"left --  of {self.data}")
                self.left.print_tree()

            if self.right is not None:
                print(f"right --  of {self.data}")
                self.right.print_tree()


# Inorder traversal
# Left -> Root -> Right
def printInorder(rootNode):
    if rootNode:
        # First recur on left child
        printInorder(rootNode.left)

        # then print the data of node
        print(rootNode.data),

        # now recur on right child
        printInorder(rootNode.right)


# Preorder tree traversal
# Root-> Left-> Right
def printPreorder(rootNode):
    if rootNode:
        # First print the data of node
        print(rootNode.data),

        # Then recur on left child
        printPreorder(rootNode.left)

        # Finally recur on right child
        printPreorder(rootNode.right)


# Post order tree traversal
# Left-> Right --> Root
def printPostorder(rootNode):
    if rootNode:
        # First recur on left child
        printPostorder(rootNode.left)

        # the recur on right child
        printPostorder(rootNode.right)

        # now print the data of node
        print(rootNode.data),


def build_binary_tree():
    lst = [17, 4, 1, 20, 9, 23, 18, 34, 4, 1]
    rootNode = Node(lst[0])
    for i in range(1, len(lst)):
        rootNode.add_node(lst[i])

    rootNode.print_tree()
    return rootNode


root = build_binary_tree()
print("------------ In Order--------------------")
printInorder(root)
print("---------------Pre Order-----------------")
printPreorder(root)
print("---------------Post Order----------------")
printPostorder(root)
print("---------------Search ----------------")
print(root.tree_search(18))
print(root.tree_search(1000))
print("Min. in Tree:", root.find_min())
print("Max. in Tree:", root.find_max())
print("Sum all elements in Tree:", root.cal_sum())
