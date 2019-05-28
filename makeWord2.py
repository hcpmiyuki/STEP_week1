import itertools
import pickle
    
def makeWord2():
    words = list(map(str, input("please input alphabet>").split()))
    w_count = len(words)
    dic = pickle.load(open("sorted_english_dic.pickle", "rb"))

    index = w_count
    result = False

    for i in range(w_count):
        # 大きい方から組み合わせを作る
        comb_list = list(itertools.combinations(words, index))
        for comb in comb_list:
            sorted_comb = "".join(sorted(comb))
            for k, v in dic.items():
                if k == sorted_comb:
                    result = True
                    print(v)
                    break
            
            if result:
                break
        
        if result:
            break
        index -= 1

    if result == False:
        print("None")
        
makeWord2()
