def uneaten_leaves(leaf_count, multiples):
  leaves = [0 for ii in range(leaf_count + 1)]
  for ii in multiples:
    factor = ii
    counter = ii
    while(counter <= leaf_count):
      leaves[counter] = 1
      counter += factor
  return len([ii for ii in leaves[1:] if ii == 0])

def main():
  print uneaten_leaves(10, [2, 4, 5])

if __name__ == "__main__":
  main()
