#Create a Node class
class Node:

  def __init__(self, data): #constructor 
    self.data = data
    self.nextNode = None

# Create a Link list class
class linkList:
  
  def __init__(self):
    self.head = None
    self.size = 0
  
  # O(1)
  def insertStart(self, data): #method
    
    self.size += 1
    newNode = Node(data) #initiate object of Node

    if not self.head:
      self.head = newNode
    else:
      newNode.nextNode = self.head
      self.head = newNode

  # O(1)
  def size1(self):

    print(self.size)

  # O(N)
  def insertEnd(self, data):

    self.size += 1
    newNode = Node(data)
    currentNode = self.head

    while currentNode.nextNode is not None:
      currentNode = currentNode.nextNode
    
    currentNode.nextNode = newNode

  # O(N)
  def remove(self, data):

    if self.head is None:
      return
    
    self.size -= 1
    currentNode = self.head
    previousNode = None

    while currentNode.data != data:

      previousNode = currentNode
      currentNode = currentNode.nextNode
    
    if previousNode is None:
      self.head = currentNode.nextNode
    else:
      previousNode.nextNode = currentNode.nextNode
    
    
  # O(N)
  def traversList(self):

    currentNode = self.head

    while currentNode is not None:
      print(currentNode.data)
      currentNode = currentNode.nextNode
    

l1 = linkList()
l1.insertStart(10)
l1.insertStart(20)
l1.insertStart(30)
l1.insertEnd(40)
l1.size1()

l1.traversList()

l1.remove(30)
l1.remove(40)
l1.remove(10)
l1.remove(20)

print("New list")
l1.traversList()
l1.size1()

#Conclusion: inserting item at the begining of the list is fast for link list.