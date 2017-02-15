import random
wlist = []
word = "myself"
print (word)
#making a list
#mocking users input = index aka list
#scramble users input
#print users input
def scramble_word(word):        
    if len(word) >= 4:
        split = list(word)
        first = split[0]
        last = split[-1]
        firstlast_l = split[0:-1]
        random.shuffle(firstlast_l)
        firstlast_l.insert(0, first)
        firstlast_l.append(last)
        final = ''.join(firstlast_l)
        print(final)
scramble_word(word)
        
    
    
