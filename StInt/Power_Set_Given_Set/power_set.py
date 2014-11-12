def power_set(orig_set):
  power_set_size = 2 ** len(orig_set)
  for ii in range(0, power_set_size):
    counter = '{0:04b}'.format(ii)
    string = ''
    for ii in range(0, len(counter)):
      if counter[ii] == '1':
        string += orig_set[ii]
    print string

power_set(['a', 'b', 'c', 'd'])
