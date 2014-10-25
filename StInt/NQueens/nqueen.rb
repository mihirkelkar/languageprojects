#!/usr/bin/ruby

def solver(board, count)
	if count > 0
		for ii in 0..(board.length - 1)
			if check(board.length - count, ii, board)
				board[board.length - count][ii] = 1
				solver(board, count - 1)
				board[board.length - count][ii] = 0
			end	
		end
	else
		puts board	
	end	
end	

def check(ii, jj, board)
	#Check the row above you
	if ii > 0
		for elem in 0..(ii - 1)
			if board[elem][jj] == 1
				return false
			end	
		end	
	end	
	#check the left diagonal above you
	row = ii - 1
	col = jj - 1
	while row >= 0
		while col >= 0
			if board[ii][jj] == 1
				return false
			end	
			col -= 1
		end	
		row -= 1
	end	
	#Check the right diagonal above you. 
	row = ii - 1
	col = jj + 1
	while ii >= 0
		while jj <= board.length - 1
			if board[row][col] == 1
				return false
			end
			col -= 1
		end
		row -= 1
	end
	return true			
end	