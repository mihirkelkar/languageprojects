#!/usr/bin/ruby
fileContent = File.open(ARGV[0]).readlines
fileContent.each do |lines|
  if lines != nil
  lines = lines.chomp
  center_coords = /Center: \((.+)\);/.match(lines).captures[0].gsub(",","").split()
  radius = /Radius: (\d+\.\d+);/.match(lines).captures[0].to_f
  point_coords = /Point: \((.+)\)/.match(lines).captures[0].gsub(",","").split()
  euclidian_distance = Math.sqrt((center_coords[0].to_f - point_coords[0].to_f) ** 2 + (center_coords[1].to_f - point_coords[1].to_f) ** 2)
  if euclidian_distance < radius
    puts "true"
  else
    puts "false"
  end
  end
end
