# problem
#ask a user to input a number containing more than one digit
#example- 1256
#calculate 1+2+5+6 and print


'''algorithm -(method to solve a problem in human language)
ask input in string, i.e don't change string to int
example-"1256"
pick a string character one by one and change to int
int(example[0]) + int(example[1])..... go upto len(example)-1'''

number = int(input("enter a number"))
# "1256" # length = 4, last index =3  
total = 0
i = 0
while i < number:
    total += i
    i += 1
print(total)
