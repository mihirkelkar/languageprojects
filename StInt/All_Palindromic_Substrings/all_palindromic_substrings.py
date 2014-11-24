def all_palindromic_substrings(string):
  result = list()
  for ii in range(0, len(string)):
    result += check_palindrome(string, ii)
  return result

def check_palindrome(string, ii):
  start = ii
  end = start
  result = list()
  while start >= 0 and end < len(string):
    if string[start:end + 1] == string[start:end + 1][::-1]:
      result.append(string[start:end + 1])
      start -= 1
      end += 1
    else:
      break
  return result

def main():
  print all_palindromic_substrings(raw_input("Enter a string").lower())

if __name__ == "__main__":
  main()
