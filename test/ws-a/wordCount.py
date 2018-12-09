# -*- coding: utf-8 -*-
import time
wordCountDic = {}
count_total = 0
wordProbability = {}

def word_count(content, bg_word, count_total):
	for line in content.split("\n"):
		for part in line.split("  "):
			count_total += 1
			part = part[0: part.find("/")]
			if part in bg_word:
				bg_word[part] += 1
			else:
				bg_word[part] = 1
	# return word count dictionary
	with open("../wordCount.txt", 'w') as file:
		for key, value in bg_word.items():
			file.write('{key} {value}\n'.format(key=key, value=value))
	with open("../wordProbability.txt", 'w') as file:
		for key, value in bg_word.items():
			p ='{:.8f}'.format(value/count_total)
			wordProbability[key] = p
			file.write('{key} {value}\n'.format(key=key, value=p))
			# file.write('{key} {value}\n'.format(key=key, value=round(value/count_total, 8)))
			# file.write('{key} {value}\n'.format(key=key, value=value/count_total))
	return bg_word

# print(0)
# start = time.time()
with open("../词性标注%40人民日报199801.txt", 'r', encoding='utf-8') as file:
	content = file.read()
	word_count(content, wordCountDic, count_total)

# end = time.time()
# timeAll = end - start
# print(timeAll)
# print(1)
