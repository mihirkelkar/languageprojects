def reverse_a_string_inplace(string):
  string = list(string)
  print string
  left = 0
  right = len(string) - 1
  while(left < right):
    string[left], string[right] = string[right], string[left]
    left += 1
    right -= 1
    print string
  print "".join(string)

reverse_a_string_inplace("mihir kelkar")
