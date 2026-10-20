#Hw-W3
#1

def word_frequency(text):
    if not isinstance(text ,str):
        print("it must be string")
    elif not text.strip():
        print("please enter something!")
    else:
        words=text.split()
        word_count={}
        for word in words:
            if word in word_count:
                word_count[word]+=1
            else:
             word_count[word]=1
    
        print(sorted(
            word_count.items(), key=lambda item:item[1], reverse=True
            ))

text = "python is great and python is powerful and python is fun"
word_frequency(text)