class Entity
	attr_reader :val
	def initialize(val)
		begin
			@val = Integer(val)
		rescue
			@val = val.to_s
		end
	end

	def <(someVal)
		result = 0
		begin
			# Integer comparison
			result = Integer(@val) <=> Integer(someVal.val)
		rescue
			# String comparison
			result = @val.to_s <=> someVal.to_s
		end
		return result==-1?true:false
	end

	def to_s
		@val.to_s	
	end
end
