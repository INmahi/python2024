#list => ordered - Changable - Duplicates
#tuple => ordered - unchangable - Duplicates
#dict => unordered - changable - no duplicates
#set => unordered - unchangable - no duplicates


#=========sorting==============#
    #case sensetive, Uppercase priority, number as string priority

#make a list of integers and sort them according to how far they are from the number 128
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


# i = 8
# while i <= 6:
#     i += 1
#     if i == 3:
#         break
#     else:
#         print(i)
   
# else:
#     print("I am out of the loop")


# newlist =[34,34,9,45,2345,98,123]

# def farFrom45(num):
#     value=45-num
#     return(abs(value))

# newlist.sort(reverse=True,key=farFrom45)
# print(newlist)


# i = 0
# while i<10:
#     i+=1
#     if i==5:
#         continue
#     print(i)
    
# got_characters = [
#         "Jon Snow",
#         "Daenerys Targaryen",
#         "Tyrion Lannister",
#         "Arya Stark",
#         "Sansa Stark",
#         "Cersei Lannister",
#         "Jaime Lannister",
#         "Bran Stark",
#         "Brienne of Tarth",
#         "Theon Greyjoy",
#         "Samwell Tarly",
#         "Jorah Mormont",
#         "Petyr Baelish",
#         "Varys",
#         "Sandor Clegane"
#     ]
# for x in got_characters:
#     if x == "Varys":
#         print("Got the eunuch!!")
#     else:
#         print(f"its not {x}")


# i = 1
# while i<=7:
#     j=1
#     numOfSpaces = (7-i)/2
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print("")
#     i+=2


# i = 1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

#function

# def myFunc(*kids):
#     print(type(kids))
#     print(kids[-1])

# myFunc("ishat","Noor","mahi")

# def intro(**kwargs):
#     for x,y in kwargs.items():
#         print(f"{x} ~ {y} ")

# intro(Name="Mahi",Age=13,height="6 ft")

# def controlledFunc(a,b,/,*,c,d):
#     pass

# # Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
#def getSum(k):
#     sum = 0
#     i = 0
#     while i<=k:
#         sum=sum+i
#         i+=1
#     # print(sum)    
#     return sum

# print(getSum(3)+3)
#RECURSION

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#     print(result)
#   return result

# print("Recursion Example Results:")
# tri_recursion(4)
 

#AVG

def getAvg(*var):
    sum = 0
    for x in var:
        sum = sum+x
    avg = sum/len(var)
    print(f"Number Of individuals: {len(var)} \nSummation: {sum} \nAVERAGE: {avg}")
    return avg
print(getAvg(1,2,3,4,5,6))
