#myList = [1, "hello", [1, 2, 3], "true"]
#print("List: " , myList)

#index print
#print(myList[2])

#concatenate
#myList.append(" add 'Jayed'")
#print(myList)
myList = [1, "hello", 5, "true"]

#convert list to set
mySet = set(myList)
mySet2 = {1, 2, 3, "hello"}
print(mySet)
print(type(mySet))

#union of set
print("First: ", mySet)
print("Second: ", mySet2)
print("Union: ", mySet.union(mySet2))

#check superset and subset
print("Superset check: ", mySet2.issuperset(mySet))
print("Subset check: ", mySet2.issubset(mySet))

#intersection of set
print(mySet.intersection(mySet2))

#difference of two set
print(mySet.difference(mySet2))

#add set
print(mySet2)
mySet2.add("Jayed")
print(mySet2)