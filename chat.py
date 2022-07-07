def read_file(filename): 
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:  # -sig可以把亂碼移除
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	for line in lines:
		if line == 'Annie':   # 一行一行印出清單中的內容
			person = 'Annie'  # 如果在講話的是Annie，就把person存成Annie
			continue          # continue是希望跳過append，因為根本還沒有對話紀錄產生 
		elif line == 'Eason':
			person = 'Eason'
			continue

		new.append(person + ': ' + line)  # 字串合併，line是對話紀錄
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)   # 把lines這個清單丟進convert的函數中
	write_file('output.txt', lines)

main()