#!/usr/bin/python
import collections

def construct_graph(input):
  binary_tree_graph = collections.defaultdict(list)
  tree_children = {}
  input = input.split(" ")
  for ii in input:
    ii = ii[1:-1].split(",")
    binary_tree_graph[ii[0]].append(ii[1])
    if len(binary_tree_graph[ii[0]]) > 2:
      print "Error One more than two children"
      return
    tree_children[ii[1]] = ii[0]
  print binary_tree_graph
  print '- - - - - - - - - - \n- - - - - - - - - -'
  print tree_children
  root = check_error(binary_tree_graph, tree_children)
  print root
  return build_s_expression(binary_tree_graph, root)

def check_error(binary_tree, tree_children):
  root_counter = 0
  for ii in binary_tree.keys():
    try:
      tree_children[ii]
    except:
      root = ii
      root_counter += 1
  if root_counter != 1:
    print "Raising error 3. Multiple root nodes found"
    return
  return root
  
def build_s_expression(binary_tree, root):
  s_expression = '(' + root
  try:
    for ii in binary_tree[root]:
      s_expression +=  build_s_expression(binary_tree, ii) + ')'      
  except:
    return s_expression
  return s_expression
print construct_graph('(A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)')    
