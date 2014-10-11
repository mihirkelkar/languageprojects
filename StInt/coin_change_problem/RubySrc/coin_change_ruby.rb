#!/usr/ruby

def coin_change(denoms, amount, change)
  flag = 0
  coin = 0
  denoms.sort.reverse.each do |ii|
    if ii <= amount
      flag = 1
      coin = ii
      break
    end
  end
  while amount >= coin
    amount -= coin
    change << coin
  end
  if coin == 0
    return "amount too small"
  end
  if flag == 1 && amount != 0
    change = coin_change(denoms,amount,change)
  end
  return change
end

def main()
  change = coin_change [1,5,10,25], 106, []
  puts change
end

main
