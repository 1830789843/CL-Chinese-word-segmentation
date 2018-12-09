import os
from math import log

document_path = './data/cut_stop'

def read_file(filepath):
    data = {}  # content of document (doc, content)
    # list all files of a directory(Document)
    for dir_item in os.listdir(filepath):
        # join dir path and file name
        dir_item_path = os.path.join(filepath, dir_item)
        # check whether a file exists before read
        if os.path.isfile(dir_item_path):
            with open(dir_item_path, 'r', encoding='utf-8') as f:
                # read content of document (doc, content)
                data[dir_item] = f.read()
    # data(dict)
    return data


def word_count(content, bg_word):
    for part in content.split():
        if part in bg_word:
            bg_word[part] += 1
        else:
            bg_word[part] = 1
    # return word count dictionary
    return bg_word


def doc_preprocess(dictionary):
    # term probability(word_count / word sum)
    for doc_key, doc_content in dictionary.items():
        doc_words = word_count(doc_content, {})
        dictionary[doc_key] = doc_words
        # sorted(doc_words.items(), key=lambda d: d[1], reverse=True)
    return dictionary


def compute_TFIDF(doc_wordcount):
    tfidf = {}
    total_docs = len(doc_wordcount.keys()) * 1.0
    # compute idf
    doc_freq = {}
    for doc, word_count_dict in doc_wordcount.items():
        for word, count in word_count_dict.items():
            if word in doc_freq:
                doc_freq[word] += 1
            else:
                doc_freq[word] = 1
    # compute tfidf

    for doc, word_count_dict in doc_wordcount.items():
        doc_tfidf = {}
        if len(word_count_dict)>0:
            max_item_count = max(word_count_dict.values())
        else:
            max_item_count = 1

        for word, count in word_count_dict.items():
            idf = log(total_docs / doc_freq[word])
            tf = count / max_item_count
            doc_tfidf[word] = tf * idf
        tfidf[doc] = doc_tfidf

    return [tfidf, doc_freq]



data = read_file(document_path)
doc_wordcount = doc_preprocess(data)
total_docs = len(doc_wordcount.keys()) * 1.0
[doc_model, doc_freq] = compute_TFIDF(doc_wordcount)

index = sorted(doc_freq.items(), key=lambda d: d[1], reverse=True)
word_to_num = {}
with open('./index.txt', 'w', encoding='utf-8') as f:
    for i, t in enumerate(index):
        f.writelines(str(t[0]) + ' ' + str(t[1]) + '\n')
        word_to_num[t[0]] = i

with open('./doc_model.txt', 'w', encoding='utf-8') as f:
    for doc_name, doc_tfidf in doc_model.items():
        terms = {}
        for key, val in doc_tfidf.items():
            terms[word_to_num[key]] = val
        terms2 = index = sorted(terms.items(), key=lambda d: d[0])

        f.write('{')
        for i, v in terms2:
            f.write('"'+str(i)+'"'+':'+'"'+str(v)+'"'+',')
        f.write('}\n')

import timeit
from collections import defaultdict
import numpy as np
from math import log, sqrt
import operator

query = {'1':'上市 公司 业务'}
query_wordcount = {}

for q_key, q_content in query.items():
    query_wordcount[q_key] = word_count(q_content, {})

query_model = defaultdict(dict)
for q_key, word_count_dict in query_wordcount.items():
    max_freq = np.max(np.array(word_count_dict.values()), axis = 0)
    for word, count in word_count_dict.items():
        if word in doc_freq:
            idf = log(1 + total_docs / doc_freq[word])

        else:
            idf = log(1 + total_docs)

        query_model[q_key][word] = (1 + log(count)) * idf

#with open("test_query_model_tfidf.pkl", "wb") as file: Pickle.dump(query_model, file, True)
'''
for q, w_uni in query_model.items():
    if q in HMMTraingSetDict:
        continue
    else:
        query_model.pop(q, None)

'''
#print(len(query_model.keys()))

# query process
print("query ...")
start = timeit.default_timer()
feedback_model = []
feedback_ranking_list = []
doc_length = {}
#with open("doc_model_tfidf_dict.pkl", "wb") as file: Pickle.dump(doc_model, file, True)
for step in range(2):
    query_docs_point_dict = {}
    AP = 0
    mAP = 0
    for q_key, q_words_count_list in query_model.items():
        docs_point = defaultdict(int)
        for doc_key, doc_words_count_dict in doc_model.items():
            relevant_point = 0
            query_length = 1

            # calculate each query value for the document
            for doc_word, doc_word_count in doc_words_count_dict.items():
                if not doc_word in q_words_count_list:
                    continue
                else:
                    relevant_point += q_words_count_list[doc_word] * doc_word_count

            if not doc_key in doc_length:
                doc_length[doc_key] = sqrt((np.array(list(doc_words_count_dict.values())) ** 2).sum(axis = 0))
            if doc_length[doc_key]==0:
                doc_length[doc_key]=1000

            # cosine measure
            relevant_point /= (query_length * doc_length[doc_key])
            docs_point[doc_key] = relevant_point
        # sorted each doc of query by point
        docs_point_list = sorted(docs_point.items(), key=operator.itemgetter(1), reverse = True)
        query_docs_point_dict[q_key] = docs_point_list
    # mean average precision
    # mAP = assessment.mean_average_precision(query_docs_point_dict)
    print(query_docs_point_dict)
    # print("mAP:", mAP)
    print("feedback:", step)
    '''
    if step < 1:
        #feedback_ranking_list = HMMTraingSetDict
        feedback_ranking_list = dict(query_docs_point_dict)
        [query_model, feedback_model] = Expansion.extQueryModel(query_model, feedback_ranking_list, doc_model, feedback_model, None)
        with open("rel_vsm_dict.pkl", "wb") as file: Pickle.dump(query_model, file, True)
    '''
stop = timeit.default_timer()
print("Result : ", stop - start)


