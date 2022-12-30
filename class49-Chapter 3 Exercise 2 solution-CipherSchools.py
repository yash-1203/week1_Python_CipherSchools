# Exercise - WATCH COCO
# Ask user's name and age
# if user's name start with ('a' or 'A' )and age is above 10 then
# print 'you can watch coco movie'
# else print 'sorry, you cannot watch coco'
user_name = input("enter name : ")
user_age = int(input("enter age : "))
if user_age >= 10 and (user_name[0] == 'a' or user_name[0]) == "A":
    print("you can watch coco movie")
else:
    print("sorry, you cannot watch coco")
    
    
