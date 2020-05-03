# Important application of stack:- Stack memory. call Stack is abstract data type that stores info about sub routines/functions/methods of a comp program. call Stack keeps a track of the point to which teach active sub routine should return control when it finishes executing. It stores temp variables created by each function.

#stack follows LIFO method - Last In First Out.

#push():- adds item into the stack
#pop():- removes the last item added in the stack
#peek():- returns the last item in the stack w/o removing it.

#Stack can be implemented using array or link-list.


#Create a class stack(using array)
class Stack:

  def __init__(self):
    self.Stack = [] 
  
  #to check if stack is empty. Return bool value.
  def isEmpty(self): 
    return self.Stack == []

  def push(self, data):
    self.Stack.append(data) #inserting item in the emty array
  
  def pop(self):
    data = self.Stack[-1] #pops the last item
    del self.Stack[-1] #get rid of the ref to last item
    return data
  
  def peek(self):
    return self.Stack[-1] #returns the last item inserted without deleting it. Structure of stack remains the same 

  def sizeStack(self):
    return len(self.Stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(100)

print("Size of stack: ", stack.sizeStack())

print("Items popped: ")
print(stack.pop())
print(stack.pop())

print("Size of Stack: ", stack.sizeStack())

print("Peek item: ", stack.peek())





