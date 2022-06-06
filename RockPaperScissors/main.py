from pickle import TRUE
import random


while True:
    possible_actions = ["R", "P", "S"]
    cpu_action = random.choice(possible_actions)
    user_input = input("Enter a choice \n(R  for Rock) \n(P for paper) \n(S for scissors): ")
    player_action=user_input.upper()

 
    def getfullactionname(s):
        if s=="R":
            return "Rock"
        elif s=="P":
            return "Paper"
        elif s=="S":
            return "Scissors"

    if (player_action in possible_actions):
        print(f"\nPlayer({getfullactionname(player_action)}): CPU({getfullactionname(cpu_action)})")

        if player_action == cpu_action:
            print(f"Both CPU and Player selected {getfullactionname(player_action)}. It's a tie, you have to play again!")
            play_again="y"
        elif player_action == "R":
            if cpu_action == "S":
                print("Rock smashes scissors! Player wins!")
            else:
                print("Paper covers rock! CPU wins.")
            play_again="n"
        elif player_action == "P":
            if cpu_action == "R":
                print("Paper covers rock! Player wins!")
            else:
                print("Scissors cuts paper! CPU wins.")
            play_again="n"
        elif player_action == "S":
            if cpu_action == "P":
                print("Scissors cuts paper! Player wins!")
            else:
                print("Rock smashes scissors! CPU wins.")
            play_again="n"

    elif(player_action not in possible_actions):
        print("Invalid choice! You have to play again")
        play_again="y"
    
    if play_again.lower() != "y":
     break