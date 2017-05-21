# DONE

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

class Node:

  # Constructor to create a new node
  def __init__(self, cost, children=None, parent=None):
    self.cost = cost
    self.children = children if children else []
    self.parent = parent
  def set_parent(self, parent):
      self.parent = parent

# O(n) time
#   where n is the number of nodes
# O(max_depth) space (on the call stack)
def getCheapestCost_recursive_dfs(rootNode):
  if not rootNode.children:
    return rootNode.cost
  
  min_sales_path_soFar = 2**31-1
  
  for child in rootNode.children:
    curr_min_sales_path = rootNode.cost + getCheapestCost_recursive_dfs(child)
    min_sales_path_soFar = min(min_sales_path_soFar, curr_min_sales_path)
  return min_sales_path_soFar


# no longer need currMin to be global
# currMin = 2**31-1
# def caller(rootNode):
#     global currMin
#     currMin = 2**31-1
#     return getCheapestCost(rootNode)

# mutates the original tree
#
# O(n) time
#   where n is the number of nodes
# O(n) space in the absolute worst case
def getCheapestCost_iterative_dfs(rootNode):
  
  # global currMin
  
  currMin = 2**31-1
  
  stack = []
  stack.append(rootNode)
  
  while stack:
    curr_node = stack.pop()
    
    # atlernative 1
    # curr_node.cost += curr_node.parent.cost if curr_node.parent else 0
    
    if not curr_node.children:
      currMin = min(currMin, curr_node.cost)
    else:
      # alternative 2
      for child in curr_node.children:
          child.cost += curr_node.cost
      
      stack.extend(curr_node.children)
  
  return currMin


'''
     0
5    3    6
4   2 0  1 5
    1 10
    1
'''

n10 = Node(10,[])
n111 = Node(1,[])
n11 = Node(1, [n111])
n55 = Node(5, [])
n1 = Node(1,[])
n00 = Node(0, [n10])
n2 = Node(2, [n11])
n4 = Node(4,[])
n6 = Node(6, [n1, n55])
n3 = Node(3, [n2, n00])
n5 = Node(5, [n4])
n0 = Node(0, [n5, n3, n6])

n10.set_parent(n00)
n111.set_parent(n11)
n11.set_parent(n2)
n55.set_parent(n6)
n1.set_parent(n6)
n00.set_parent(n3)
n2.set_parent(n3)
n4.set_parent(n5)
n6.set_parent(n0)
n3.set_parent(n0)
n5.set_parent(n0)
n0.set_parent(None)

print getCheapestCost_recursive_dfs(n0) == 7
print getCheapestCost_iterative_dfs(n0) == 7 # this call mutates the original tree
print getCheapestCost_iterative_dfs(n0) #=> 13 (due to mutation of tree)