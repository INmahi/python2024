from functools import reduce
#filter even numbers

# ls = [1,4,2,4,5,6,7,2,5,8,9,60,59,47,25,12]

# # def checker(x):
# #     return x%2==0
# newls = filter(lambda x: x%2==0 ,ls)
# print(list(newls))



#Square all elems

# ls = [1,4,2,4,5,6,7,2,5,8,9,60,59,47,25,12]
# def condition_sq(x):
#     if x%2==0:
#         return x*x
# print(list(map(condition_sq,ls)))

# ls = [1,4,2,4,5,6,7,2,5,8,9,60,59,47,25,12]

# print(list(map(lambda x: x*x,ls)))




# #CONVERT A LIST OF LOWERCASE STRINGS TO UPPERCASE

# ls = ["hello","Hi","low","Tets"]

# print(list(map(lambda x: x.upper(),ls)))



#SUM ALL USING REDUCE

# ls = [1,4,2,4,5,6,7,2,5,8,9,60,59,47,25,12]

# result = reduce(lambda x,y: x+y,ls)

# print(result)


#FILTER ALL NON EMPTY STRINGS

ls = ["apple", "", "banana", " ", "cherry", "", "date", "fig", ""]

print(list(filter(lambda x: x.strip(),ls)))

