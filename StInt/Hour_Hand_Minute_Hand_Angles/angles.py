#!/usr/bin/python

def angle(hour, minute):
  minute_angle = minute * 6
  hour_angle = hour * 30 + minute * 0.5
  if hour_angle >= minute_angle:
    angle = hour_angle - minute_angle
  else:
    angle = minute_angle  - hour_angle
  if angle > 180:
    angle = 360 - angle
  return angle

def main():
  time_list = map(int, raw_input("What time in HH:MM format").split(":"))
  print angle(time_list[0], time_list[1])

if __name__ == "__main__":
  main()
