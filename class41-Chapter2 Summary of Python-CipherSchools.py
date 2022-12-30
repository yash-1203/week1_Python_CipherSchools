# strings
name = "harshit"

#string indexing
print(name[1])

# string slicing
print(name[-1:0:-1])

#take user input
age = input("enter your age: ") # strings
print(age)

#take two user inputs
user_name, age = input("enter your name and age :").split(",")
print(user_name)
print(age)

#len function
print(len(name))

#lower, upper, title method
print(name.lower())
print(name.upper())
print(name.title())

#find, replace, center method
r_pos = name.find("r")
r_pos2 = name.find("r",r_pos + 1)
print(r_pos2)

print(name.center(11,"*"))

#strings are immutable


