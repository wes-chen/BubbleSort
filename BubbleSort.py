import argparse

def BubbleSort(array):
	counter = 0
	i = 0
	j = 0
	n = len(array)
	print("n = " + str(n))
	while i < (n - 1):
		#print("OUTER i is equal to " + str(i))
		j = 0
		while j < (n - i - 1):
			#print("INNER j is equal to " + str(j))
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
			counter+=1	
			j += 1
		i += 1

	print("sorted array: " + str(array))
	return counter

def main():
	CLI=argparse.ArgumentParser()
	CLI.add_argument(
	  "--array",  # name on the CLI - drop the `--` for positional/required parameters
	  nargs="*",  # 0 or more values expected => creates a list
	  type=int,
	  default=[0],  # default if nothing is provided
	)

	# parse the command line
	args = CLI.parse_args()
	print("number of comparisons: " + str(BubbleSort(args.array)))
  
if __name__== "__main__":
  main()