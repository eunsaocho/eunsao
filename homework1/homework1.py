# File: homework1. py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) #this is an integer, whole num
b = 1.5
print(b)
print(type(b)) #this is a float, a decimal
c = 3j
print(c)
print(type(c)) #this is a complex
d = "hello"
print(d)
print(type(d)) #this is a String
e = [1, 2, 3]
print(e)
print(type(e)) #this is a list
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #this is a dictionary
g = (1, 2)
print(g)
print(type(g)) #this is a tuple
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #this is a list
i = True
print(i)
print(type(i)) #this is a bool
j = None
print(j)
print(type(j)) #this is NoneType
k = [True, "blue", 12]
print(k)
print(type(k)) #this is a list
l = str(14)
print(l)
print(type(l)) #this is a String
m = 1e4
print(m)
print(type(m)) #this is a float

#1. We found 9 types
#2: String, float, list, Nonetype, bool, tuple, dictionary, int, complex
#3. [True, "blue", 12] and [1, 2, 3] are a lists
# str(14) and "hello" are Strings, 1.5 and 1e4 are floats
#4. it is a float because it has a decimal. str() can make a
# number into a String. 
# 5. bytes

# --- Booleans ---
10 > 9 #True
10 == 9 #False
10 <= 9 #False
bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True
bool(True) #True
bool(False) #False
bool(0) #False
bool("") #False
bool(" ") #True
bool(()) #False
bool([]) #False
bool({}) #False
bool(True and False) #False
bool(True and True) #True
bool(False and False) #False
bool(True or False) #True
bool(True or True) #True
bool(False or False) #False
bool(not(False)) #True
bool(not(True)) #False

#1. Empty values are False
#2. 0 is false
#3. 10==10 because 10 is equal to 10
#4. 10==9 because 10 is not equal to 9. 

#--- Arithmetic Operators ---
print(10 + 5) #15
print(10 - 5) #5
print(2 * 4) #8
print(6 / 3) #2.0
print(5 % 2) #1
print(3 ** 2) #9
print(15 // 2) #7

#--- Comparison Operators ---
print(5 == 2) #False
print(10 != 10) #False
print(2 < 5) #True
print(12 > 5) #True
print(5 <= 6) #True
print(1 >= 10) #False

#---Assignment Operators ---
x = 5
x += 5 #x is now 10
x -= 4 #x is now 6
x *= 3 #x is now 18

#--- Logical Operators ---
#1. Checks if both operands are True. 
# (1 and 2) returns True because 1 and 2 are both True
# (1 and 0) return False because 0 is False
#2. Or checks if one of the operands are True. 
# (1 or 0) returns True because 1 is True
# (0 or 0) return False because both are False
# Not returns False if operand is True. 
# not(0) returns True. 
# not(1) returns False. 

#--- More questions ---
#1. / creates a float. // creates a int without the remainder
#2. % returns the remainder
#3. I would use / or //. 15/2 is 7.5 and 15//2 is 7. 
#4. Use the equal sign, and you can modify it. 

#--- Strings ---
my_string = "hello"
print(my_string) #prints hello
print(my_string[0]) #prints h
print(my_string[1]) #prints e
print(my_string[2]) #prints l
print(my_string[3]) #prints l
print(my_string[-1]) #prints 0
print(my_string[1:3]) #prints el
print(my_string[0:5:2]) #prints hlo
print(len(my_string)) #prints 5
print(my_string + "goodbye") #prints hellogoodbye
print(7*my_string) #prints hellohellohellohellohello

#--- questions ---
#1. when you take a portion of a String. [1:3] and [0:5:2]
#2. Hello, my name is Oski
#3. Hello, my name is Oski
#4. in f strings, python evaluates whatever is in the {}

#--- Terminal Commands ---
#cd: changes the current working directory. cd Documents
#ls: Lists the files and folders in current directory
#ls - a: lists all files, including the hidden ones
#mkdir: makes a new directory (folder)
#cat: concatnates and dispays the content of a file in the terminal
#pwd: prints the working directory
#cd ..: moves you up one level to the parent directory
# cd .: refers to the current directory
#cp: copies a file or directory from one place to another
#mv: moves or renames a file or directory
#rm: removes/deletes a file (no trash bin!)
#clear: clears the terminal screen of all previous text
# grep: searches for a specific pattern of text within a file

#--- questions ---
#1. man, head, tail
#2. ls -a also lists the hidden files
#3. hidden files have a . in front
