import pickle

def makeWord():
    dic = pickle.load(open("sorted_english_dic.pickle", "rb"))
    keyword = input("アルファベットを入れてください>")
    sorted_keyword = "". join(sorted(keyword))
    result = False
    for k, v in dic.items():
        if k == sorted_keyword:
            result = True
            print(v)
            break
    if result == False:
        print("None")
        
            
makeWord()
