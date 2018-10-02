import sys

def BubbleSort(array):
	counter = 0
	i = 0
	j = 0
	n = len(array)
	done = True
	print("n = " + str(n))
	while i < (n - 1):
		#print("OUTER i is equal to " + str(i))
		done = True
		j = 0
		while j < (n - i - 1):
			#print("INNER j is equal to " + str(j))
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				done = False
			counter+=1	
			j += 1
		if done == True:
			break
		i += 1

	print("sorted array: " + str(array))
	return counter

def main():
  print("number of comparisons: " + str(BubbleSort([1, 2, 3, 4, 5, 6, 7])))
  
if __name__== "__main__":
  main()