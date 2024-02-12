class Node: 
    def __init__(self,key): 
        self._left = None
        self._right = None
        self._data = key 

 
def preOrder(root):
    if root: 
        print(root._data), 
        preOrder(root._left) 
        preOrder(root._right) 

def inOrder(root):
    if root: 
        inOrder(root._left) 
        print(root._data), 
        inOrder(root._right) 

def postOrder(root):
    if root: 
        postOrder(root._left) 
        postOrder(root._right) 
        print(root._data), 


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root._data:
        root._left = insert(root._left, key)
    else:
        root._right = insert(root._right, key)
    return root
 

def recursive_order():
    array = [5, 30, 3, 8, 2, 7, 9, 20, 40, 17, 25, 45, 1, 42, 47]
    root = Node(10)
    print("Recursive order:\n")
    for key in array:
        root = insert(root, key)
    
    print("Preorder:")
    preOrder(root)
    print("\n\nPostorder:")
    postOrder(root)
    print("\n\nInorder:")
    inOrder(root)


def search(root,key): 
      
    if not root: 
        return print(key, "does not exist in the tree")
    if root._data == key:
        return print(key, "does exist in the tree")
  
    if root._data < key: 
        return search(root._right,key) 
    
    return search(root._left,key) 

def recursive_search():
    array = [5, 30, 3, 8, 2, 7, 9, 20, 40, 17, 25, 45, 1, 42, 47]
    root = Node(10)
    print("Recursive search:\n")
    for key in array:
        root = insert(root, key)
    
    search(root, 9)
    search(root, 41)

def recursive_add():
    array = [5, 30, 3, 8, 2, 7, 9, 20, 40, 17, 25, 45, 1, 42, 47]
    root = Node(10)
    insertion = [4, 35, 44]
    print("Recursive addition:\n")
    for key in array:
        root = insert(root, key)
    for key in insertion:
        print(key, "got added succesfully")
        root = insert(root, key)

    print("\nThe new Binary tree: ")
    inOrder(root)

recursive_order()
print("\n~~~~~~~~~~~~~~~~~~~~\n")
recursive_search()
print("\n~~~~~~~~~~~~~~~~~~~~\n")
recursive_add()   
