require './sort.rb'

# Get Input
array = Array.new

puts "Enter the array"
gets.chomp().split(" ").each { |x| array.push(Entity.new(x)) }

# Call sort
Sort.InsertionSort(array)

# Print the sorted array
array.each { |x|
	print ' '+ x.to_s
}

print "\n"