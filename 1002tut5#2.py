word=input("please input a word:")
string=list[word]


def newWord():
    words= word.split("a"&"e"&"i"&"o"&"u"&"A"&"E"&"I"&"O"&"U")
    for i in words:
        wordss= words[len(words),-1]
    print(wordss) 
c=-1
c=word.find("a","e","i","o","u","A","E","I","O","U")
if c ==-1:
   print(word)
elif c==0:
    print(word,"add")
else:
    newWord()