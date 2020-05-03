#Queue - Abstract data type. Uses FIFO : First in -> First out.
#enqueue(): adds items from the back.
#dequeue(): delets items from the front.
#peek(): return the first item w/o removing the item from the queue.

class queue:

  def __init__(self):
    self.queue = []
  
  def isEmpty(self):
    return self.queue == []

  def sizeQueue(self):
    return len(self.queue)
  
  def enqueue(self, data):
    self.queue.append(data)
  
  def dequeue(self):
    data =  self.queue[0]
    del self.queue[0]
    return data

  def peek(self):
  
    return self.queue[0]
  
  def printQueue(self):

    for i in self.queue:
      print(i)
  
q = queue()
q.enqueue(10)
q.enqueue(110)
q.enqueue(102)
q.enqueue(200)

print("Size of queue: ", q.sizeQueue())

q.printQueue()

print('removing top element: ',q.dequeue())
print("Peeking the first item: ", q.peek())

print("Size of queue: ", q.sizeQueue())

q.printQueue()
