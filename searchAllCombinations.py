import itertools
import pickle

def searchAllCombinations():
    words = list(input("please input alphabet>"))
    w_count = len(words)
    dic = pickle.load(open("sorted_english_dic.pickle", "rb"))

    index = w_count
    result = False
    r_count = 0
    result_list = []
    one_point_list = ["a","b","d","e","g","i","n","o","r","s","t","u"]
    two_points_list = ["c","f","h","l","m","p","v","w","y"]
    three_points_list = ["j","k","q","x","z"]

    for i in range(w_count):
        # 大きい方から組み合わせを作る
        comb_list = list(itertools.combinations(words, index))
        unique_comb_list = list(dict.fromkeys(comb_list))
        for comb in unique_comb_list:
            sorted_comb = "".join(sorted(comb))
            if sorted_comb in dic:
                result_list.append(dic[sorted_comb])
                r_count += 1
                result = True

        index -= 1

    if result == False:
        print("None")
    else:
        result_dic = {}
        for r_word in result_list:
            score = 0
            for word in list(r_word):
                if word in one_point_list:
                    score += 1
                elif word in two_points_list:
                    score += 2
                elif word in three_points_list:
                    score += 3
            result_dic[r_word] = (score+1)**2
            
        sorted_result_dic = sorted(result_dic.items(), key=lambda x:x[1], reverse=True)
        print(sorted_result_dic[0])

searchAllCombinations()