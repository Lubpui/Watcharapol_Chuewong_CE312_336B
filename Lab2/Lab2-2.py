# - Create 1D integer array => 7,5,10,14,3,9,7 and 9,10,3,4,2,5,7,1
array1 = [7,5,10,14,3,9,7]
array2 = [9,10,3,4,2,5,7,1]

# - Find length and print both arrays
print("Length of 1st array is : ",len(array1))
print("Length of 2st array is : ",len(array2))

# - Insert 15 in 1stArray
array1.insert(7,15)
print("insert 15 in 1st array = ",array1)

# - Find index of 7 in 2 arrays
print("index of 7 is : ",array2.index(7))
print("index of 7 is : ",array1.index(7))

# - Append 1 in first array and 14 in second array
array1.append(1)
array2.append(14)
print("1st array = ",array1,"\n2st array = ",array2)

# - Copy 1stArray to create new array (3rdArray)
array3 = array1.copy()
print("3rd array = ",array3)

# - Merge new array and 2ndArray together (3rdArray and 2ndArray)
array3.extend(array2)
print("2st and 3rd Array = ",array3)

# - Count value of 7 in 3rdArray
print("There are 7 in the 3rd array : ",array3.count(7))

# - Sort 3rdArray
array3.sort()
print("3rd array but arranged => ",array3)

# - Remove 7 in 3rdArray
array3.remove(7)
print("Remove 7 in 3rd array => ",array3)

# - Copy 3rdArray to 4thArray
array4 = array3.copy()
print("4th array is : ",array4)

# - Reverse 4thArray
array4.reverse()
print("Reverse 4th array : ",array4)

# - Print 3rd and 4th Array
print("Reverse 3rd array : ",array3)
print("Reverse 4th array : ",array4)
