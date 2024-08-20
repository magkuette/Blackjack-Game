# Documentation
"""
Blackjack Game

Run this program to play Blackjack.

DESCRIPTION AND RULES:
This game of Blackjack involves a deck of 52 cards. You will play with the Blackjack dealer.
First, each you and the Blackjack dealer will draw two cards from the deck of cards.
Your cards will be visible to you, and you will be able to know the total card value of the cards.
As for the dealer's cards, you will only be able to see one of their cards.

In the event that you or the dealer gets a card that has an A, K, Q, or J: an A is always worth 11, and K, Q, and J are always worth 10 each.

This Blackjack game will calculate your total card value for you.
You will then determine whether you would like to "hit" or "stay".
Hitting involves drawing another card from the deck. Staying involves doing nothing.
Once you choose to stay, you are stuck with the amount of cards you have at that moment.

As for the dealer, they will keep taking new cards until their total card value is 17 or higher.
Once their total card value is 17 or higher, they will stay.
Additionally, the user will only be able to see all of the dealer's cards once the dealer has a card value of 17 or higher.
If the dealer has a card value of 16 or lower, the user will only be able to see one of the dealer's cards.

Be careful with hitting, as going over a card value of 21 will result in a bust, meaning you lose.
If someone busts, then the other player wins.

In the event that the card value of the dealer is at least 17 and therefore must stay while you are also staying,
the higher card value between you and the dealer will win.

Another way to win is to get to a card value of 21 first, which is a Blackjack.

After every win, the program will ask you if you would like to play again.
If you would like to play again and there are no more cards in the deck (since drawing a card means it is gone from the deck),
then no problem! The deck will reshuffle and all the cards will be restored into the deck.

IN THE EVENT OF AN ERROR:
In the event that the program doesn't run smoothly, you can stop running the program by pressing the stop button on Visual Studio Code
(red square at the top of the screen). You can then go to Run to restart the program.
"""
import random # This will be used to get a random card from the deck (cardList)

print("""
      Before we proceed, let's explain the card values of each card:
      With cards with numbers on them, it is pretty straightforward as
      to what their integer value is. For example, '♥ 2' has a value of 2.
      As for the others, J has a value of 10, Q has a value of 10, K has a value of 10,
      and A always has a value of 11.
      That being said, let's start!
      """)

# Rounds of Blackjack where each player (in this case, the user and the dealer) is dealt a card from a standard 52 card deck (this deck, in this case, is cardList).    

# cardList is a standard 52 deck of cards
cardList = ["♠ 2", "♠ 3", "♠ 4", "♠ 5", "♠ 6", "♠ 7", "♠ 8", "♠ 9", "♠ 10", "♠ J", "♠ Q", "♠ K", "♠ A",
            "♥ 2", "♥ 3", "♥ 4", "♥ 5", "♥ 6", "♥ 7", "♥ 8", "♥ 9", "♥ 10", "♥ J", "♥ Q", "♥ K", "♥ A",
            "♦ 2", "♦ 3", "♦ 4", "♦ 5", "♦ 6", "♦ 7", "♦ 8", "♦ 9", "♦ 10", "♦ J", "♦ Q", "♦ K", "♦ A",
            "♣ 2", "♣ 3", "♣ 4", "♣ 5", "♣ 6", "♣ 7", "♣ 8", "♣ 9", "♣ 10", "♣ J", "♣ Q", "♣ K", "♣ A"]


# cardValues is the values of each card from the standard 52 deck of cards (cardList).
# cardValues is arranged in a way that makes it so that each card/index in cardList corresponds to its respective value from cardValues.
# ^ For example, cardList[1] is ♠ 3. cardValues[1] is 3. This is correct as ♠ 3 is indeed a value of 3.
cardValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
              2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
              2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
              2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

if len(cardList) > 0: # Once len(cardList) is not > 0 (i.e. once len(cardList) = 0), this means that the deck is out of cards.

    roundCounter = 1 # This will count the number of rounds the user plays. It starts at one because this is considered the first round.
    dealerWinCounter = 0 # This will count the number of times the dealer wins.
    userWinCounter = 0 # This will count the number of times the user wins.
    tieCounter = 0 # This will count the number of times there is a tie.

    while len(cardList) > 0: # Once len(cardList) is not > 0 (i.e. once len(cardList) = 0), this means that the deck is out of cards.

        # User's Play
        def userCardsPlay(cardCounter = 2): # cardCounter = 2 because initially, the user must draw 2 cards.

            """
            This is the user's play of this Blackjack game.

            userCards is the cards the user has. userCardValues is the values of the cards the user has.
            (For example, if userCards is [♠ 2, ♠ K] then userCardValues will be [2, 10].)

            The function will first check whether or not there are enough cards in the deck (cardList) to proceed with the game.
            If there is a number of less than 2 indices in cardList, we break out of the loop; if there are at least 2 indicides in cardList, we continue.

            A random index from cardList will be chosen--this represents the card that is drawn for the user. The index number of this card (drawnCard) will be obtained and
            stored into indexOfDrawnCard. This will be used to obtain the value of this card, which will be obtained from cardValues.
            The drawnCard will be removed from cardList so it will not be drawn again, and drawnCard will be appended to userCards; in other words,
            drawnCard will be added to the user's collection of cards (userCards).
            indexOfDrawnCard will be used to track which index drawnCard corresponds to in cardValues. The program will pop this value from cardValues out
            (so as to not mess up to order of values in cardValues) and append it to userCardValues so as to match the value to the card that is in userCards.

            What is described in the above two paragraphs will be repeated once more (for a total of 2 times). This is made possible by the cardCounter which equals 2.
            This is a 2 because the user is to draw 2 cards intially. (Later, the function will be called with the syntax userCardsPlay(1) so as to only draw once when the user hits.)

            After that loop, the sum of the userCardValues will be calculated and stored into userCardTotal. For example, if userCards values is [2, 10], then
            userCardTotal will be 12.

            The function will then return userCards, userCardValues, and userCardTotal so that they can be used outside of the function.
            """
            userCards = [] # This is a list of cards the user has. Right now it is [] which is an empty list. This means that right now, the user has no cards. But later, cards from cardList will be added to this list.
            userCardValues = [] # This is a list of the card values of cards the user has. Right now it is [] which is an empty list. This means that right now, the user has no cards, thus no card values. But later, this list will consist of the card values the user has.

            for _ in range(cardCounter): # This will loop for the amount of times cardCounter is equal to (which, as stated in line 78, is 2). This is to ensure that a user will draw a card for the amount of times cardCounter is equal to. If cardCounter is equal to 2, the user will draw 2 cards.
                if len(cardList) >= 2: # If the card deck has less than 2 cards left, then the game cannot continue on --> break out of loop.
                    drawnCard = random.choice(cardList) # Choose a random card from cardList. This is the equivalent of drawing a random card from the card deck.
                else:
                    break # Breaks out of loop
                indexOfDrawnCard = cardList.index(drawnCard) # Gets which index drawnCard was (in cardList) and puts it in indexOfDrawnCard.
                cardList.remove(drawnCard) # drawnCard is removed from the deck called cardList so that card cannot be drawn again.
                userCards.append(drawnCard) # drawnCard is added to userCards (essentially the user has taken the card from the deck cardList).
                userCardValues.append(cardValues.pop(indexOfDrawnCard)) # Taking the number that is indexOfDrawnCard. With this number, this index number is popped out of cardValues list and then appended into userCardValues. This is to get the value of the drawn card.

            userCardTotal = sum(userCardValues) # Adds up the values of the cards in userCardValues i.e. the values of the cards the user has
                
            return userCards, userCardValues, userCardTotal # Return so that they can be used outside of the function.

        userCards, userCardValues, userCardTotal = userCardsPlay() # Unpack tuple into userCardsPlay() so that userCards, userCardValues, and userCardTotal can each be used on their own.

        # Dealer's Play
        def dealerCardsPlay(cardCounter = 2): # cardCounter = 2 because initially, the dealer must draw 2 cards.

            """
            This is the dealer's play of this Blackjack game.

            dealerCards is the cards the dealer has. dealerCardValues is the values of the cards the dealer has.
            (For example, if userCards is [♠ 2, ♠ K] then userCardValues will be [2, 10].)

            The function will first check whether or not there are enough cards in the deck (cardList) to proceed with the game.
            If there is a number of less than 2 indices in cardList, we break out of the loop; if there are at least 2 indicides in cardList, we continue.

            A random index from cardList will be chosen--this represents the card that is drawn for the dealer. The index number of this card (drawnCard) will be obtained and
            stored into indexOfDrawnCard. This will be used to obtain the value of this card, which will be obtained from cardValues.
            The drawnCard will be removed from cardList so it will not be drawn again, and drawnCard will be appended to dealerCards; in other words,
            drawnCard will be added to the dealer's collection of cards (dealerCards).
            indexOfDrawnCard will be used to track which index drawnCard corresponds to in cardValues. The program will pop this value from cardValues ou
            (so as to not mess up to order of values in cardValues) and append it to dealerCardValues so as to match the value to the card that is in userCards.

            What is described in the above two paragraphs will be repeated once more (for a total of 2 times). This is made possible by the cardCounter which equals 2.
            This is a 2 because the dealer is to draw 2 cards intially. (Later, the function will be called with the syntax dealerCardsPlay(1) so as to only draw once when the dealer must hit.)

            After that loop, the sum of the dealerCardValues will be calculated and stored into dealerCardTotal. For example, if dealerCards values is [2, 10], then
            dealerCardTotal will be 12.

            The function will then return dealerCards, dealerCardValues, and dealerCardTotal so that they can be used outside of the function.
            """

            dealerCards = [] # This is a list of cards the dealer has. Right now it is [] which is an empty list. This means that right now, the dealer has no cards. But later, cards from cardList will be added to this list.
            dealerCardValues = [] # This is a list of the card values of cards the dealer has. Right now it is [] which is an empty list. This means that right now, the dealer has no cards, thus no card values. But later, this list will consist of the card values the dealer has.

            for _ in range(cardCounter): # This will loop for the amount of times cardCounter is equal to (which, as stated in line 124, is 2)
                if len(cardList) >= 2: # If the card deck has less than 2 cards left, then the game cannot continue on --> break out of loop.
                    drawnCard = random.choice(cardList) # Choose a random card from cardList. This is the equivalent of drawing a random card from the card deck.
                else:
                    break # Breaks out of loop
                indexOfDrawnCard = cardList.index(drawnCard) # Gets which index drawnCard was in (in cardList) and puts it in indexOfDrawnCard
                cardList.remove(drawnCard) # drawnCard is removed from the deck called cardList
                dealerCards.append(drawnCard) # drawnCard is added to dealerCards (essentially the dealer has taken the card from the deck cardList)
                dealerCardValues.append(cardValues.pop(indexOfDrawnCard)) # Taking the number that is indexOfDrawnCard. With this number, this index number is popped out of cardValues list and then appended into dealerCardValues.

            dealerCardTotal = sum(dealerCardValues) # Adds up the values of the cards in dealerCardValues i.e. the cards the dealer has
                
            return dealerCards, dealerCardValues, dealerCardTotal # Return so that they can be used outside of the function.

        dealerCards, dealerCardValues, dealerCardTotal = dealerCardsPlay() # Unpack tuple into dealerCardsPlay() so that dealerCards, dealerCardValues, and dealerCardTotal can each be used on their own.
            
        while userCardTotal < 21 and dealerCardTotal < 21: # Loop while less than 21 because 21 means Blackjack --> game over; over 21 means bust --> game over.
            
            dealerCardsJoined = ", ".join(dealerCards) # Makes dealerCards list into one string.
            userCardsJoined = ", ".join(userCards) # Makes userCards list into one string.

            if dealerCardTotal < 17: # If the dealer has a total value of cards less than 17, the user can only see the dealer's first card. The rest of the dealer's cards are unknown to the user.
                if len(cardList) >= 2: # If the card deck has less than 2 cards left, then the game cannot continue on --> break out of loop.
                    while True: # try except will keep looping till the user inputs "hit" or "stay"
                        try: # Catches error.
                            # Player can choose to 'hit' or 'stay'
                            userAnswer = input(f"""
                                        Your cards are {userCardsJoined} therefore making your total {userCardTotal}.
                                        The dealer's cards are {dealerCards[0]} and one or some other card(s) that are faced down, therefore making their total
                                        {dealerCardValues[0]} + some other card(s).
                                        Would you like to 'hit' or 'stay'?
                                        """).lower()
                            
                            if userAnswer != "hit" and userAnswer != "stay": # If userAnswer does not equal "hit" and does not equal "stay"
                                # ValueError is for when something does not equal the desired value.
                                # In this case, the desired value is "hit" and "stay". If the user types something other than these, then a ValueError will be raised.
                                raise ValueError("Please choose to 'hit' or 'stay'.") # The sentence in parentheses is stored into ValueError
                            
                            elif userAnswer == "hit" or userAnswer == "stay": # If the user answers with "hit" or "stay", then the loop will be broken and the game will continue.
                                break
                            
                        except ValueError as errorMessage: # ValueError is stored into errorMessage
                            print(f"{errorMessage}") # Output: "Please choose to 'hit' or 'stay'."
                else:
                    break # Breaks out of loop.
            elif dealerCardTotal >= 17: # If the dealer has a total value of cards of 17 or more, the user is able to see all of the dealer's cards (dealerCardsJoined)
                if len(cardList) >= 2: # If the card deck has less than 2 cards left, then the game cannot continue on --> break out of loop.
                    while True: # try except will keep looping till the user inputs "hit" or "stay"
                        try: # Catches error.
                            # Player can choose to 'hit' or 'stay'
                            userAnswer = input(f"""
                                        Your cards are {userCardsJoined} therefore making your total {userCardTotal}.
                                        The dealer's cards are {dealerCards[0]} and one or some other card(s) that are faced down, therefore making their total
                                        {dealerCardValues[0]} + some other card(s).
                                        Would you like to 'hit' or 'stay'?
                                        """).lower()
                            
                            if userAnswer != "hit" and userAnswer != "stay": # If userAnswer does not equal "hit" and does not equal "stay"
                                # ValueError is for when something does not equal the desired value.
                                # In this case, the desired value is "hit" and "stay". If the user types something other than these, then a ValueError will be raised.
                                raise ValueError("Please choose to 'hit' or 'stay'.") # The sentence in parentheses is stored into ValueError
                            
                            elif userAnswer == "hit" or userAnswer == "stay": # If the user answers with "hit" or "stay", then the loop will be broken and the game will continue.
                                break
                            
                        except ValueError as errorMessage: # ValueError is stored into errorMessage
                            print(f"{errorMessage}") # Output: "Please choose to 'hit' or 'stay'."

            # When a player chooses to stay, their total is set until the round is over and can't choose to hit again.
            if userAnswer == "stay":
                print("You chose to stay.") # The user is stuck with their current cards for the rest of the round (so until someone wins).

            if userAnswer == "hit":
                # Calling userCardsPlay() with cardCounter = 1 which means the function will be gone through once. This means one card will be drawn.
                newUserCards, newUserCardValues, newUserCardTotal = userCardsPlay(1) # newUserCards = new card drawn, newUserCardValues = value of new card drawn, newUserCardTotal = total of value of new card drawn.
                userCards += newUserCards # The newly drawn card is added to userCards
                userCardsJoined = ", ".join(userCards) # Combines the indices of userCards into one string that is put into userCardsJoined
                userCardTotal += newUserCardTotal # The total of the value of the new card drawn will be added to the value of the userCardTotal thus resulting in this being the updated total of the card values the user now has.
            
            # Player can choose to 'hit' or 'stay'
            while dealerCardTotal < 17: # So as long as the dealerCardTotal < 17, the dealer must keep drawing cards.
                # Calling dealerCardsPlay() with cardCounter = 1 which means the function will be gone through once. This means one card will be drawn.
                newDealerCards, newDealerCardValues, newDealerCardTotal = dealerCardsPlay(1) # newDealerCards = new card drawn, newDealerCardValues = value of new card drawn, newDealerCardTotal = total of value of new card drawn.
                dealerCards += newDealerCards # The newly drawn card is added to dealerCards
                newDealerCardsJoined = ", ".join(dealerCards) # Combines the indices of dealerCards into one string that is put into dealerCardsJoined
                dealerCardTotal += newDealerCardTotal # The total of the value of the new card drawn will be added to the value of the dealerCardTotal thus resulting in this being the updated total of the card values the dealer now has.

                print("The dealer has drawn another card.")

            newDealerCardsJoined = "" # Define newDealerCardsJoined again so that I can use it in future loops

            # The following loops determines losses, wins, and ties.

            # If someone busts, they lose immediately
            if userCardTotal > 21:
                print(f"Your cards are {userCardsJoined} therefore making your total {userCardTotal}; bust. You lose!")
                dealerWinCounter += 1
                break # Break because user lost.

            elif userCardTotal == 21:
                print(f"Your cards are {userCardsJoined} therefore making your total {userCardTotal}; Blackjack. You win!")
                userWinCounter += 1
                break # Break because user won.

            # If someone busts, they lose immediately
            if dealerCardTotal > 21:
                print(f"The dealer's cards are {newDealerCardsJoined} therefore making their total {dealerCardTotal}; the dealer busts. You win!")
                userWinCounter += 1
                break # Break because user won.
            elif dealerCardTotal == 21:
                print(f"The dealer's cards are {newDealerCardsJoined} therefore making their total {dealerCardTotal}; Blackjack. You lose!")
                dealerWinCounter += 1
                break # Break because user lost.

            # When the dealer has a total card value of at least 17, the dealer is to stay until the round ends.
            # In the event that the user chose to stay too, the cards the user and dealer has will stay the same.
            # When the cards of the user and dealer will stay the same for the whole round, the one with the highest card value wins.
            # If multiple players stay, the highest total wins
            if userAnswer == "stay" and dealerCardTotal >= 17:
                if userCardTotal > dealerCardTotal: # If the user has a higher total card value than that of the dealer's, the user wins.
                    print(f"""
                        Your cards are {userCardsJoined} therefore making your total {userCardTotal}.
                        The dealer's cars are {newDealerCardsJoined} therefore making their total {dealerCardTotal};
                        You win!
                        """)
                    userWinCounter += 1
                    break # Break because the user won.
                elif userCardTotal < dealerCardTotal: # If the user has a lesser total card value than that of the dealer's, the user loses.
                    print(f"""
                        Your cards are {userCardsJoined} therefore making your total {userCardTotal}.
                        The dealer's cards are {newDealerCardsJoined} therefore making their total {dealerCardTotal};
                        You lose!
                        """)
                    dealerWinCounter += 1
                    break # Break because the user lost.
                elif userCardTotal == dealerCardTotal: # If the user has an equal total card value to that of the dealer's, it's a tie.
                    print(f"""
                        Your cards are {userCardsJoined} therefore making your total {userCardTotal}.
                        The dealer's cars are {newDealerCardsJoined} therefore making their total {dealerCardTotal};
                        Tie!
                        """)
                    tieCounter += 1
                    break # Break because there was a tie.
        
        # Dictionary
        allGameStats = {
        "rounds played": f"{roundCounter}",
        "rounds won": f"{userWinCounter}",
        "rounds lost": f"{dealerWinCounter}",
        "ties": f"{tieCounter}"
            }
        
        # Access allGameStats, then access the keys (e.g. rounds played, rounds won, etc)
        print(f"""
            Your game stats so far:
            Number of rounds played: {allGameStats["rounds played"]}
            Number of rounds won: {allGameStats["rounds won"]}
            Number of rounds lost: {allGameStats["rounds lost"]}
            Number of ties: {allGameStats["ties"]}
            """)

        restartGamePrompt = input("Would you like to start another round?").lower()
        if restartGamePrompt == "no":
            break
        elif restartGamePrompt == "yes" and len(cardList) < 2: # There being less than 2 cards in cardList means the game cannot continue on as the user and dealer will need to draw cards. This means the deck will have to reshuffle.
            print("Out of cards. Reshuffling now.")

            # Adding all of the cards back into the deck (cardList)
            cardList = ["♠ 2", "♠ 3", "♠ 4", "♠ 5", "♠ 6", "♠ 7", "♠ 8", "♠ 9", "♠ 10", "♠ J", "♠ Q", "♠ K", "♠ A",
            "♥ 2", "♥ 3", "♥ 4", "♥ 5", "♥ 6", "♥ 7", "♥ 8", "♥ 9", "♥ 10", "♥ J", "♥ Q", "♥ K", "♥ A",
            "♦ 2", "♦ 3", "♦ 4", "♦ 5", "♦ 6", "♦ 7", "♦ 8", "♦ 9", "♦ 10", "♦ J", "♦ Q", "♦ K", "♦ A",
            "♣ 2", "♣ 3", "♣ 4", "♣ 5", "♣ 6", "♣ 7", "♣ 8", "♣ 9", "♣ 10", "♣ J", "♣ Q", "♣ K", "♣ A"]

            # Adding all of the card values back into cardValues
            cardValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        elif restartGamePrompt == "yes":
            roundCounter += 1

allGameStats = {
    "Number of rounds played": f"{roundCounter}",
    "Number of rounds won": f"{userWinCounter}",
    "Number of rounds lost": f"{dealerWinCounter}",
    "Number of ties": f"{tieCounter}"
}

openInFileAnswer = input("Thanks for playing! Would you like to view your game stats in a file?").lower()

if openInFileAnswer == "yes":
    fileName = "game_stats.txt"
    with open (fileName, "w") as gameStatsFile: # Open game_stats.txt. w means write so the program will either make a new file with the name of game_stats.txt or if the file already exists then it will overwrite whatever is in game_stats.txt.
        for category, number in allGameStats.items():
            gameStatsFile.write(f"{category}: {number}\n")
    print("File created")