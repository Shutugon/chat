
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip('\n'))

for line in lines:
	s = line.split(' ')
	time = s[0][:5]    # 因為時間固定是五個字，如12:00共五位，以這個手法可將時間、人名取出
	name = s[0][5:]
	print(time)
	print(name)