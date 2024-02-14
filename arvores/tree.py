class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percurso em ordem simetrica
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_traversal(node.left)
        print(node)
        if node.right:
            self.simetric_traversal(node.right)

    # Percurso em pós ordem
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end='')

    # Obtendo a altura de uma árvore
    def height(self, node=None):
        if node is None:
            node = self.root
        lheight = 0
        rheight = 0
        if node.left:
            lheight = self.height(node.left)
        if node.right:
            rheight = self.height(node.right)
        if lheight > rheight:
            return lheight + 1
        return rheight + 1

if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = Node(3)
    tree.root.right = Node(15)
    print(tree.root)
