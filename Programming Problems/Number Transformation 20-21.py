# Overly complicated because why not

with open("Number Transformation input.txt", 'r') as f:

	for inp in f.read().split("\n"):
		splitInput = inp.split(" ")
		N = splitInput[0]

		P = len(N) - int(splitInput[1])

		result = list(map(lambda n, i: str(int(n) if i == P else (int(n) + int(N[P]) * (1 if i < P else -1)))[-1], N, range(len(N))))

		print(''.join(result))

# The same thing, but written better and without inline commands

with open("Number Transformation input.txt", 'r') as f:
	fileText = f.read()

	operationList = fileText.split('\n') # Split the file into each line, which is its own 2-number problem

	for operation in operationList: # Iterate through every operation
		[N, P] = operation.split(' ') # Break each one into both numbers

		PIndex = len(N) - int(P) # Change the indexing to be zero-indexed from left to right 
		
		result = ""

		for digit in N:
			if len(result) < PIndex: # To the left of P
				result += str(int(digit) + int(N[PIndex]))[-1] # Return the last character of the sum of each digit and the Pth digit
			elif len(result) > PIndex: # To the right of P
				result += str(int(digit) + int(N[PIndex]))[-1] # Return the last character of the differrence of each digit and the Pth digit
			else:
				result += digit # Otherwise, return the digit
		
		print(result)