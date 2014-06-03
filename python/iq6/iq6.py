#!/usr/bin/python

def make_prev(i, array):
	mult = 1
	for i in range(i, -1, -1):
		mult = mult * array[i]
	return mult	

def make_next(i, array):
	mult = 1
	for i in range(i, len(array)):
		mult = mult * array[i]
	return mult

array  = [2,3,1,4]
prev_array = [1] + [make_prev(i, array) for i in range(0, len(array))]
next_array = [make_next(i, array) for i in range(0, len(array))] + [1]
final_array = [prev_array[i] * next_array[i + 1] for i in range(0, len(array))]
print final_array
