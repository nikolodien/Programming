class MaxSubarray
	attr_accessor :differences
	def initialize(input)
		@input = input
		@differences = Array.new
		computeDifferences()
		@result = Array.new
	end

	def computeDifferences
		if @input.length>0
			for i in 1...@input.length
				@differences << @input[i]-@input[i-1]
			end
		end
	end
	
	def computeResult
		
	end

	def to_s()
		if @input.length>0 and @result.length=0
			computeResult()
		end
		@result.each {|x| print ' '+x.to_s}
	end
end

#Get input
ip = Array.new
gets.chomp.split(" ").each{|x| ip.push(Integer()) }


#Call MaxSubarray
msub = MaxSubarray.new(ip)

#Call to compute the final answer
msub.to_s()
