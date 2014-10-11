"""
Given a list of coin denominations and a amount to generate. Find out the minimum number of coins that are required to generate the coins.
"""

def generate_coins(denoms, amount, change = []):
  flag = 0
  for coin in sorted(denoms, reverse = True):
    #print coin
    if coin <= amount:
      flag = 1
      break
  while amount >= coin:
    amount -= coin
    change.append(coin)
  if flag == 1 and amount != 0:
    change = generate_coins(denoms, amount, change)
  return change

def main():
  change = generate_coins([1, 5, 10, 25], 106)
  print change
if __name__ == "__main__":
  main()
