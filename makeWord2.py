import itertools
import pickle
    
def makeWord2():
    words = list(input("please input alphabets>"))
    w_count = len(words)
    dic = pickle.load(open("sorted_english_dic.pickle", "rb"))

    index = w_count
    result = False
    result_list = []
    for i in range(w_count):
        # 大きい方から組み合わせを作る
        comb_list = list(itertools.combinations(words, index))
        for comb in comb_list:
            sorted_comb = "".join(sorted(comb))
            for k, v in dic.items():
                if k == sorted_comb:
                    result = True
                    result_list.append(v)
                    break
        index -= 1

    if result == False:
        print("None")
    else:
        # 重複している単語を消す
        unique_result_list = list(dict.fromkeys(result_list))
        for r in unique_result_list:
            print(r)
        
makeWord2()
