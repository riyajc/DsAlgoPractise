#Create a node.
#Node class in AVL will have data, left-child, right-child and height(height of a node is the length of longest path from it to the leaf node.) parameters.
#Height can be calculated using recursion                 h = max(rightChild.height(), leftChild.height())+1.
#Height of a node in AVL should be as small as possible.   |rightChild.height()-leftChild.height()| <= 1

#Node class.
class Node:

  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None
    self.height = 0

#AVL class.
class AVL:

  def __init__(self):
    self.root = None
  
  def insert(self, data):
    self.root = self.insertNode(data, self.root)
  
  def insertNode(self, data, node):
    if not node:
      return Node(data)
    
    if data < node.data:
      node.leftChild = self.insertNode(data, node.leftChild)
    else:
      node.rightChild = self.insertNode(data, node.rightChild)
    
    #update the height of parent node.
    node.height = max(self.heightCal(node.leftChild), self.heightCal(node.rightChild)) +1  
    #print("Height of node " + str(node.data) + " is " + str(node.height))

    return self.settleVoilation(data, node)

  
  # Maintaining the balance of tree.
  def settleVoilation(self, data, node):
    balance = self.balanceCal(node)

    #case 1: if balance > 1 , Right Rotation:- Because, doubly left heavy situation.
    if balance > 1 and data < node.leftChild.data:
      print("Left subtree of the node is heavy")
      return self.rightRotate(node)

    #case 2: if balance < -1, Left Rotation:- Doubly right heavy situation
    if balance < -1 and data > node.rightChild.data:
      print("Right subtree of node is heavy")
      return self.leftRotation(node)

    #case 3: Left-Right heavy subtree:- Left rotation - Right rotation 
    if balance > 1 and data > node.leftChild:
      node.leftChild = self.leftRotation(node.leftChild)
      return self.rightRotation(node)
      
    #case 4: Right-left heavy subtree:- Right rotation - Left Rotation.
    if balance < -1 and data < node.rightChild:
      node.rightChild = self.righRotation(node.rightChild)
      return self.leftRotation(node)
    
    return node


  def heightCal(self, node):

    if not node:
      return -1
    
    return node.height
  
  #if it returns val > 1 => left heavy tree => right rotation
  #if it returns val < -1 => right heavy tree => left rotation.
  #calculate balance of node.

  def balanceCal(self, node):
    if not node:
      return 0

    return self.heightCal(node.leftChild) - self.heightCal(node.rightChild)
  
  #Right Rotation
  #store left child of node to temp.
  #store right child of temp to another variable(t).
  #right child of temp = node
  #left child of node = t 
  #update height of node and tempNode.
  #return tempNode because that will be the new root node.

  def rightRotate(self, node):
    print("Rotating to right of node, ", node.data)

    tempNode = node.leftChild
    t = tempNode.rightChild

    tempNode.rightChild = node
    node.leftChild = t
    
    node.height = max(self.heightCal(node.leftChild), self.heightCal(node.rightChild)) + 1
    tempNode.height = max(self.heightCal(tempNode.leftChild), self.heightCal(tempNode.rightChild)) + 1

    return tempNode
  
  #rotation is O(1) time complexity because we just have to update the references of the nodes

  #left rotation
  #store right child of node in temp.
  #store left child of temp to t.
  #left child of temp = node.
  #right child of node = t

  def leftRotation(self, node):
    print("Rotation to left of node, ", node.data)

    tempNode = node.rightChild
    t = tempNode.leftChild

    tempNode.leftChild = node
    node.rightChild = t

    node.height = max(self.heightCal(node.leftChild), self.heightCal(node.rightChild)) + 1
    
    tempNode.height = max(self.height(tempNode.leftChild), self.height(tempNode.rightChild)) + 1

    return tempNode
  

  #AVL tree traversal
  def traverse(self):
    if self.root:
      self.traverseTree(self.root)
  
  def traverseTree(self, node):
    if node.leftChild:
      self.traverseTree(node.leftChild)
    
    print("%s" % node.data)

    if node.rightChild:
      self.traverseTree(node.rightChild)
    
    


#Test AVL Algo
avl = AVL()
avl.insert(5)
avl.insert(4)
avl.insert(2)

avl.traverse()
  