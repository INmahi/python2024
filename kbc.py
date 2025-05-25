from rich import print

# EXCERCISE: KBC

# takes input from user the number of question
# Total Amount is 7 Crore
# Creates an exponential distribution of the prize money according to the number of question 


shuffled_questions = ["[bold]What is the capital of France?[/bold]\nA. Paris\nB. Rome\nC. London\nD. Berlin\n","[bold]What is the largest planet in our solar system?[/bold]\nA. Earth\nB. Mars\nC. Jupiter\nD. Venus\n","[bold]Who painted the Mona Lisa?[/bold]\nA. Michelangelo\nB. Leonardo da Vinci\nC. Vincent van Gogh\nD. Pablo Picasso\n","[bold]What is the boiling point of water in Celsius?[/bold]\nA. 80\nB. 120\nC. 90\nD. 100\n","[bold]Which animal is known as the King of the Jungle?[/bold]\nA. Tiger\nB. Lion\nC. Bear\nD. Elephant\n","[bold]What is the chemical symbol for Oxygen?[/bold]\nA. Ox\nB. O\nC. Og\nD. Oy\n","[bold]Who wrote the play 'Romeo and Juliet'?[/bold]\nA. Jane Austen\nB. Charles Dickens\nC. Mark Twain\nD. William Shakespeare\n","[bold]What is the smallest prime number?[/bold]\nA. 5\nB. 3\nC. 2\nD. 1\n","[bold]Which country is known as the Land of the Rising Sun?[/bold]\nA. South Korea\nB. China\nC. Japan\nD. Thailand\n","[bold]What is the hardest natural substance on Earth?[/bold]\nA. Gold\nB. Iron\nC. Diamond\nD. Silver\n","[bold]Who developed the theory of relativity?[/bold]\nA. Galileo Galilei\nB. Albert Einstein\nC. Isaac Newton\nD. Nikola Tesla\n","[bold]What is the longest river in the world?[/bold]\nA. Nile\nB. Mississippi\nC. Yangtze\nD. Amazon\n","[bold]Which element has the atomic number 79?[/bold]\nA. Silver\nB. Platinum\nC. Copper\nD. Gold\n","[bold]Who was the first person to reach the South Pole?[/bold]\nA. Roald Amundsen\nB. Robert Scott\nC. Ernest Shackleton\nD. Edmund Hillary\n"]

new_answer_letters = ["A", "C", "B", "D", "B", "B", "D","C", "C", "C", "B", "A", "D", "A"]
print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~ WELCOME TO KBC ~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Total Questions: 14 \nPrize: 7 Crore\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Type 'START' to Continue:")

init = input()

basePrize = 5000

def askNext(q=0):
    print(f"[bold]({q+1}) {shuffled_questions[q]}[/bold]")
    userAns = input("Type Your Answer \n or Type 0 to QUIT now: ")
    if userAns == "0":
        quitGame(q)
    else:
        startKBC(userAns,q)

def startKBC(userAns=None,S=0):
    choosen = userAns
    if S<=13:
        if userAns==None:
            askNext(S)
        elif(choosen == new_answer_letters[S]):
            announcePrize(S)
            S+=1
            if S>13:
                finishGame()
            if S<=13:
                askNext(S)
        else:
            gameOver(S)
    else:
        finishGame()
    
def getPrize(state):
    if state<0:
        prize=0
    elif state==12:
        prize = "5 CRORE"
    elif state==13:
        prize = "7 CRORE"
    else:
        prize = basePrize*pow(2,state)
    return prize


def announcePrize(state):
    print(f"[green]CORRECT ANSWER! You have now won ~~~~ [bold]{getPrize(state)}$[/bold] ~~~~[green]\n")
def gameOver(state):
    print(f"[red]!!!!!!!!SORRY WRONG ANSWER!!!!!! [/red]\nYou have now won total~~~~ {getPrize(state-1)}$ ~~~~\n")
def quitGame(state):
    print(f"You Have Quit The Game. You won [bold green]{getPrize(state-1)}$[/bold green]")
def finishGame():
    print("[bold blue]CONGRATULATIONS, YOU HAVE MADE HISTORY[/bold blue]")
    
if init=="START":
    print("Type Down The Correct Option Letter (A,B,C or D):\n")
    startKBC()