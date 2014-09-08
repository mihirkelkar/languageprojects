def find_if_intersect(x, y):
  slope = x[0] * y[1] - x[1] * y[0]
  if slope == 0:
    return False
  return True

def line_intersect(line1, line2):
  x_cord_diff = [line1[0][0] - line1[1][0], line2[0][0] - line2[1][0]]
  y_cord_diff = [line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]]
  return find_if_intersect(x_cord_diff, y_cord_diff)

lines = \
[([37.788353, -122.387695], [37.829853, -122.294312]),
([37.429615, -122.087631], [37.487391, -122.018967]),
([37.474858, -122.131577], [37.529332, -122.056046]),
([37.532599,-122.218094], [37.615863,-122.097244]),
([37.516262,-122.198181], [37.653383,-122.151489]),
([37.504824,-122.181702], [37.633266,-122.121964])
]

intersection_map = {}
final_list = []

for ii in range(len(lines)):
  for jj in range(ii, len(lines)):
    if line_intersect(lines[ii], lines[jj]):
      #If both the lines intersect
      intersection_map[ii] = jj
      intersection_map[jj] = ii

print intersection_map
