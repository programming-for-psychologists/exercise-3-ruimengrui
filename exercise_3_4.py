import random

sides = ['left','right']
maskOrNot = ['masked','masked', 'nonmasked']
numTrials = 1
numBlocks = 5

def generateTrials(sides, maskOrNot, numTrials, numBlocks):
	for block in range(numBlocks):
		trials = []
		for mask in maskOrNot:
			for side in sides:
				trial = ",".join([str(block),mask,side])
				trials.append(trial)
		random.shuffle(trials)
		for trial in trials:
			print trial

generateTrials(sides,maskOrNot,numTrials,numBlocks)