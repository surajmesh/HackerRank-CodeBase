
## word count

'''Que. : You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. Note: Each input line ends with a "\n" character.

Sample Input :

    4
    bcdef
    abcdefg
    bcde
    bcdef

Sample Output

    3
    2 1 1
'''



from collections import Counter

def occurance_count(num):
    list_1 = []
    for i in range(num):
        words = input()
        list_1.append(words)
        
    dis_count_words = len(set(list_1))
        
   
    word_counts = Counter(list_1)

    uni_count = []
    for key,value in word_counts.items():
        uni_count.append(value)
        
        
    str_uni_count = ' '.join(map(str,uni_count))
    
    
    
    
    return dis_count_words,str_uni_count


result = occurance_count(4)
print(result[0])
print(result[1])
