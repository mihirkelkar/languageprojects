def share_stock_one_sale(stock_array):
  min_so_far = float("inf")
  min_so_far_index = -1
  max_diff_so_far = -float("inf")
  sell_date = 0
  buy_date = 0
  for ii in range(len(stock_array)):
    if stock_array[ii] < min_so_far:
      min_so_far = stock_array[ii]
      min_so_far_index = ii
    
    else:
      if stock_array[ii] - min_so_far > max_diff_so_far:
        max_diff_so_far = stock_array[ii] - min_so_far
        buy_date = min_so_far_index
        sell_date = ii
  print max_diff_so_far, buy_date, sell_date

def main():
  share_stock_one_sale([10, 3, 7, 1, 4, 17, 7]) 

if __name__ == "__main__":
  main()   
