import pickle
# reading dictionary
dic = pickle.load(open("sorted_english_dic.pickle", "rb"))

def binarySearch(array, target):
    if len(array) == 0:
        return False
    else:
        mid = len(array) // 2
        if array[mid] == target:
            return array[mid]
        else: 
            if array[mid] > target:
                return binarySearch(array[:mid], target)
            else:
                return binarySearch(array[mid:+1], target)

def makeWord(dictionary, keyword):
    sorted_keyword = "". join(sorted(keyword))
    # list of sorted word 
    sorted_dic_words = list(dictionary.keys())
    result = binarySearch(sorted_dic_words, sorted_keyword)
    if result == False:
        return False
    else:
        return dictionary[result]

print(makeWord(dic, "moonstarer"))
