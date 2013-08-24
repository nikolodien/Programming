for i in range(1,11):
	print reduce(lambda x,y:x*2 if (y=='T' or y=='D' or y =='L' or y=='F') else x, list(raw_input()), 1)
