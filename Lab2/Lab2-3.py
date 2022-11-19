# - Number ID,Name,Count
arraySTR = ["Number ID","Name","Count"]                                                  # <| Declare an array variable
print(arraySTR)

# - Find length of array
print("length of array is : ",len(arraySTR))                                               # <| len(array) = fine the number of variables in array

# - Find location of Name in array
print("location of Name in array is : ",arraySTR.index("Name"))             # <| Find index of Name in arrays

# - Add value "Status" in the last index of array
arraySTR.append("Status")                                                                          # add Status to the last position in the array
print(arraySTR)

