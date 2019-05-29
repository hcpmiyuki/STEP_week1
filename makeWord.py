import itertools
import pickle
    
def makeWord2():
    words = list(input("please input alphabet>"))
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
            if sorted_comb in dic:
                print(dic[sorted_comb])
                result = True
                break
                
        if result:
            break
            
        index -= 1

    if result == False:
        print("None")
        
makeWord2()
