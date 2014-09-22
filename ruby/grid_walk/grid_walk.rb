require 'set'

start = [0, 0]
$visited = Set.new [start]
$queue = [start]

def sum_digits n
  sum = 0
  n *= -1 if n < 0

  while n > 0 do
    d = n / 10
    r = n % 10
    sum += r
    n -= r
    if d > 0
      n /= 10
    end
  end

  sum
end

def accessible? x, y
  !$visited.member?([x, y]) && sum_digits(x) + sum_digits(y) <= 19
end

def explore x, y
  if accessible? x, y
    p = [x, y]
    $visited.add p
    $queue << p
  end
end

until $queue.empty?
  x, y = $queue.shift

  explore x + 1, y
  explore x - 1, y
  explore x, y + 1
  explore x, y - 1
end

puts $visited.size
