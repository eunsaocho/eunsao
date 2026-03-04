#3.1: Say Goodbye
def say_goodbye(name):
    print("Goodbye", name)

#area of a circle
def circleArea(radius):
    area = 3.14* (radius ** 2)
    print(area)

#4.1: Subtract, multiply divide
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a/b

#5.1 what should i wear
def wear(readings):
    highest = max(readings)
    lowest = min(readings)
    val = (lowest, highest)
    return val

#5.2 check it it's the weekend
def weekend(num):
    if (num >= 1 and num <= 5):
        return False
    return True

#5.3 fuel efficiency
def fuel(distance, fuelUsed):
    fuelEfficiency = distance/fuelUsed
    return fuelEfficiency

#5.4: secret code
def code(num):
    oldLast = num%10 #5
    rest = num//10 #1234

    digits = 0
    temp = rest
    while(temp):
        temp = temp//10
        digits += 1
    return oldLast*(10 ** digits) + rest

#6.1 Oski stole your power
def newPow(x, y):
    #x^y (x * x * ...)
    returnVal = 1 #y = 1
    while (y > 0):
        returnVal = returnVal * x
        y-=1
    return returnVal

#6.2.1: min and max with for loops
def forMin(list):
    currMin = list[0]
    for x in list:
        if x < currMin:
            currMin = x
    return currMin
def forMax(list):
    currMax = list[0]
    for x in list:
        if x>currMax:
            currMax = x
    return currMax

#6.2.2 while loop
def whileMin(list):
    currMin = list[0]
    currIndex = 0
    while currIndex < len(list):
        if list[currIndex] < currMin:
            currMin = list[currIndex]
        currIndex+=1
    return currMin
def whileMax(list):
    currMax = list[0]
    currIndex = 0
    while currIndex > len(list):
        if list[currIndex] < currMax:
            currMax = list[currIndex]
        currIndex+=1
    return currMax

#6.3 calculate the sun
def sun(num):
    sum = 0
    while (num > 0):
        sum += num % 10
        num = num//10
    return sum

#7.1 Running the code
x = 1234
result = sun(1234) #expected = 10
print(f"The result of sun (6.3) with num = {x} is {result}")

#example from homework
x = 2
y = 3
result = newPow(2, 3)
print(f"The result of Oski Stole Your power (5.1) with x = {x} and y = {y} is {result}")