def look_and_say(number):
  number  = list(number)
  result = ""
  temp = number.pop(0)
  times = 1
  while number:
    new_el = number.pop(0)
    if new_el == temp:
      times += 1
    else:
      result += str(times) + temp
      times = 1
    temp = new_el
  result += str(times) + temp
  return result 

def main():
  result = 1
  for ii in range(10):
    result = look_and_say(str(result))
    print result

if __name__ == "__main__":
  main()






