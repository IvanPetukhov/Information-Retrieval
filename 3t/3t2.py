import numpy as np
import math
from sklearn.preprocessing import normalize
from scipy.spatial.distance import cosine

def fcos(arr1, arr2):
	l1, l2 = 0.0, 0.0
	s = 0.0
	for x,y in zip(arr1, arr2):
		s = s + x*y
		l1 = l1 + x**2
		l2 = l2 + y**2
	return s/math.sqrt(l1)/math.sqrt(l2)

arr1 = np.array([27, 3, 0, 14])
arr2 = np.array([4, 33, 33, 0])
arr3 = np.array([24, 0, 29, 17])
arr1 = np.array([np.log(x + 1) for x in arr1])
arr2 = np.array([np.log(x + 1) for x in arr2])
arr3 = np.array([np.log(x + 1) for x in arr3])
arridf = np.array([1.65, 2.08, 1.62, 1.5])
arr = np.array([1, 0, 1, 0])
arr1 = arr1 * arridf
arr2 = arr2 * arridf
arr3 = arr3 * arridf
arr = arr * arridf
arr1 = arr1 / np.linalg.norm(arr1)
arr2 = arr2 / np.linalg.norm(arr2)
arr3 = arr3 / np.linalg.norm(arr3)
cos = {};
cos['d1'] = fcos(arr, arr1)
cos['d2'] = fcos(arr, arr2)
cos['d3'] = fcos(arr, arr3)
pairs = [(k, v) for k, v in cos.items()]
pairs = sorted(pairs, key = lambda i: i[1], reverse = True)
with open('result2.txt', 'w') as t:
	for w, v in pairs:
		t.write(w + ' ' + str(v) +  '\n');
