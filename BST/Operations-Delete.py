
class Node:

  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

class BST:

  def __init__(self):
    self.root = None
  
  def insert(self, data):
    if not self.root:
      self.root = Node(data)
      print(self.root.data)
    else:
      self.insertNode(data, self.root)
      
    
  def insertNode(self, data, node):
    if data < node.data:
      if not node.leftChild:
        node.leftChild = Node(data)
        print(node.leftChild.data)
      else:
        self.insertNode(data, node.leftChild)

    else:
      if not node.rightChild:
        node.rightChild = Node(data)
        print(node.rightChild.data)
      else:
        self.insertNode(data, node.rightChild)
      
  
  def remove(self, data):
    if self.root:
      self.removeVal(data, self.root)
  
  def removeVal(self, data, node):
    if data < node.data:
      node.leftChild = self.removeVal(data, node.leftChild)
    elif data > node.data:
      node.rightChild = self.removeVal(data, node.rightChild)
    else:
      if not node.leftChild and node.rightChild:
        print("Removing leaf node")
        del node
        return None
      
      if not node.leftChild:
        print("Removing node with right child")
        tempNode = node.rightChild
        del node
        return tempNode
      elif not node.rightChild:
        print("Removing node with left child")
        tempNode = node.leftChild
        del node
        return tempNode
      
      #if the node to remove has two children. Method 1: Get the highest value in the left sub-tree. Node-data = highest value in left subtree. Traverse to the right in left-subtree uptill the temp node. The temp node is either going to be a left node or node with left child or right child. Use the removeVal method.
      print("Removing node with two children")
      tempNode = self.getPredecessor(node.leftChild)
      node.data = tempNode.data
      node.leftChild = self.removeVal(tempNode.data, node.leftChild)

  def getPredecessor(self, node):
    if node.rightChild:
      self.getPredecessor(node.rightChild)
        
    return node
  
  def traverse(self):
    if self.root:
      self.traverseInOrder(self.root)
    else: return None

  def traverseInOrder(self, node):
    if node.leftChild:
      self.traverseInOrder(node.leftChild)
    
    print(node.data)

    if node.rightChild:
      self.traverseInOrder(node.rightChild)
      

      
   
      
      


b = BST()
b.insert(12)
b.insert(4)
b.insert(15)
b.insert(1)
b.insert(3)
b.traverse()
b.remove(12)
b.traverse()