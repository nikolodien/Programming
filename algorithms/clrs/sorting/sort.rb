require './Entity.rb'

module Sort

	module_function :InsertionSort
	module_function :MergeSort
	module_function :HeapSort

	def InsertionSort(array)
		for card in 1...array.length
			place = card-1
			key = array[card]
			until place<0 || array[place]<key 
				array[place+1]=array[place]
				place = place-1
			end
			array[place+1] = key
		end
	end

	def MergeSort(array)

	end

	def HeapSort(array)

	end

end
