class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.key)
class BinaryTree:
    def __init__(self):
        self.root=None
    def _insert(self,node,key):
        if node is None:
            return TreeNode(key)
        if key < node.key: 
            node.left= self._insert(node.left,key)
        elif key > node.key :
            node.right=self._insert(node.right,key)
        return node
    def insert(self,key):
        self.root=self._insert(self.root,key)
    def _search(self,node,key):
        if node is None or node.key==key:
            return node
        if key < node.key:
            return self._search(node.left,key)
        return self._search(node.right,key)
    def search(self,key):
        return self._search(self.root,key)
    def _delete(self,node,key):
        if node is None:
            return node
        if key < node.key :
            node.left= self._delete(node.left,key)
        elif key > node.key:
            node.right= self._delete(node.right,key)
bst = BinaryTree()
values = [2,3,1,9,10]
for value in values:
    bst.insert(value)
print(bst.search(10))