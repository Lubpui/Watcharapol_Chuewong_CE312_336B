array = [["Number ID","Name","Count","Status"],[]]                                   # <| Declare an array variable

print(len(array))                                                                                           # <|  len(array) = fine the number of variables in array

array.insert(1,[1,"Rubber",0,"Out of stock"])                                              # <|
array.insert(2,[2,"Ruler",5,"In stock"])                                                        # <| Insert list goes to index[1,2,3]
array.insert(3,[3,"Pencil",1,"In stock"])                                                       # <|

print(array)
