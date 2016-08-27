#!/usr/bin/python

class Solution(object):
	def reverseVowels(self, s):
		vowels = ['a','e','i','o','u','A','E','I','O','U']
		array = list(s)
		i,j = 0,len(array)-1

		while i<j:
			if(array[i] in vowels and array[j] in vowels):
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
				i = i + 1
				j = j - 1
			if(array[i] not in vowels):
				i = i + 1
			if(array[j] not in vowels):
				j = j - 1

		return ''.join(array)


print Solution().reverseVowels("nikhel")