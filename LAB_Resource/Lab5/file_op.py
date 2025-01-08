
# example = 'C:\mj\lab_6\Example1.txt'
#with open(example, "r") as file1:
    #print(file1.read())
    
# with open(example, "r") as file1:
    # i = 0
    # for line in file1:
    #     print("Iteration", str(i), ": ", line)
    #     i = i + 1

# with open(example, "r") as file1:
#     fileName = file1.readlines()
#     for ind, val in enumerate(fileName):
#         print(fileName[ind])
        
# example2 =  'C:\mj\lab_6\Example2.txt'
# with open(example2, "w") as writeFile:
#     writeFile.write("This line created by my programm\nSo, we are happy")
    
# with open(example2, "r") as testWrite:
#     print(testWrite.read())

Lines = ['This is lineA\n' 'This is lineB\n' 'This is lineC']
example3 =  'C:\mj\lab_6\Example3.txt'
with open(example3, "w") as myWrite:
    for line in Lines:
        print(line)
        myWrite.write(line)
    
    
