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
  
  #calculate height of node.
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
  
  #Right rotation
  def rightRotate(self, node):
    print("Rotating to right of node, ", node.data)

    #store left child of node to temp.
    #store right child of temp to another variable(t).
    #root = temp.
    #right child of root = node
    #left child of node = t 
    tempNode = node.leftchild
    t = tempNode.rightChild

    tempNode.rightChild = node
    node.leftChild = t

    #update height of node and tempNode.
    node.height = max(self.heightCal(node.leftChild), self.heightCal(node.rightChild)) + 1

    tempNode.height = max(self.heightCal(tempNode.leftChild), self.heightCal(tempNode.rightChild)) + 1

    #return tempNode because that will be the new root node.
    return tempNode
  
  #rotation is O(1) time complexity because we just have to update the references of the nodes
  def leftRotation(self, node):
    print("Rotation to left of node, ", node.data)

    tempNode = node.rightChild
    t = tempNode.leftChild

    tempNode.leftChild = node
    node.rightChild = t

    node.height = max(self.heightCal(node.leftChild), self.heightCal(node.rightChild)) + 1
    
    tempNode.height = max(self.height(tempNode.leftChild), self.height(tempNode.rightChild)) + 1

    return tempNode

    
  