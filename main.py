#import random module
import random
from replit import clear
#import data
from game_data import data

#import logo and vs
from art import vs
from art import logo

#global variable to keep track of user good answer
COUNT = 0


#funtion to choose random person in the data
def random_personnality():
    """
    Choose a random personnality in the data file and return it 
    """
    return random.choice(data)


def resume_personnality(personnality):
    """
    Function take a list as parameter, get value of this list and return a short sentence to present personnality
    """
    name = personnality.get('name')
    description = personnality.get('description')
    country = personnality.get('country')
    return f"{name}, a {description}, from {country}"


def followers(personnality):
    """
    Function take a list as parameter, get value of this list and number of follower of the personnality
    """
    return personnality.get('follower_count')


#function to compare
def compare(nb_follow_a, nb_follow_b, user_choice):
    """
    function take number of followers and user choice as parameters, 
    if compare nb follow and user guess to check if user make the right guess
    """
    if nb_follow_a > nb_follow_b and user_choice == "a":
        return True
    elif nb_follow_a < nb_follow_b and user_choice == "b":
        return True
    else:
        return False


person_a = random_personnality()
person_b = random_personnality()

guess_wrong = False
#while loop to continue to play the game after a good guess and stop it after a bad one
while not guess_wrong:

    #print logo
    print(logo)

    #get the resume of celebrity and print it
    resume = resume_personnality(person_a)
    print(f"Compare A: {resume}")
    #print the Versus art
    print(vs)
    resume = resume_personnality(person_b)
    print(f"Against B: {resume}")

    #stock random personnality number of followers in variable
    followers_a = followers(person_a)
    followers_b = followers(person_b)

    print(followers_a)
    print(followers_b)

    #ask user which one of the celeb he thinks got more followers
    user_guess = input("Who has more followers ? Type 'A' or 'B': ").lower()

    #if user guess it right add 1 poitn to count and continue to play, else end game
    if compare(followers_a, followers_b, user_guess) == True:
        COUNT += 1
        print(f"You guess it right, you continue, actual score {COUNT}")
        #celeb b become a and select random celelb for b
        person_a = person_b
        person_b = random_personnality()
    else:
        clear()
        print(f"You guess wrong, sorry you loose, actual score: {COUNT}")
        guess_wrong = True
