name = input("Hello what is your name?")
midgrade = int(input("Please insert your middle test grade"))
midgrade = midgrade * 0.4
examgrade = int(input("Please insert your exam grade"))
examgrade = examgrade * 0.6
finalgrade= int(midgrade+examgrade)
print(f"Hey {name}  your final grade in Python course is: {finalgrade}")
