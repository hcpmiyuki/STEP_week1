# preparing dictionary
import requests
import pickle

## downloadong dictionary
url = "https://icanhazwordz.appspot.com/dictionary.words" 
response = requests.get(url)
response.encoding = response.apparent_encoding

english_dic = response.text.split('\n')
sorted_english = {}
sorted_english_dic = {}
## sort
### 単語の文字をソート
for word in  english_dic:
    sorted_word =  "". join(sorted(word))
    #insert sorted_word to key,original word to value
    sorted_english[sorted_word] = word

### listをkeyでソート
sorted_english = sorted(sorted_english.items())
### タプルからdict型に戻す
for s_word, o_word in sorted_english:
    sorted_english_dic[s_word] = o_word
    
print(sorted_english_dic)
pickle.dump(sorted_english_dic, open("sorted_english_dic.pickle", "wb"))