def createnewstring(str1):
    length = len(str1)
    str1 = str1[0] + str1[length // 2] + str1[length - 1]
    return str1

print(createnewstring("PythonProgram"))


def createnewstring2(str2):
    length = len(str2)
    str2= str2[(length//2)-1] + str2[length//2] + str2[(length//2) + 1]
    return str2

print(createnewstring2("PythonProgram"))

#is the word is longer than 4 letters-print first 2 and last2 (create new string from them)
def createnewstring3(str3):
    length = len(str3)
    if length<4:
        return "error"
    else:
        str3 = str3[0] + str3[1] + str3[length - 2] + str3[length - 1]
        return str3

str3=input("enter your string")
print(createnewstring3(str3))

#check and add letters to the end of the string
def createnewstring4(str4):
    length = len(str4)
    if length<3:
        return "error"
    else:
        if(str4[length-3] + str4[length-2] + str4[length-1] == "ing"):
            str4 +="ly"
            return str4
        else:
            str4 += "ing"
            return str4

str4=input("enter your word")
print(createnewstring4(str4))







