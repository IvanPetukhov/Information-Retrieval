import math
d_words_idf = {'car': 1.65, 'auto': 2.08, 'insurance': 1.62, 'best': 1.5}
words = ['car', 'auto', 'insurance', 'best']
d1_v = [27, 3, 0, 14]
d2_v = [4, 33, 33, 0]
d3_v = [24, 0, 29, 17]
q = [1, 0, 1, 0]
d1_tf = [x * 1.0 / sum(d1_v) for x in d1_v]
d2_tf = [x * 1.0 / sum(d2_v) for x in d2_v]
d3_tf = [x * 1.0 / sum(d3_v) for x in d3_v]

q_tf = [x * 1.0 / sum(q) for x in q]

def cos(arr1, arr2):
	l1, l2 = 0.0, 0.0
	s = 0.0
	for x,y in zip(arr1, arr2):
		s = s + x*y
		l1 = l1 + x**2
		l2 = l2 + y**2
	return s/math.sqrt(l1)/math.sqrt(l2)

def normalize(arr):
	len = math.sqrt(sum(map(lambda x: x**2, arr)))
	return list(map(lambda x: x/len, arr))

print ('cos(d1,q) = {0}'.format(cos(normalize(d1_tf), q_tf)))
print ('cos(d2,q) = {0}'.format(cos(normalize(d2_tf), q_tf)))
print ('cos(d3,q) = {0}'.format(cos(normalize(d3_tf), q_tf)))