#!/usr/bin/python

"""
Given a asorted array, write an algorithm to create a binary tree with minimal height.
"""

"""
Make the middle element the root of the tree
Add left array to left subtree (using middle of the left list as a first child)
Add right side to right subarray
"""

def addToTree(array, start, end):
  if start > end:
    return None
  else:
    mid = (start + end) / 2
    temp = Node(array[mid])
    temp.left = addToTree(array, start, mid - 1)
    temp.right = addToTree(array, mid + 1, end)
    return temp

def main():
  array = [1,2,3,4,5,6,7,8,9]
  return addToTree(array, 0, len(array) - 1)

if __name__ == "__main__":
  main()
