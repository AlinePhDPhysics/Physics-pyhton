list1 = ["M", "no", "é", "Ali"] 
list2 = ["eu", "me", "é", "ne"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)