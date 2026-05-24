#stop if there are blank:

my_str="Hello World"
for letter in my_str:
    print(letter)
    if(letter==' '):
        break
print("Out of the loop")

