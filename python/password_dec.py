"""

Chef changed the password of his laptop a few days ago, but he can't remember it today. Luckily, he wrote the encrypted password on a piece of paper, along with the rules for decryption.
The encrypted password is a string S consists of ASCII printable characters except space (ASCII 33 - 126, in decimal notation, the same below). Read here for more details: ASCII printable characters.
Each rule contains a pair of characters ci, pi, denoting that every character ci appears in the encrypted password should be replaced with pi. Notice that it is not allowed to do multiple replacements on a single position, see example case 1 for clarification.
After all the character replacements, the string is guaranteed to be a positive decimal number. The shortest notation of this number is the real password. To get the shortest notation, we should delete all the unnecessary leading and trailing zeros. If the number contains only non-zero fractional part, the integral part should be omitted (the shortest notation of "0.5" is ".5"). If the number contains zero fractional part, the decimal point should be omitted as well (the shortest notation of "5.00" is "5").
Please help Chef to find the real password.
Input

The first line of the input contains an interger T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains a single interger N, denoting the number of rules.
Each of the next N lines contains two space-separated characters ci and pi,
denoting a rule.
The next line contains a string S, denoting the encrypted password.
Output

For each test case, output a single line containing the real password.
Constraints

1 ≤ T ≤ 1000
0 ≤ N ≤ 94
All characters in S and ci may be any ASCII printable character except space. (ASCII 33 - 126)
All ci in a single test case are distinct.
pi is a digit ("0" - "9") or a decimal point "." (ASCII 46).
The total length of S in a single input file will not exceed 106.


"""

#!/usr/bin/python
tt = input()
while tt:
  rules = []
  nn = input()
  for i in range(nn):
    rules.append(raw_inputs().split())
  pwd = raw_input()
  for ii in rules:
    pwd = pwd.replace(ii[0], ii[1])
  #replace leading zeroes:
  for i in range(len(pwd)):
    if pwd[i] != '0':
      delteleader = i
      break
    else:
      pass
  if '.' in pwd:
    temp = pwd.split('.'):
    index_pre = len(temp[0])
    dec = temp[1]
    for i in range(len(dec)):
      if dec[i] != '0':
        deletetrailer = index_pre + 2 + i
      else:
        continue

pwd = pwd[deleteleader: delete_trailer]
