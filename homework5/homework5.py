#3.1 vocab review
#Git vs GitHub:
#	Git=version control tool on computer
#	GitHub = website/service for hosting Git repositories online
#Terminal vs CommandLine
#	Terminal=the window where you type commands
#	Command line: text-based way of interacting with the computer
#local vs remote repository
#	Local: Git repo on your own computer
#	remote: git re[o stored online (like GitHub)
#Version control: a system for tracking file changes over time
#Staging area: a holding area where you choose changes before commiitting
#git add: puts file changes into stanging area
#git commit: saves a snapshot of staged changes with a message
#git push: uploads local commits to the remote repository
#git status: shows which files changed and what Git is tracking
#git pull: downloads and merges changes from the remote repo
#pwd: prints your current folder path
#ls: lists files and folders in the current firectory
#cd: changes to another directory
#nano: changes to another directory
#touch: creates a new empty files
#mv: moves or renames a file/folder
#rm: removes a file or folder
#cat: displays the contents of a file

#3.2: directory tree
#pwd
#ls
#cd ../brianna_repo ->(next line) git pull
#mv homework.py ../judy_decal/homework/
#cd ../judy_decal
#cat homework/homework.py
#git add homework/homework.py -> git commit -m "done w hw yay"
#	->git push
#git pull -> git push
#	this means remote repo has changes that Judy doesn't have locally
#~/Recent/

#4.1 data types
def checkDataType(x):
    return str(type(x).__name__)

#4.2 conditionals
def evenOrOdd(n):
    if n%2 == 0:
        return "Even"
    return "Odd"

#5 loops
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#6.1 lists
def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

#6.2 debugging
def square(num):
    return num*num

print("using #5 to sum the list [2, 4, 6]:")
sumList = [2, 4, 6]
print(sumWithLoop(sumList))
