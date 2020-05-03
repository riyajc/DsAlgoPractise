#BST: every single node has two childern. Left child < root. Right child > root.

#Create  class Node:- represents the nodes in the tree. 
class Node:

  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None
  #print(self.data)

#Define BST class to execute operations on BST
class BST:

  def __init__(self):
    self.root = None
  
  def insert(self, data):
    if not self.root:
      self.root = Node(data)
      print(self.root.data)
    else:
      self.insertNode(data, self.root)

  #O(log N):- Although we have recursive func, the condition "if data < node.data" reduces the search to only half of the BST. If true, search algo only executes for left half from root of BST. Otherwise, right half from root of BST. 

  #THIS IS APPLICABLE ONLY FOR BALANCED BST.OTHERWISE, TIME COMPLEXITY WILL BE O(N). 

  def insertNode(self, data, node):

    if data < node.data:
      if node.leftChild:
        self.insertNode(data, node.leftChild) #recursive.
      else:
        node.leftChild = Node(data)
        print(node.leftChild.data)
    else:
      if node.rightChild:
        self.insertNode(data, node.rightChild)
      else:
        node.rightChild = Node(data)
        print(node.rightChild.data)
  
  #if self.root = None, returns nothing.
  def getMinValue(self):
    
    if self.root:
      return self.getMin(self.root)
    
  def getMin(self, node):
    
    if not node.leftChild:
      print("Minimum value")
      return node.data
    else:
      return self.getMin(node.leftChild)
  
  def getMaxValue(self):
    if self.root:
      return self.maxValue(self.root)
  
  def maxValue(self, node):
    if node.rightChild:
      return self.maxValue(node.rightChild)
    
    print("Maximum value")
    return node.data
  
  
  def traversal(self):
    if self.root:
      print("In order traversal: ")
      self.traverseInOrder(self.root)
      print("Pre order traversal: ")
      self.traversePreOrder(self.root)
      print("Post order traversal:")
      self.traversePostOrder(self.root)
  
  #O(N): In order traversal= lc + root + rc
  def traverseInOrder(self, node):
    if node.leftChild:
      self.traverseInOrder(node.leftChild)
    
    print(node.data)

    if node.rightChild:
      self.traverseInOrder(node.rightChild)
  
  #O(N): Pre order traversal= root + lc + rc
  def traversePreOrder(self, node):
    print(node.data)

    if node.leftChild:
      self.traversePreOrder(node.leftChild)
    
    if node.rightChild:
      self.traversePreOrder(node.rightChild)
  
  #O(N): Post order traversal= lc+ rc+ root
  def traversePostOrder(self,node):
    if node.leftChild:
      self.traversePostOrder(node.leftChild)
    
    if node.rightChild:
      self.traversePostOrder(node.rightChild)
    
    print(node.data)
     
b = BST()
b.insert(12)
b.insert(4)
b.insert(1)
b.insert(5)
b.insert(15) 
b.insert(3)
print(b.getMinValue())
print(b.getMaxValue())
b.traversal()