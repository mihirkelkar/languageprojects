def nearest_repeat(string_array):
  word_hash = {}
  min_distance = [float("inf"), '']
  for ii in range(len(string_array)):
    try:
      temp = ii - word_hash[string_array[ii]]
      if temp < min_distance[0]:
        min_distance[0] = temp
        min_distance[1] = string_array[ii]
      word_hash[string_array[ii]] = ii
    except:
      word_hash[string_array[ii]] = ii
  return min_distance


def main():
  print nearest_repeat(["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "play", "and", "no", "results"])

if __name__ == "__main__":
  main()
