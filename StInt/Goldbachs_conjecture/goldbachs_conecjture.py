import math

def goldbachs_conjecture(number):
  if number % 2 != 0:
    print "Not an even number"
    return False
  for ii in range(3, number / 2 + 1):
    if isPrime(ii) and isPrime(number - ii):
      print ii, number - ii
      return True

def isPrime(number):
  for ii in range(2, int(math.sqrt(number)) + 1):
    if number % ii == 0:
      return False
  return True

def main():
  goldbachs_conjecture(18)

if __name__ == "__main__":
  main()
