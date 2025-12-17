from rich import print
import string
import random
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
# print(getAvg(1,2,3,4,5,6))


# EXCERCISE: KBC

# takes input from user the number of question
# Total Amount is 7 Crore
# Creates an exponential distribution of the prize money according to the number of question 


# shuffled_questions = ["[bold]What is the capital of France?[/bold]\nA. Paris\nB. Rome\nC. London\nD. Berlin\n","[bold]What is the largest planet in our solar system?[/bold]\nA. Earth\nB. Mars\nC. Jupiter\nD. Venus\n","[bold]Who painted the Mona Lisa?[/bold]\nA. Michelangelo\nB. Leonardo da Vinci\nC. Vincent van Gogh\nD. Pablo Picasso\n","[bold]What is the boiling point of water in Celsius?[/bold]\nA. 80\nB. 120\nC. 90\nD. 100\n","[bold]Which animal is known as the King of the Jungle?[/bold]\nA. Tiger\nB. Lion\nC. Bear\nD. Elephant\n","[bold]What is the chemical symbol for Oxygen?[/bold]\nA. Ox\nB. O\nC. Og\nD. Oy\n","[bold]Who wrote the play 'Romeo and Juliet'?[/bold]\nA. Jane Austen\nB. Charles Dickens\nC. Mark Twain\nD. William Shakespeare\n","[bold]What is the smallest prime number?[/bold]\nA. 5\nB. 3\nC. 2\nD. 1\n","[bold]Which country is known as the Land of the Rising Sun?[/bold]\nA. South Korea\nB. China\nC. Japan\nD. Thailand\n","[bold]What is the hardest natural substance on Earth?[/bold]\nA. Gold\nB. Iron\nC. Diamond\nD. Silver\n","[bold]Who developed the theory of relativity?[/bold]\nA. Galileo Galilei\nB. Albert Einstein\nC. Isaac Newton\nD. Nikola Tesla\n","[bold]What is the longest river in the world?[/bold]\nA. Nile\nB. Mississippi\nC. Yangtze\nD. Amazon\n","[bold]Which element has the atomic number 79?[/bold]\nA. Silver\nB. Platinum\nC. Copper\nD. Gold\n","[bold]Who was the first person to reach the South Pole?[/bold]\nA. Roald Amundsen\nB. Robert Scott\nC. Ernest Shackleton\nD. Edmund Hillary\n"]

# new_answer_letters = ["A", "C", "B", "D", "B", "B", "D","C", "C", "C", "B", "A", "D", "A"]

# print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~ WELCOME TO KBC ~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("Total Questions: 14 \nPrize: 7 Crore\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("Type 'START' to Continue:")

# # init = input()

# basePrize = 5000

# def askNext(q=0):
#     print(f"[bold]({q+1}) {shuffled_questions[q]}[/bold]")
#     userAns = input("Type Your Answer \n or Type 0 to QUIT now: ")
#     if userAns == "0":
#         quitGame(q)
#     else:
#         startKBC(userAns,q)

# def startKBC(userAns=None,S=0):
#     choosen = userAns
#     if S<=13:
#         if userAns==None:
#             askNext(S)
#         elif(choosen == new_answer_letters[S]):
#             announcePrize(S)
#             S+=1
#             if S>13:
#                 finishGame()
#             if S<=13:
#                 askNext(S)
#         else:
#             gameOver(S)
#     else:
#         finishGame()
    
# def getPrize(state):
#     if state<0:
#         prize=0
#     elif state==12:
#         prize = "5 CRORE"
#     elif state==13:
#         prize = "7 CRORE"
#     else:
#         prize = basePrize*pow(2,state)
#     return prize


# def announcePrize(state):
#     print(f"[green]CORRECT ANSWER! You have now won ~~~~ [bold]{getPrize(state)}$[/bold] ~~~~[green]\n")
# def gameOver(state):
#     print(f"[red]!!!!!!!!SORRY WRONG ANSWER!!!!!! [/red]\nYou have now won total~~~~ {getPrize(state-1)}$ ~~~~\n")
# def quitGame(state):
#     print(f"You Have Quit The Game. You won [bold green]{getPrize(state-1)}$[/bold green]")
# def finishGame():
    print("[bold blue]CONGRATULATIONS, YOU HAVE MADE HISTORY[/bold blue]")
    
# if init=="START":
    print("Type Down The Correct Option Letter (A,B,C or D):\n")
    startKBC()

#the fibonacci sequence

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# num = int(input("Enter a number: "))
# for i in range(num):
#     print(fibonacci(i), end=" ")

#all exceptions
# import builtins
# exceptions = [e for e in dir(builtins) if isinstance(getattr(builtins, e), type) and issubclass(getattr(builtins, e), BaseException)]
# print(exceptions)


#===========encoding-decoding============


import random
import string

# Constants for obfuscation length
ENCODE_PREFIX_LEN = 3
ENCODE_SUFFIX_LEN = 2
MIN_ENCODE_LEN = ENCODE_PREFIX_LEN + ENCODE_SUFFIX_LEN + 1


def obfuscate(word: str) -> str:
    """Obfuscate a word by rearranging and adding random characters."""
    prefix = ''.join(random.choices(string.ascii_letters, k=ENCODE_PREFIX_LEN))
    suffix = ''.join(random.choices(string.ascii_letters, k=ENCODE_SUFFIX_LEN))
    return prefix + word[1:] + word[0] + suffix


def deobfuscate(word: str) -> str:
    """Decode an obfuscated word back to its original form."""
    trimmed = word[ENCODE_PREFIX_LEN:-ENCODE_SUFFIX_LEN]
    return trimmed[-1] + trimmed[:-1]


def encode() -> None:
    """Encode a full message input by the user."""
    plain_text = input("Enter your message here: ")
    words = plain_text.split()
    encoded_words = []

    for word in words:
        if len(word) < 3:
            encoded_words.append(word[::-1])
        else:
            encoded_words.append(obfuscate(word))

    encoded_words.reverse()
    encoded_msg = ' '.join(encoded_words)
    print("[green]Here is your encoded version: [/green]" + encoded_msg)


def decode() -> None:
    """Decode an encoded message back to its original text."""
    try:
        encoded_text = input("Enter the message you want to decode: ")
        words = encoded_text.split()
        decoded_words = []

        for word in words:
            if len(word) < 3:
                decoded_words.append(word[::-1])
            else:
                decoded_words.append(deobfuscate(word))

        decoded_words.reverse()
        decoded_msg = ' '.join(decoded_words)
        print("[blue]Here is your decoded version: [/blue]" + decoded_msg)
    
    except Exception:
        print("[bold red] Please add a properly enoded message here[/bold red]")

# def main() -> None:
#     """Main loop to interact with the user."""
#     while True:
#         print("\n0 -> Encode\n1 -> Decode\nx -> Quit")
#         action = input("Enter code here: ").strip().lower()

#         if action == "0":
#             encode()
#         elif action == "1":
#             decode()
#         elif action == "x":
#             break
#         else:
#             print("[bold red]INVALID CODE[/bold red]")


# if __name__ == "__main__":
#     main()

ab = 2
bc = 3

# print("ab") if ab>bc else print("=") if ab == bc else print("bc")

integers_list = [10, 25, 7, 42, 3, 18]

# # i = 0
# for index, intiger in enumerate(integers_list):
#     print(index,intiger)
#     # i+=1


# inp = ' '.join(input("name: ").strip().split())

# print(inp)

# h,w = input("Enter size: ").split(",")

# for _ in range(int(h)):

#     for _ in range(int(w)):
#         print("-",end='')

#     print("")    

### imp

#def main():
#
#    user_expression = input("Expression: ").strip()
#
#    x,y,z = user_expression.split(" ")
#    x,z = int(x),int(z)

#    result = 0

#    ops = {
#        "+": lambda x,z: x+z,
#        "-": lambda x,z: x-z,
#        "*": lambda x,z: x*z,
#        "/": lambda x,z: x/z if z!=0 else "Cannot Devide by 0"
#    }

#    result = ops.get(y,lambda x,z:"Unsupported operator")(x,z)
#    #look for key:y in ops, if not found priont "unsupported..". if found, it finds a function and we call it with x and z

#    print(result)

#main()


# print(bool("sep" in "sep tem ber"))


