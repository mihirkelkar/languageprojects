#!/usr/bin/ruby
$letter = {"1" => '1', "2" => "ABC", "3" => "DEF", "4" => "GHI", "5" => "JKL", "6" => "MNO", "7" => "PRS", "8" => "TUV", "9" => "WXY", "0" => "0"}
def testmethod(cur_digit, chars = '')
	if cur_digit == $len - 1
		letters = $letter[$number[cur_digit]]
		letters.split("").each do |item|
			$file.write(chars + item + "\n")
		end
	else
		letters = $letter[$number[cur_digit]]
		letters.split("").each do |item|
			testmethod(cur_digit + 1, chars + item)
		end		
	end	
end

def main()
	while true
		puts("Enter your 7 digit telephone number")
		$number = gets().chomp
		$number.gsub!("-","")
		if $number.length == 7
			$len = 7
    		break 
		end
	end
	$file = File.open("word", "w")
	testmethod(0)
	$file.close	 
end
main()