import random

def get_choices(): #defining the function get_choices
    player_choice = input("Enter a choice (rock, paper, scissors): ") #taking input of the player choices
    options = ["rock", "paper", "scissors"] #creating a list for options
    computer_choice = random.choice(options) #using ramdom module to select option
    choices = {"player": player_choice, "computer": computer_choice} #using dictionaries
    return choices

def check_win(player, computer): #defining the function check_win eith arguments 
    print(f"You chose {player}, computer chose {computer}") #fstring is used in this statement which allows you to embed expressions directly inside the string using curly braces {}
    if player == computer: #if cond
        return "It's a tie!"
    
    elif player == "rock": #nested if
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
            
    elif player == "paper": #nested if
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
            
    elif player == "scissors": #nested if
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices() #calling func get_choices() using variable choices
result = check_win(choices["player"], choices["computer"]) #calling func check_win() using variable result
print(result)
