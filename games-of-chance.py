# Games of Chance with roulette, coin toss, and cho han.

import random
import time
money = 100


def playGame():
    game = input("Would you like to play a game? ").lower()
    if game == "yes":
        startGame()
    elif game == "no":
        return "Ok, have a nice day!"
    else:
        print("I'm sorry, " + name + ", I didn't quite understand that")
        return playGame()


def endGame():
    print("Thank you for choosing 'Computer' for all of your gambling needs")
    time.sleep(1)
    if money == 0:
        print("And thank you for giving us all your money.")
    else:
        print("Don't forget to cash out your chips with Janice at the 3rd window!")
        time.sleep(1)
        print("You currently have €" + str(money) + " in chips")


def startGame():
    animal = random.randint(1, 10)
    animals = {
        1: "an elephant",
        2: "a giraffe",
        3: "an hippopotamus",
        4: "a lion",
        5: "a kangaroo",
        6: "a velociraptor",
        7: "a sabretoothed tiger",
        8: "Winona Ryder",
        9: "like, 80 cats",
        10: "a ghost"
    }
    print("What would you like to play?")
    time.sleep(1)
    gameType = input("We have a coin to flip, a game called Cho Han, and a roulette table. ").lower()
    print("You're starting with €" + str(money) + " in chips. ")
    time.sleep(1)
    if "coin" in gameType:
        print("Welcome to the coin toss.")
        time.sleep(1)
        coinToss()
    elif "cho" in gameType:
        print("Time to Cho some Hans.")
        time.sleep(1)
        choHanRules()
    elif "roulette" in gameType:
        print("I'm sorry there's " + (animals[animal]) + " on the roulette table.")
        time.sleep(2)
        print("Ha! Just kidding.")
        time.sleep(1)
        print("Welcome to the roulette table. Here, you can place multiple bets")
        time.sleep(1)
        roulette()
    else:
        print("Well that's just nonsense.")
        return startGame()


def coinToss():
    global money
    bet = input("How much would you like to wager? ")
    if int(bet) == 0:
        noBet = input("You didnt bet anything, would you like to play something else? ")
        if noBet == "yes":
            startGame()
        if noBet == "no":
            stop = input("Do you want to go home? ")
            if stop == "yes":
                endGame()
            else:
                coinToss()
    time.sleep(1)
    try:
        val = int(bet)
        print("Alright, betting has closed.")
    except ValueError:
        print("Sorry, I'm not sure what " + bet + " is, we only wager in legal currency here.")
        coinToss()
    if int(bet) > money:
        print("Sorry, you don't have that kind of scratch. Place a lower bet or get out of here")
        return coinToss()
    if int(bet) == money:
        print("Wow, all in? Living on the edge!")

    if money < 20:
        sure = input("Are you sure you want to keep playing? You only have " + str(money) + " left.").lower()
        if sure == "no":
            endGame()
    winningSentences = {
        1: "AMAZING! What are the odds? One of us should know. You just won " + str(bet) + " smackeroos!",
        2: "Well wasn't that something! Are your pockets getting heavy? Because you just won €" + str(bet) + ".",
        3: "Do you feel lucky, punk? Well you should, you just won " + str(bet) + " big ones!",
        4: "You won €" + str(bet) + ", so I guess that means the drinks are on you?",
        5: "Good show, old chap. You've won €" + str(bet) + "."}
    losingSentences = {
        1: "Ouch! That one will cost ya, €" + str(bet) + " to be exact.",
        2: "Well, you know what they say, maybe you're just lucky in love instead. You lost €" + str(bet) + ".",
        3: "Do you feel lucky, punk? Well you shouldn't, you just lost " + str(bet) + " big ones",
        4: "Why don't you just hand over the €" + str(bet) + " instead? It'll save you the time of betting.",
        5: "Sorry pall, better luck next time. You lost all " + str(bet) + " smackeroos."}
    coinGuess = input("Heads or Tails? ").lower()
    flip = random.randint(0, 1)
    results = random.randint(1, 5)
    di = {0: "Heads", 1: "Tails"}
    if coinGuess == "heads":
        guess = 0
    else:
        guess = 1
    print("Ok! the coin landed on " + (di[flip]) + "!")
    time.sleep(1)
    if guess == flip:
        money += int(bet)
        print(winningSentences[results])
        time.sleep(1)
    else:
        money += -int(bet)
        print(losingSentences[results])
        time.sleep(1)
    print("You currently have €" + str(money) + " in chips")
    time.sleep(1)
    if money == 0:
        endGame()
    flipAgain()


def flipAgain():
    again = input("Would you like to flip again? ").lower()
    if again == "yes":
        coinToss()
    elif again == "no":
        another = input("Would you like to play a different game? ").lower()
        if another == "yes":
            startGame()
        elif another == "no":
            endGame()
        else:
            print("I'm sorry I didn't understand that, " + name + ". Were you trying to say spaghetti?")
            return flipAgain()
    else:
        print("I'm sorry I didn't understand that, " + name + ". Were you trying to say spaghetti?")
        return flipAgain()


def choHanRules():
    rules = input("Do you know the rules, " + name + "? ")
    if rules == "no":
        print("Cho Han is a traditional Japanese dice gambling game.")
        time.sleep(2)
        print("We roll two dice, and you bet on whether the number will be even or odd")
        time.sleep(2)
        print("Ok Let's play!")
        choHan()
    elif rules == "yes":
        print("Ok Let's play!")
        choHan()
    else:
        "Were you trying to say spaghetti?"
        choHanRules()


def choHan():
    global money
    bet = input("How much would you like to wager? ")
    if int(bet) == 0:
        noBet = input("You didnt bet anything, would you like to play something else? ")
        if noBet == "yes":
            startGame()
        if noBet == "no":
            stop = input("Do you want to go home? ")
            if stop == "yes":
                endGame()
            else:
                coinToss()
    time.sleep(1)
    try:
        val = int(bet)
        print("Alright, betting has closed.")
    except ValueError:
        print("Sorry, I'm not sure what " + bet + " is, we only wager in legal currency here.")
        choHan()
    if int(bet) > money:
        print("Sorry, you don't have that kind of scratch. Place a lower bet or get out of here")
        return coinToss()
    if int(bet) == money:
        print("Wow, all in? Living on the edge!")
    if money < 20:
        sure = input("Are you sure you want to keep playing? You only have " + str(money) + " left.").lower()
        if sure == "no":
            endGame()
    winningSentences = {
        1: "AMAZING! What are the odds? One of us should know. You just won " + str(bet) + " smackeroos!",
        2: "Well wasn't that something! Are your pockets getting heavy? Because you just won €" + str(bet) + ".",
        3: "Do you feel lucky, punk? Well you should, you just won " + str(bet) + " big ones!",
        4: "You won €" + str(bet) + ", so I guess that means the drinks are on you?",
        5: "Good show, old chap. You've won €" + str(bet) + "."}
    losingSentences = {
        1: "Ouch! That one will cost ya, €" + str(bet) + " to be exact.",
        2: "Well, you know what they say, maybe you're just lucky in love instead. You lost €" + str(bet) + ".",
        3: "Do you feel lucky, punk? Well you shouldn't, you just lost " + str(bet) + " big ones",
        4: "Why don't you just hand over the €" + str(bet) + " instead? It'll save you the time of betting.",
        5: "Sorry pall, better luck next time. You lost all " + str(bet) + " smackeroos."}
    diceGuess = input("Even or Odd? ").lower()
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll = die1 + die2
    print("Ok, first die is a " + str(die1) + "!")
    time.sleep(1)
    results = random.randint(1, 5)
    if roll % 2 == 0:
        dice = "even"
    else:
        dice = "odd"
    print("Aaaaannnnddd - the second die is a " + str(die2) + " for a total of " + str(roll) + " which is " + str(dice) + "!")
    time.sleep(1)
    if diceGuess == dice:
        money += int(bet)
        print(winningSentences[results])
        time.sleep(1)
    else:
        money += -int(bet)
        print(losingSentences[results])
        time.sleep(1)
    print("You currently have €" + str(money) + " in chips")
    rollAgain()


def rollAgain():
    again = input("Would you like to roll again? ").lower()
    if again == "yes":
        choHan()
    elif again == "no":
        another = input("Would you like to play a different game? ").lower()
        if another == "yes":
            startGame()
        elif another == "no":
            endGame()
        else:
            print("I'm sorry I didn't understand that, " + name + ". Were you trying to say spaghetti?")
            return rollAgain()
    else:
        print("I'm sorry I didn't understand that, " + name + ". Were you trying to say spaghetti?")
        return rollAgain()


def roulette():
    global money
    bets = 0
    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    blacks = [2, 4, 6, 8, 10, 20, 22, 24, 26, 28, 34, 11, 13, 15, 17, 29, 31, 33, 35]
    di = {1: "Red", 3: "Red", 5: "Red", 7: "Red", 9: "Red", 12: "Red", 14: "Red", 16: "Red", 18: "Red", 19: "Red",
          21: "Red", 23: "Red", 25: "Red", 27: "Red", 30: "Red", 32: "Red", 34: "Red", 36: "Red", 2: "Black",
          4: "Black", 6: "Black", 8: "Black", 10: "Black", 20: "Black", 22: "Black", 24: "Black", 26: "Black",
          28: "Black", 34: "Black", 11: "Black", 13: "Black", 15: "Black", 17: "Black", 29: "Black", 31: "Black",
          33: "Black", 35: "Black"}
    marble = random.randint(1, 36)
    results = random.randint(1, 5)
    results2 = random.randint(1, 5)
    results3 = random.randint(1, 5)
    marble2 = marble
    marble3 = marble
    high = range(19, 36)
    low = range(1, 19)
    time.sleep(2)
    bet = input("How much would you like to wager per bet? ")
    if int(bet) == 0:
        noBet = input("You didnt bet anything, would you like to play something else? ")
        if noBet == "yes":
            startGame()
        if noBet == "no":
            stop = input("Do you want to go home? ")
            if stop == "yes":
                endGame()
            else:
                coinToss()
    time.sleep(1)
    try:
        val = int(bet)
        print("Alright!")
    except ValueError:
        print("Sorry, I'm not sure what " + bet + " is, we only wager in legal currency here.")
        roulette()
    if int(bet) > money:
        print("Sorry, you don't have that kind of scratch. Place a lower bet or get out of here")
        return roulette()
    if int(bet) == money:
        print("Wow, all in? Living on the edge!")
    if money < 20:
        sure = input("Are you sure you want to keep playing? You only have " + str(money) + " left.").lower()
        if sure == "no":
            endGame()
    winningSentences = {
        1: "AMAZING! What are the odds? One of us should know. You just won " + str(bet) + " smackeroos!",
        2: "Well wasn't that something! Are your pockets getting heavy? Because you just won €" + str(bet) + ".",
        3: "Do you feel lucky, punk? Well you should, you just won " + str(bet) + " big ones!",
        4: "You won €" + str(bet) + ", so I guess that means the drinks are on you?",
        5: "Good show, old chap. You've won €" + str(bet) + "."}
    losingSentences = {
        1: "Ouch! That one will cost ya, €" + str(bet) + " to be exact.",
        2: "Well, you know what they say, maybe you're just lucky in love instead. You lost €" + str(bet) + ".",
        3: "Do you feel lucky, punk? Well you shouldn't, you just lost " + str(bet) + " big ones",
        4: "Why don't you just hand over the €" + str(bet) + " instead? It'll save you the time of betting.",
        5: "Sorry pall, better luck next time. You lost all " + str(bet) + " smackeroos."}
    print("If you'd like to place a color bet, please type 'Red' or 'Black'")
    color = input("Otherwise, just press return. ").lower()
    if color == "red" or color == "black":
        bets += 1
    time.sleep(1)
    ooe = input("Now, tell us if you think it will be 'Odd' or 'Even,' or you can skip this bet. ").lower()
    if ooe == "odd" or ooe == "even":
        bets += 1
    time.sleep(1)
    hilo = input("What about the number? Will it be high or low? ").lower()
    if hilo == "high" or hilo == "low":
        bets += 1
    if bets == 1:
        print("Ok, I see you've only placed one bet.")
        time.sleep(1)
        if int(bet) == money:
            if color == "red" or color == "black":
                print("And you're putting it all on " + color + ".")
                time.sleep(1)
                if color == "black":
                    print("Just like the movies")
                    time.sleep(1)
    if bets > 1:
        print("Ok, you've placed " + str(bets) + " bets.")
    time.sleep(1)
    if bets == 0:
        zeroBets = input("You didn't place any bets. Do you want to start again, play something else, or just watch?")
        if "start" in zeroBets:
            roulette()
        if "else" in zeroBets:
            startGame()
        else:
            print("Voyeur.")
    # color bet
    if marble in reds:
        marble = "red"
    if marble in blacks:
        marble = "black"
    print("And around and around she goes!")
    time.sleep(1)
    print("..3..")
    time.sleep(1)
    print("..2..")
    time.sleep(1)
    print("..1..")
    time.sleep(1)
    print("Ok, the wheel has stopped!")
    time.sleep(1)
    print("The marble landed on " + str(marble3) + " " + str(marble))
    time.sleep(2)
    if color == "red" or color == "black":
        if color == marble:
            money += int(bet)
            print("You won the color bet!")
            time.sleep(2)
            print(winningSentences[results])
            time.sleep(2)
        if color != marble:
            money += -int(bet)
            print("You lost the color bet!")
            time.sleep(2)
            print(losingSentences[results])
            time.sleep(2)
    else:
        print("you didnt place a color bet")
        time.sleep(1)

    # odd or even
    if marble2 % 2 == 0:
        marble2 = "even"
    else:
        marble2 = "odd"
    if ooe == "odd" or ooe == "even":
        if ooe == marble2:
            money += int(bet)
            print("You won the odds/evens bet!")
            time.sleep(2)
            print(winningSentences[results2])
            time.sleep(2)
        if ooe != marble2:
            money += -int(bet)
            print("You lost the odds/evens bet!")
            time.sleep(2)
            print(losingSentences[results2])
            time.sleep(2)
    else:
        print("You didn't place an odd/even bet")
        time.sleep(1)

    # hilo
    if marble3 in range(19, 37):
        marble3 = "high"
    if marble3 in range(1, 19):
        marble3 = "low"
    if hilo == "high" or hilo == "low":
        if hilo == marble3:
            money += int(bet)
            print("You won the hilo bet!")
            time.sleep(2)
            print(winningSentences[results3])
            time.sleep(2)
        if hilo != marble3:
            money += -int(bet)
            print("You lost the hilo bet!")
            time.sleep(2)
            print(losingSentences[results3])
            time.sleep(2)
    else:
        print("You didn't place a high/low bet")
        time.sleep(1)
    if bets == 0:
        print("You didnt place any bets")

    print("You currently have €" + str(money) + " in chips")
    playAgain()


def playAgain():
    again = input("Would you like to spin the wheel again? ").lower()
    if again == "yes":
        roulette()
    elif again == "no":
        another = input("Would you like to play a different game? ").lower()
        if another == "yes":
            startGame()
        elif another == "no":
            endGame()
        else:
            print("I'm sorry I didn't understand that, " + name + ". Were you trying to say spaghetti?")
            return playAgain()
    else:
        print("I'm sorry I didn't understand that, " + name + ". Were you trying to say spaghetti?")
        return playAgain()


firstName = random.randint(1, 10)
names = {
    1: "Bob",
    2: "Michael",
    3: "Jermaine",
    4: "Susan",
    5: "Stacey",
    6: "Dominique",
    7: "Alejandro",
    8: "Ali",
    9: "Fatima",
    10: "Camila"
}
name = input("Hello, what is your name? ")
if len(name) == 0:
    print("I mean, you can give me a fake name")
    print("I'll call you " + (names[firstName]) + " instead")
    name = names[firstName]
print("Hello, " + name + ".")
time.sleep(1)
print("My name is Computer.")
time.sleep(1)
playGame()
