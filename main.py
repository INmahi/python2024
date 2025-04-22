#list => ordered - Changable - Duplicates
#tuple => ordered - unchangable - Duplicates
#dict => unordered - changable - no duplicates
#set => unordered - unchangable - no duplicates


#=========sorting==============#
    #case sensetive, Uppercase priority, number as string priority

#make a list of integers and sort them according to how far they are from the number 50
# def myFunc(n):
#     # value = n-128
#     # print(f"({n},{value})")
#     return abs(n)

# numbers = [39,28,50,128,438,1,780,343,50,57]
# numbers.sort(key=myFunc)
# print(numbers)


# copy list with copy()
    #safest. makes independent copy
# list1 = ["apple","banana","mango","kiwi",[1,2,3]]
# list2 = list1.copy()

# list2.append("New")

# print("List 1 ",list1) #doesn't change
# print("List 2 ",list2)

# ========tuple============#

# tuple1 = ("Hello", "hi", "Bye", "tata")
# tuple2 = (1,2,3)
# tuple3 = tuple1+tuple2
# print(tuple3)

# (one,two,three)=tuple2

# #print one two and three separately
# print(one)
# print(two)
# print(three)

#============Sets===============
# set1={"a","b","c"}
# set2={"e","f","g"}
# # set1.add("d")
# set1.update(set2)
# print(set2)

#==========dictionary===========

# dict1 = {
#     "Name" : "mahi",
#     "Age" : 19,
#     "Status" : "Failed"
# }

# for x in dict1:
#     print(f"{x} : {dict1[x]}")

# ls1 = ("hello", "mahi")

# print(ls1[0])


# parents = {
#     "Mother" : {
#         "Name" : "Marufa",
#         "Age" : 55
#     },
#     "Father" : {
#         "Name" : "Obaidul",
#         "Age" : 60
#     }
# }

# # print(parents["Mother"]["Age"])

# children = {
#     "child1" : {
#         "Name" : "Tasfia",
#         "Age" : 20
#     },
#     "child2" : {
#         "Name" : "Mahi",
#         "Age" : 19
#     },
#     "child3" : {
#         "Name" : "X",
#         "Age" : 14
#     }
# }

# myFamily = {
#     "Parents" : parents,
#     "children" : children
# }

# # print(myFamily["children"]["child2"]["Name"])


# day = 7
# match day:
#     case 1|2|3|4|5:
#         print("Weekday")
#     case 6|7:
#         print("YEY!! WEEKEND")
#     case _:
#         print("Invalid Day")    


i = 8
while i <= 6:
    i += 1
    if i == 3:
        break
    else:
        print(i)
   
else:
    print("I am out of the loop")