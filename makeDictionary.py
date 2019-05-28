# preparing dictionary
import requests
import pickle

## downloadong dictionary
url = "https://icanhazwordz.appspot.com/dictionary.words"
response = requests.get(url)
response.encoding = response.apparent_encoding

english_dic = response.text.split('\n')
q_english_dic = []
sorted_english_dic = {}

# quをqに置き換える
for word in english_dic:
    q_english_dic.append(word.replace('qu', 'q').replace('Qu', 'Q'))
    
## sort
### 単語の文字をソート
for word in  q_english_dic:
    sorted_word =  "". join(sorted(word))
    # insert sorted_word to key,original word to value
    sorted_english_dic[sorted_word] = word


pickle.dump(sorted_english_dic, open("sorted_english_dic.pickle", "wb"))
