import math

def dcg(vec):
	dcg = vec[0]
	for i in range(1, len(vec)):
		dcg += vec[i] / math.log(i+1)
	return dcg

sys1 = [4, 2, 4, 1, 2]
sys2 = [3, 2, 4, 4, 4]
dcg1 = dcg(sys1)
dcg2 = dcg(sys2)
print("system1: " + str(dcg1) + " system2: " + str(dcg2))
