#3.1
foods = ["asian pear", "broccoli", "chicken", "french fries", "grapes"]
print(foods[-1])
foods.append("pizza")
foods.insert(0, "apple")
foods.remove("broccoli") #apple, asian pear, brocolli
print(len(foods))
for food in foods:
    print(food.upper()) #expected: apple, asian pear, chicken, fries, grapes, pizza
newFoods = foods[:1] + foods[-1:]
print(newFoods)
if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

#3.2
numbers = list(range(0, 21))
print(numbers)
def get_first_15(numbers): #0-14
    return numbers[:15]
def get_every_5th(lst):
    i = 0
    returnList = []
    while i < len(lst):
        returnList.append(lst[i])
        i+=5
    return returnList

def reverse_and_stride(lst):
    i = 0
    helper = []
    returnList = []
    while i < len(lst):
        helper.insert(0, lst[i])
        i += 1
    i=0
    while i < len(lst):
        returnList.append(helper[i])
        i+=3
    return returnList
print(reverse_and_stride(get_every_5th(get_first_15(numbers))))
#putting it all together
step1 = get_first_15(numbers)
print(step1)
step2 = get_every_5th(step1)
print(step2)
step3 = reverse_and_stride(step2)
print(step3)

#3.3 nested list
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])
def sum_nested(lst):
    sum = 0
    for row in numbers:
        for val in row:
            sum += val
    return sum
print(sum_nested(numbers))

#3.4 5x5 list
def five() :
    something = []
    num = 1
    for i in range(5): #1-4
        nested = []
        for j in range(5): #0-4
            #create a list
            nested.append(num)
            num += 1
        something.append(nested)
    return something

def threes(something):
    new_something = []
    for row in something:
        new_row = []
        for item in row:
            if item % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(item)
        new_something.append(new_row)
    return new_something

def sum(something):
    total = 0
    for row in something:
        for item in row:
            if item != "?":
                total += item
    return total

ages = {"Katie": 30, "Mariam": 42, "Safia": 25, "Mira": 48}
#print katie's age:
print(ages["Katie"])
#change mira's age to 100
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for name in ages:
    print(name, ages[name])


example = five()
print(example)
print(threes(example))