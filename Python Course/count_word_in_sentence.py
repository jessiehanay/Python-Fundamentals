#with built-in function
def countwords (sentence):
    return sentence.count(word)


sentence = input("enter a sentence: ")
word=input("enter a word that you want to search in the sentence")
#Calling the def function!!!!!
count=countwords(sentence)
print(f"the count of {word} is {count}")

#without built-in function

def countwords2(sentence2,searchword):
    count2=0
    words=sentence2.split()
    for i in words:
        if i == searchword:
            count2+=1
    return count2

sentence2 = input("enter another sentence: ")
searchword=input("enter a word that you want to search in the second sentence")
count2=countwords2(sentence2,searchword)
print(f"the count of {searchword} is {count2}")



