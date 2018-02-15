def repetition(letters, numberBeforeSwitch, numRepetitions):
	for i in range(numRepetitions):
		for letter in letters:
			for j in range(numberBeforeSwitch):
				print letter

repetition(['A','B'],1,1)
repetition(['A','B'],2,1)
repetition(['A','B'],2,2)
repetition(['A','B','C'],3,1)