############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
from replit import clear
import random
from art import logo
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
start_game = True
while start_game:
    start = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if start == "y":
        clear()
        print(logo)

        #Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
        #11 is the Ace.

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        def deal_card():
            random_card = random.choice(cards)
            return random_card

        #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
        #user_cards = []
        #computer_cards = []

        user = []
        computer = []
        for a in range(2):
            user.append(deal_card())
            computer.append(deal_card())

        #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
        #and returns the score. 
        #Look up the sum() function to help you do this.
        def calculate_score(list_cards):
            x = sum(list_cards)
            
            if 11 in list_cards and 10 in list_cards and len(list_cards) == 2:
                return 0

            #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
            if 11 in list_cards and x > 21:
                list_cards.remove(11)
                list_cards.append(1)

            return x

        #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
        
        def compared(user_score, computer_score):
            if user_score == computer_score:
                return "It's a Draw!"
            elif user_score == 0:
                return "You Win!"
            elif computer_score == 0:
                return "You Lose"
            elif user_score > 21:
                return "You Lose"
            elif computer_score > 21:
                return "You Win!"
            elif user_score > computer_score:
                return "You Win!"
            else:
                return "You Lose :("

        #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
        game_must_continue = False
        while not game_must_continue:
            #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
            user_score = calculate_score(user)
            computer_score = calculate_score(computer)
            print(f"   Your cards are: {user} and your score is: {user_score}")
            print(f"   Computer first cards is: {computer[0]}")

            if computer_score == 0 or user_score == 0 or user_score > 21:
                game_must_continue = True
            else:
            #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended                
                ask = input("Type 'y' to geth another card, type 'n' to pass: ")
                if ask == "y":
                    user.append(deal_card())
                else:
                    game_must_continue = True

        #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
        while computer_score !=0 and computer_score < 17:
            computer.append(deal_card())
            new_computer_score = calculate_score(computer)

        print(f"   Your final hand: {user}, final score: {user_score}")
        print(f"   Computer's final hand: {computer}, final score: {computer_score}")

        print(compared(user_score,computer_score))
    else:
        start_game = False
