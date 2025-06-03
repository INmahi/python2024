from rich import print
from rich.align import Align
from rich.panel import Panel
import random

# Game introduction panel
print(Align.center(Panel("[bold blue]🎮 LET'S START THE GAME 🎮[/bold blue]")))

# Game symbols
game_law = {0: "🐍", 1: "🌊", 2: "🔫"}
options = "0 ➡ 🐍 Snake\n1 ➡ 🌊 Water\n2 ➡ 🔫 Gun"

# Determine winner
def is_player_winner(p, c):
    return (
        (p == 0 and c == 1) or  # Snake drinks water
        (p == 1 and c == 2) or  # Water douses gun
        (p == 2 and c == 0)     # Gun shoots snake
    )

# Final result announcement
def announce_prize(score):
    print("\n[bold cyan]-----------------------------[/bold cyan]")
    if score >= 2:
        print("[bold green]🏆 Congratulations! You won the game! 🏆[/bold green]")
    else:
        print("[bold red]💔 You lost the game! Better luck next time! 💔[/bold red]")
    print(f"[bold yellow]Final Score: {score}/3[/bold yellow]")
    print("[bold cyan]-----------------------------[/bold cyan]\n")

# Game logic
def start_game():
    score = 0
    for i in range(3):
        print(f"\n[bold]Round {i+1} — Choose your weapon:[/bold]")
        print(options)
        
        try:
            player_choice = int(input("Your Choice: "))
            if player_choice not in [0, 1, 2]:
                raise ValueError
        except ValueError:
            print("[red]Invalid input! Please enter 0, 1, or 2.[/red]")
            continue

        computer_choice = random.randint(0, 2)
        print(f"You: {game_law[player_choice]} | 🤖: {game_law[computer_choice]}")

        if player_choice == computer_choice:
            print(f"[yellow]🤝 Round {i+1} is a draw. Score {score}/3[/yellow]")
        elif is_player_winner(player_choice, computer_choice):
            score += 1
            print(f"[green]😃 You won round {i+1}! Score {score}/3[/green]")
        else:
            print(f"[red]😥 You lost round {i+1}. Score {score}/3[/red]")

    announce_prize(score)

# Game loop
def init():
    while True:
        inp = input("Enter 1 to start or 0 to quit:")
        if inp == '1':
            start_game()
        elif inp == '0':
            print("[bold magenta]👋 Thanks for playing! Goodbye![/bold magenta]")
            break
        else:
            print("[red]❌ Invalid input. Please enter 1 or 0.[/red]")

init()
