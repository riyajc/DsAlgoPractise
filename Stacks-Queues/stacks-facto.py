#recursive calls are pushed onto the stack untill we bump into the base case.
#stack memory is limited. if there are too many recursive calls pushed onto the stack, and if the stack memory is full, stack overflow happens. Hence, for eg:- factorial(1000) might lead to stack overflow.
#Base case is needed to be defined. Otherwise, the recursive call is executed untill stackoverflow.

#recursive method calls are useful during : DFS, traversing link-list, factorial. The OS transform recursive implementation using stacks.

def factorial(num):

  if num == 0: #base case
    return 1
  
  return num * factorial(num-1)

print(factorial(4)) #recursive method calls