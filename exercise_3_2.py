
sides = ['left','right']
maskOrNot = ['masked','masked', 'nonmasked']
numTrials = 1
numBlocks = 5

def generateTrials(sides, maskOrNot, numTrials, numBlocks):
	trials = []
	for block in range(numBlocks):
		for mask in maskOrNot:
			for side in sides:
				trial = ",".join([str(block),mask,side])
				trials.append(trial)
	
	for trial in trials:
		print trial

generateTrials(sides,maskOrNot,numTrials,numBlocks)