N = int(input())
word_dic = {}

for i in range(N):
    word = input()
    word_dic[word] = len(word)

tmp_dic = dict(sorted(word_dic.items(), key = lambda x : x[0]))
sort_dic = sorted(tmp_dic.items(), key= lambda x : x[1])

for i in sort_dic:
    print(i[0])
