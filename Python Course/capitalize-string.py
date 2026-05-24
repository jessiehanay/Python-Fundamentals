str1=input("What movie is Princess Jasmine from?")
while str1.capitalize() != "Aladdin":
    str1=input("incorrect,try again")
print(f"congratulations,you got it! The answer was {str1.capitalize()}")