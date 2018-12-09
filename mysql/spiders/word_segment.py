# encoding=utf-8
import jieba
import process_doc

content = process_doc.read_file('./data/raw/')

stopWordsSet = set()

with open('../../ChineseStopWords.txt', 'r', encoding='utf-8') as f:
    for word in f.readlines():
        stopWordsSet.add(word.strip())

for key in content:
    seg_list = jieba.lcut(content[key])  # 默认是精确模式

    for item in seg_list:
        if item in stopWordsSet:
            seg_list.remove(item)

    print("  ".join(seg_list))

    with open('./data/cut_stop/'+key, 'w', encoding='utf-8') as f:
        for word in seg_list:
            f.write(word+' ')
