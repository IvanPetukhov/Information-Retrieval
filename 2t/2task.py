import pymorphy2
morph = pymorphy2.MorphAnalyzer()
with open('text.txt', 'r') as f:
	line = ''.join(f.readlines())
line = line.replace('\n', '')
line = line.replace('.', '')
line = line.replace(',', '')
line = line.replace('!', '')
line = line.replace('%', '')
line = line.replace('^', '')
line = line.replace('&', '')
line = line.replace('*', '')
line = line.replace('(', '')
line = line.replace(')', '')
line = line.replace('-', '')
line = line.replace('+', '')
line = line.replace('=', '')
line = line.replace('{', '')
line = line.replace('[', '')
line = line.replace('}', '')
line = line.replace(']', '')
line = line.replace(':', '')
line = line.replace(';', '')
line = line.replace('"', '')
line = line.replace('§', '')
line = line.replace('?', '')
line = line.replace('  ', ' ')
words = line.split(' ')
stat = {}
for i in words:
	stat[morph.parse(i)[0].normal_form] = 0
for i in words:
	stat[morph.parse(i)[0].normal_form] += 1 
stat.pop('')
#for i in stat:
#	stat[i] = stat[i] / words.__len__()
pairs = [(k, v) for k, v in stat.items()]
pairs = sorted(pairs, key = lambda i:i[1], reverse = True)
with open('result.txt', 'w') as t:
	for w, v in pairs:
		t.write(w + ' ' + str(v) + '\n')