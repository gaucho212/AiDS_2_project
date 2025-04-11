import sys
import time

sys.setrecursionlimit(10**6)  # Ustawienie limitu rekurencji na 1 milion

class Tree:
    # In-order
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.key, end=" ")
        self.in_order(root.right)

    # Pre-order
    def pre_order(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    # Post-order
    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.key, end=" ")
    
    # Usuwanie całego drzewa
    def remove_tree(self, root):
        if not root:
            return
        self.remove_tree(root.left)
        self.remove_tree(root.right)
        del root

    # Znajdowanie minimalnej i maksymalnej wartości w drzewie
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def find_max(self, root):
        while root.right:
            root = root.right
        return root
    
    # Rysowanie drzewa
    def export(self, root, level=0, type="ROOT"):
        indent = "    " * level
        if not root.left and not root.right:
            return f"{indent}{type} LEAF {root.key}"

        l_str = (
            self.export(root.left, level + 1, "LEFT")
            if root.left
            else f"{indent}    child [missing]"
        )
        r_str = (
            self.export(root.right, level + 1, "RIGHT")
            if root.right
            else f"{indent}    child [missing]"
        )

        return f"{indent}{type} {root.key}\n{l_str} \n{r_str}"

# Tworzenie drzewa BST
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Implementacje komend w BST
class BSTree(Tree):
    pass

    # Dodawanie elementu do drzewa
    def insert(self, root, key):
        if not root:
            return BSTNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    # Usuwanie elementów
    def remove(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.remove(root.left, key)

        elif key > root.key:
            root.right = self.remove(root.right, key)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.remove(root.right, temp.key)

        return root

    
    # Przekształca drzewo w kregosłup
    def create_temp(self, root):
        temp_root = BSTNode(0)
        temp_root.right = root
        current = temp_root

        while current.right:
            if current.right.left:
                node = current.right
                current.right = node.left
                node.left = current.right.right
                current.right.right = node
            else:
                current = current.right

        return temp_root.right
    
    # Wykonuje rotacje w lewo
    def change(self, root, count):
        dummy = BSTNode(0)
        dummy.right = root
        current = dummy

        for _ in range(count):
            if current.right and current.right.right:
                node = current.right
                current.right = node.right
                node.right = current.right.left
                current.right.left = node
            current = current.right

        return dummy.right
    
    # Rownoważenie drzewa przy pomocy DSW
    def rebalance(self, root):
        if not root:
            return None

        root = self.create_temp(root)
        
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        n = count_nodes(root)
        m = 2 ** (n.bit_length() - 1) - 1
        root = self.change(root, n - m)

        while m > 1:
            m //= 2
            root = self.change(root, m)

        return root

# Tworzenie drzewa AVL
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# Implementacje komend w AVL
class AVLTree(Tree):
    pass
    # Dodawanie elementow do drzewa i balansowanie drzewa
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

    # Rotacje lewe i prawe
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

    # Wysokość drzewa
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    # Balansowanie drzewa
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # Usuwanie elementu z drzewa i balansowanie drzewa
    def remove(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.remove(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

def main():
    def log_action(tree_type, action_type, execution_time):
        with open("tree_actions.log", "a") as log_file:
            log_file.write(f"{tree_type} {action_type} {execution_time:.6f} seconds\n")

    if "--tree" == sys.argv[1] and "AVL" == sys.argv[2]:
        tree = AVLTree()
        root = None
        inserted = []
        tree_type = "AVL"

        if len(sys.argv)>3 and sys.argv[3] == "test":
            value = [x for x in range(1, 10000)]

        else:
            print("Enter values to insert into the AVL tree:")
            s = sys.stdin.read()
            value = list(map(int, s.split()))
            print("insert>", " ".join(map(str, value)))
        start_time = time.time()
        for v in value:
            root = tree.insert(root, v)
            inserted.append(v)
        execution_time = time.time() - start_time
        log_action(tree_type, "Insert", execution_time)

        print("Tree is completed\n")

    elif "--tree" == sys.argv[1] and "BST" == sys.argv[2]:
        tree = BSTree()
        root = None
        inserted = []
        tree_type = "BST"

        if len(sys.argv)>3 and sys.argv[3] == "test":
            value = [x for x in range(1, 10000)]

        else:
            print("Enter values to insert into the BST tree:")
            s = sys.stdin.read()
            value = list(map(int, s.split()))
            print("insert>", " ".join(map(str, value)))
        start_time = time.time()
        for v in value:
            root = tree.insert(root, v)
            inserted.append(v)
        execution_time = time.time() - start_time
        log_action(tree_type, "Insert", execution_time)

        print("Tree is completed\n")

    else:
        message = """
        Wrong arguments. Please use the following format:
        python main.py --tree 'AVL/BST'
        """
        print(message)

    practice = """
    Help         Show this message
    Print        Print the tree usin In-order, Pre-order, Post-order
    FindMinMax   Find the minimum and maximum values in the tree
    Draw         Draw the tree
    Remove       Remove elements of the tree
    Delete All   Delete whole tree
    Rebalance    Rebalance the tree
    Exit         Exit the program (same as Ctrl+D)
    """
    print(practice)

    sys.stdin = open("/dev/tty")

    while True:
        print("action> ", end="")
        action = input()

        if action == "Help" or action == "help":
            print(practice)

        elif action == "Print" or action == "print":
            start_time = time.time()
            print("In-order: ", end="")
            tree.in_order(root)
            execution_time = time.time() - start_time
            print("\nPre-order: ", end="")
            tree.pre_order(root)
            print("\nPost-order: ", end="")
            tree.post_order(root)
            print()

            log_action(tree_type, "Print(In_order)", execution_time)

        elif action == "FindMinMax" or action == "findminmax":
            start_time = time.time()
            if not root:
                print("Tree is empty.")
            else:
                print(
                    "Min: ", tree.find_min(root).key, "\nMax: ", tree.find_max(root).key
                )
            execution_time = time.time() - start_time
            log_action(tree_type, "FindMinMax", execution_time)

        elif action == "Remove" or action == "remove":
            print("to remove> ", end="")
            values = list(map(int, input().split()))
            removed = []
            not_found = []

            # Funkcja pomocnicza do sprawdzania czy element istnieje w drzewie
            def find_key(root, key):
                if not root:
                    return False
                if root.key == key:
                    return True
                if key < root.key:
                    return find_key(root.left, key)
                return find_key(root.right, key)

            start_time = time.time()
            for value in values:
                if find_key(root, value):
                    root = tree.remove(root, value)
                    removed.append(value)
                else:
                    not_found.append(value)
            execution_time = time.time() - start_time

            if removed:
                print(f"Removed {removed} from the tree.")
            if not_found:
                print(f"Values {not_found} not found in the tree.")
            if not removed and not not_found:
                print("No values provided to remove.")
            log_action(tree_type, "Remove", execution_time)

        elif action == "Draw" or action == "draw":
            start_time = time.time()
            print(f"\\{tree.export(root)}")
            execution_time = time.time() - start_time
            log_action(tree_type, "Draw", execution_time)

        elif action == "Delete All" or action == "delete all":
            start_time = time.time()
            tree.remove_tree(root)
            root = None
            execution_time = time.time() - start_time
            print("Tree has been deleted.\n")
            log_action(tree_type, "Delete All", execution_time)

        elif action == "Rebalance" or action == "rebalance":
            if tree_type == "AVL":
                print("Tree is already balanced.")
                continue
            start_time = time.time()
            root = tree.rebalance(root)
            execution_time = time.time() - start_time
            print(f"Pre-Order: ", end="")
            tree.pre_order(root)
            print()
            log_action(tree_type, "Rebalance", execution_time)

        elif action == "Exit" or action == "exit":
            break

        else:
            print("Invalid Instruction\n")


if __name__ == "__main__":
    main()
