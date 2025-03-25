import sys

# Tworzenie drzewa BST
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Implementacje komend w BST

class BSTree:
    #Dodawanie elementu do drzewa
    def insert(self, root, key):
        if not root:
            return BSTNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    
#Wypisawywanie drzewa 

    #In-order
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.key, end=" ")
        self.in_order(root.right)
        
    #Pre-order
    def pre_order(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)
        
    #Post-order
    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.key, end=" ")
        
    #Znajdowanie minimalnej i maksymalnej wartości w drzewie
    def find_min(self, root):
        while root.left:
            root = root.left
        return root.key

    def find_max(self, root):
        while root.right:
            root = root.right
        return root.key

# Tworzenie drzewa AVL
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Implementacje komend w AVL
class AVLTree:
    
    #Dodawanie elementow do drzewa i balansowanie drzewa
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

    #Znajdowanie minimalnej i maksymalnej wartości w drzewie
    def find_min(self, root):
        while root.left:
            root = root.left
        return root.key

    def find_max(self, root):
        while root.right:
            root = root.right
        return root.key
    
    #Rotacje lewe i prawe
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
    
    #Wysokość drzewa
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    #Balansowanie drzewa
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
#Wypisywanie drzewa

    #In-order
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.key, end=" ")
        self.in_order(root.right)
        
    #Pre-order
    def pre_order(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)
        
    #Post-order
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
        s = sys.stdin.read()
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
        s = sys.stdin.read()
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

    practice = """
    Help         Show this message
    Print        Print the tree usin In-order, Pre-order, Post-order
    FindMinMax   Find the minimum and maximum values in the tree
    Remove       Remove elements of the tree
    Delete       Delete whole tree
    Export       Export the tree to tickzpicture
    Rebalance    Rebalance the tree
    Exit         Exit the program (same as Ctrl+D)
    """
    print(practice)

    sys.stdin = open("/dev/tty")

    while True:
        print("action> ", end="")
        action = input()
        
        if action == "Help":
            print(practice)

        elif action == "Print":
            print("In-order: ", end="")
            tree.in_order(root)
            print("\nPre-order: ", end="")
            tree.pre_order(root)
            print("\nPost-order: ", end="")
            tree.post_order(root)
            print()
            
        elif action == "FindMinMax":
            print("Min: ", tree.find_min(root), "\nMax: ", tree.find_max(root))
        elif action == "Exit":
            break


if __name__ == "__main__":
    main()
