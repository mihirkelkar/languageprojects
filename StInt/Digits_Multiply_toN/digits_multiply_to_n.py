def digits_multiply_to_n(number):
  result = list()
  if number < 10:
    return number + 10
  elif number >= 10:
    for ii in range(9, 1, -1):
      while number % ii == 0:
        number = number / ii
        result.append(ii)
    if number > 10:
      print "Not possible"
    else:
      return "".join(map(str, result)[::-1])


def main():
  print digits_multiply_to_n(100)

if __name__ == "__main__":
  main()
