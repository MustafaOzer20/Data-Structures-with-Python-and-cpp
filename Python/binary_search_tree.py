class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key

class BinarySearchTree:
    __counter = 0
    minVal = None
    maxVal = None
    __preorderList = []
    __postorderList = []
    __inorderList = []
    def __init__(self, *args):
        self.root = None
        for arg in args:
            self.add(arg)
    
    def add(self, key):
        node = Node(key)
        if self.root == None:
            self.root = node
            self.minVal = key
            self.maxVal = key
        else:
            temp = self.root
            while temp != None:
                attr = temp
                if key == temp.key:
                    raise Exception("This value exists in the tree.")
                elif key < temp.key:
                    temp = temp.left
                else:
                    temp = temp.right
            if key < attr.key:
                attr.left = node
            else:
                attr.right = node
            
            if key > self.maxVal:
                self.maxVal = key
            if key < self.minVal:
                self.minVal = key

        self.__counter += 1


    def search(self, key):
        if self.root == None:
            return False
        else:
            temp = self.root
            attr = temp
            while temp != None:
                if key == temp.key:
                    return (True, temp, attr)
                elif key < temp.key:
                    attr = temp
                    temp = temp.left
                else:
                    attr = temp
                    temp = temp.right
            return False


    
    def deletion(self, key):
        if not self.search(key):
            return f"{key} is not found in tree."
        else:
            _, temp, attr = self.search(key)
            if temp.left == None and temp.right == None:
                if attr.key > temp.key:
                    attr.left = None
                else:
                    attr.right = None

            elif temp.right: # successor
                successor = self.__successor(temp)
                data = successor.key
                self.deletion(data)
                temp.key = data

            elif temp.left: # predecessor
                predecessor = self.__predecessor(temp)
                data = predecessor.key
                self.deletion(data)
                temp.key = data

    def __successor(self, node):
        temp = node
        temp = temp.right
        while temp.left != None:
            temp = temp.left
        return temp   

    def __predecessor(self, node):
        temp = node
        temp = temp.left
        while temp.right != None:
            temp = temp.right
        return temp 


    def preorder(self):
        self.__preorderList.clear()
        self.__preorder(self.root)
        return self.__preorderList

    def postorder(self):
        self.__postorderList.clear()
        self.__postorder(self.root)
        return self.__postorderList

    def inorder(self):
        self.__inorderList.clear()
        self.__inorder(self.root)
        return self.__inorderList 

    def __preorder(self, root):
        temp = root
        if temp != None:
            self.__preorderList.append(temp.key)
            self.__preorder(temp.left)
            self.__preorder(temp.right)

    def __inorder(self,root):
        temp = root
        if temp != None:
            self.__inorder(temp.left)
            self.__inorderList.append(temp.key)
            self.__inorder(temp.right)

    def __postorder(self,root): 
        temp = root
        if temp != None:  
            self.__postorder(temp.left)
            self.__postorder(temp.right)
            self.__postorderList.append(temp.key)

    def __len__(self):
        return self.__counter
