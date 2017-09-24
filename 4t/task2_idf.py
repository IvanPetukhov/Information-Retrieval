import pymorphy2
import re
import math
import sys

#подключаем анализатор
morph = pymorphy2.MorphAnalyzer()

#разбиваем предложение на леммы
def repl(line):
	line = line.replace('\n', ' ')
	line = line.replace('.', ' ')
	line = line.replace(',', ' ')
	line = line.replace('!', ' ')
	line = line.replace('%', ' ')
	line = line.replace('^', ' ')
	line = line.replace('&', ' ')
	line = line.replace('*', ' ')
	line = line.replace('(', ' ')
	line = line.replace(')', ' ')
	line = line.replace('-', ' ')
	line = line.replace('+', ' ')
	line = line.replace('=', ' ')
	line = line.replace('{', ' ')
	line = line.replace('[', ' ')
	line = line.replace('}', ' ')
	line = line.replace(']', ' ')
	line = line.replace(':', ' ')
	line = line.replace(';', ' ')
	line = line.replace('"', ' ')
	line = line.replace('§', ' ')
	line = line.replace('?', ' ')
	line = line.replace('  ', ' ')
	line = line.replace('...', ' ')
	line = line.replace('--', ' ')
	words = line.split(' ')
	stat = {}
	for word in words:
		stat[morph.parse(word)[0].normal_form] = 0
	for word in words:
		stat[morph.parse(word)[0].normal_form] += 1
	if(stat.get('',0) != 0):
		stat.pop('')
	return stat

#открытваем файл со статьей
with open(sys.argv[2], 'r') as fs:
	line = ''.join(fs.readlines())
#открываем файл с запросом
with open(sys.argv[1], 'r') as fz:
	task = ''.join(fz.readlines())
#делим статью на предложения
sent = re.split('()[.?!\n"]', line)
#получаем леммы из запроса
tasks = repl(task)
#получаем леммы из предложений (sent2 -- без пустых предложений), значение -- tf слова в предложении
sents = []
sent2 = []
for i in sent:
	if(i != ''):
		sents.append(repl(i))
		sent2.append(i)
#находим idf для каждого слова в статье
idf = {}
for i in tasks:
	idf[i] = 0
for i in sents:
	for word in i:
		if(idf.get(word, 0) == 0):
			idf[word] = 1
		else:
			idf[word] += 1
for i in idf:
	if(idf[i] != 0):
		idf[i] = math.log10(len(sents) / idf[i])
#умножаем каждый вектор предложений и запроса на вектор idf
itasks = tasks
for i in itasks:
	itasks[i] = itasks[i]*idf[i]
isents = sents
for i in isents:
	for j in i:
		i[j] = i[j]*idf[j]
#нормализуем вектора предложений
nsents = isents
for i in nsents:
	ln = 0
	for t in i:
		ln += i[t]**2
	ln = math.sqrt(ln)
	for t in i:
		i[t] = i[t] / ln
#нормализуем запрос
ntasks = itasks
ln = 0
for i in ntasks:
	ln += ntasks[i]**2
ln = math.sqrt(ln)
for i in ntasks:
	ntasks[i] = ntasks[i] / ln
#для каждого предложения оставляем только те леммы, которые совпадают с леммами запроса (остальные обнулятся при вычислении косинуса угла между векторами)
nvect = []
for s in nsents:
	vec = {}
	for t in tasks:
		if(s.get(t, 0) != 0):
			vec[t] = s[t]
	nvect.append(vec)
#найдем косинус угла для каждого предложения, запишем в пары (косинус, номер предложения)
#косинус будет выглядеть как сумма всех произведений слов вектора запроса на соответствующие слова вектора предложения
#делить на их длины не надо, так как они будут равны 1
pairs = []
for i in range(0, len(nvect)):
	cs = 0
	for j in nvect[i]:
		cs += nvect[i][j]*ntasks[j]
	pairs.append((cs, i))
#сортируем. Чем ближе косинус к 1 -- тем меньше расстояние между векторами
pairs = sorted(pairs, key = lambda i:i[0], reverse = True)

with open(sys.argv[3], 'w') as t:
	t.write("Запрос: " + task + '\n\n')
	t.write("Выдача:\n\n")
	for w, v in pairs:
		t.write(str(w) + " " + sent2[v] + '\n')
