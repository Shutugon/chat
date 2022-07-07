def read_file(filename): 
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:  # -sig可以把亂碼移除
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None  # 如果第一行不是名字，先把person設為None可以避免程式當掉
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')   # split後會變成一個「清單」
		time = s[0]  # 清單中第一項是時間，第二項是人名 
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in s[2:]:   # [2:]代表從第一項到最後一項，通常用在不知道整句話到底有多少項時，不包含結束值
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else: 
				for msg in s[2:]:
					viki_word_count += len(msg)
	print('Allen 說了', allen_word_count, '個字')
	print('Allen 傳了', allen_sticker_count, '張貼圖')
	print('Allen 傳了', allen_image_count, '張照片')
	print('Viki 說了', viki_word_count, '個字')
	print('Viki 傳了', viki_sticker_count, '張貼圖')
	print('Viki 傳了', viki_image_count, '張照片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)   # 把lines這個清單丟進convert的函數中
	#write_file('output.txt', lines)

main()