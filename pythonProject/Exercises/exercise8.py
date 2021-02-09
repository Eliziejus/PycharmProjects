first_player_choice = input("Choose Rock-Paper-Scissors:  ")
second_player_choice = input("Choose Rock-Paper-Scissors:  ")


def to_compare(ch1,ch2):

    if ch1 == "rock":
        if ch2 == "scissors":
            return("Rock win")
    else:
        return("Paper win")
    if ch1 == "paper":
        if ch2 == "rock":
            return("Paper win")
        else:
            return("Rock win")
    if ch1 == "scissors":
        if ch2 == "paper":
            return("Scissors win")
        else:
            return("Rock win")
    if ch1 == ch2:
        return("draw")
print   (to_compare(first_player_choice,second_player_choice))



