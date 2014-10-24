#!/usr/bin/python

def combination_sum(can_list, target_number, result, solutions):
	if len(can_list) > 0 and sum(result) < target_number:
		for ii in range(0, len(can_list)):
			if sum(result) + can_list[ii] == target_number:
				result.append(can_list[ii])
				if sorted(result) not in solutions:
				  solutions.append(sorted(result))
				  return solutions
			elif sum(result) + can_list[ii] < target_number:
				solutions = combination_sum(can_list[:ii] + can_list[ii + 1:], target_number,\
				 result + [can_list[ii]], solutions)
		return solutions		

def main():
	can_list = sorted([10,1,2,7,6,1,5])
	solutions = combination_sum(can_list, 8, [], [])
	print solutions

if __name__ == "__main__":
	main()