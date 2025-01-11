class Node:
    def __init__(self,key):
        self.key=key
        self.left = None
        self.right = None


class binarysearchtree:
    def __init__(self):
        self.root = None

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root,key)
    
    def _insert(self,curr,key):
        if key<curr.key:
            if curr.left is None:
                curr.left = Node(key)
            else:
                self._insert(curr.left,key)
        elif key>curr.key:
            if curr.right is None:
                curr.right=Node(key)
            else:
                self._insert(curr.right,key)

    def search(self,key):
        return self._search(self.root,key)
    
    def _search(self,curr,key):
        if curr is None:
            return False
        if curr.key==key:
            return True
        if key<curr.key:
            return self._search(curr.left,key)
        if key>curr.key:
            return self._search(curr.right,key)
        

if __name__ == "__main__":
    bst = binarysearchtree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("sear for 40",bst.search(40))