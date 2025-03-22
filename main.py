import sys


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTree:
    def insert(self, root, key):
        if not root:
            return BSTNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.key, end=" ")
        self.in_order(root.right)

    def pre_order(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.key, end=" ")


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.key, end=" ")
        self.in_order(root.right)

    def pre_order(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.key, end=" ")


def main():
    if "--tree" == sys.argv[1] and "AVL" == sys.argv[2]:
        tree = AVLTree()
        root = None
        inserted = []
        print("Enter values to insert into the AVL tree:")
        s = input()
        value = list(map(int, s.split()))
        print("insert>", " ".join(map(str, value)))
        for v in value:
            root = tree.insert(root, v)
            inserted.append(v)

        print("Tree is completed")
        print()
    elif "--tree" == sys.argv[1] and "BST" == sys.argv[2]:
        tree = BSTree()
        root = None
        inserted = []
        print("Enter values to insert into the BST tree:")
        s = input()
        value = list(map(int, s.split()))
        print("insert>", " ".join(map(str, value)))
        for v in value:
            root = tree.insert(root, v)
            inserted.append(v)

        print("Tree is completed")
        print()
    else:
        print("Wrong arguments. Please use the following format:")
        print("python main.py --tree 'AVL/BST'")

    action = ""
    print("Help         Show this message")
    print("Print        Print the tree usin In-order, Pre-order, Post-order")
    print("Remove       Remove elements of the tree")
    print("Delete       Delete whole tree")
    print("Export       Export the tree to tickzpicture")
    print("Rebalance    Rebalance the tree")
    print("Exit         Exit the program (same as Ctrl+D)")
    print()
    while action != "Exit":
        print("action> ", end="")
        action = input()
        if action == "Help":
            print("Help         Show this message")
            print("Print        Print the tree usin In-order, Pre-order, Post-order")
            print("Remove       Remove elements of the tree")
            print("Delete       Delete whole tree")
            print("Export       Export the tree to tickzpicture")
            print("Rebalance    Rebalance the tree")
            print("Exit         Exit the program (same as Ctrl+D)")
            print()
        elif action == "Print":
            print("In-order: ", end="")
            tree.in_order(root)
            print("\nPre-order: ", end="")
            tree.pre_order(root)
            print("\nPost-order: ", end="")
            tree.post_order(root)
            print()


if __name__ == "__main__":
    main()
