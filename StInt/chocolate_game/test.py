import random

def chart_boost(number):
  print 'Chart'*(not(number%3))+'Boost'*(not(number%5)) or number

def gen_fhun_random_numbers():
  counter = 0
  while counter < 500:
    chart_boost(random.randint(1, 500))
    counter += 1
    
def main():
  gen_fhun_random_numbers()

if __name__ == "__main__":
  main()
