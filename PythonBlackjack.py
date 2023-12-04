import random
import os
import sys
from colorama import init, Fore, Style
init()

blank_cards_ascii = {
    0: """
       _______
    |?      |
    |       |
    |       |
    |       |
    |______?|
    """,   
}

cards_ascii = {
    0: """
     _______
    |?      |
    |       |
    |       |
    |       |
    |______?|
    """,   
    2: """
     _______
    |2      |
    |  ♥    |
    |       |
    |    ♥  |
    |______2|
    """,

    3: """
     _______
    |3      |
    | ♥ ♥   |
    |       |
    |   ♥   |
    |______3|
    """,

    4: """
     _______
    |4      |
    | ♥  ♥  |
    |       |
    | ♥  ♥  |
    |______4|
    """,

    5: """
     _______
    |5      |
    | ♥  ♥  |
    |   ♥   |
    | ♥  ♥  |
    |______5|
    """,

    6: """
     _______
    |6      |
    | ♥  ♥  |
    | ♥  ♥  |
    | ♥  ♥  |
    |______6|
    """,

    7: """
     _______
    |7      |
    | ♥ ♥ ♥ |
    | ♥  ♥  |
    | ♥  ♥  |
    |______7|
    """,

    8: """
     _______
    |8      |
    |♥ ♥ ♥  |
    | ♥  ♥  |
    |♥ ♥ ♥  |
    |______8|
    """,

    9: """
     _______
    |9      |
    |♥ ♥ ♥ ♥|
    | ♥  ♥  |
    |♥ ♥ ♥ ♥|
    |______9|
    """,

    10: """
     _______
    |10 ♥ ♥ |
    |♥ ♥ ♥ ♥|
    |♥ ♥ ♥ ♥|
    |♥ ♥ ♥ ♥|
    |___10__|
    """,

    'J': """
     _______
    |J  ww  |
    |   {)  |
    |   %   |
    |  %%%  |
    |___J___|
    """,

    'Q': """
     _______
    |Q  ww  |
    |   {)  |
    |   %   |
    |  %%%  |
    |___Q___|
    """,

    'K': """
     _______
    |K  WW  |
    |   {)  |
    |   %   |
    |  %%%  |
    |___K___|
    """,

    11: """
     _______
    |A      |
    |   ♥   |
    |  JAX  |
    |   ♥   |
    |______A|
    """
}


def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def CalculatePoints(hand):
    """This function will calculate the points"""
    pnts = 0
    detect_ace = False
    for i in (hand):
            pnts += i
            if (i == 11):
                # print('Ace Detected! ')
                detect_ace = True
    if pnts > 21 and detect_ace == True:
        pnts -= 10
        detect_ace = False
    return pnts

def PrintArt(hand):
    user_hand = hand
    cards_lines = [cards_ascii[card].split('\n') for card in user_hand]

    # Get the number of lines in the ASCII art (assuming all cards have the same number of lines)
    num_lines = len(cards_lines[0])

    # Print each line of each card's ASCII art side by side
    for i in range(num_lines):
        for card in cards_lines:
            print(card[i], end='  ')
        print()

def DealPlayerCard(user_hand, deck):
    """Simple function to deal a new player card."""
    print('\nDealing card to player')
    new_card = random.choice(deck[1:])
    user_hand.append(new_card)
    print(cards_ascii.get(new_card))
    return user_hand

def DealDealerCard(dealer_hand, deck):
    """This is a function to deal a new card to the dealer."""
    print(f'\n{Fore.YELLOW}Dealing card to dealer{Style.RESET_ALL}')
    dealer_hand.append(random.choice(deck[1:]))
    return dealer_hand

def PlayBlackjack(game_mode, player_name, player_money):
    """This is the main function of the whole program.
    This probably needs to be cut down quite a bit.
    I'm using it for both current game modes so I have a number of game mode flags in the code"""
    # Initialize the deck
    deck = [0, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Initialize the user and dealer hands
    user_hand = []
    dealer_hand = []

    # lets set some variables
    points = 0
    dealer_points = 0
    bet = 0

    if game_mode == 2 or game_mode == 3:
        if player_money <= 0:
            print('Oh no! It seems you are all out of money!')
            input('Press any key to continue...')
            run_game()
            
        bet_continue = False
        try:
            while not bet_continue:
                bet = int(input(f'{player_name}, place your bet : '))
                if bet <= player_money:
                    player_money -= bet
                    print(f'Bet of {bet} has been placed. Good luck!')
                    bet_continue = True
                elif bet > player_money:
                    print('You do not have that much to bet. Place a smaller bet')
        except:
            PlayBlackjack(game_mode, player_name, player_money)

    # To start, we are going to give 2 cards to the user
    # and 2 cards to the dealer
    user_hand.append(random.choice(deck[1:]))
    user_hand.append(random.choice(deck[1:]))
    dealer_hand.append(random.choice(deck[1:]))
    dealer_hand.append(deck[0])

    # Now lets calculate the user points
    # and the dealer points
    points = CalculatePoints(user_hand)
    dealer_points = CalculatePoints(dealer_hand)
    dealers_card_to_show = dealer_hand[0]
    print(f'{Fore.YELLOW}Dealers hand : {dealer_hand[0]}\n {Style.RESET_ALL}') # We only want to show the dealers first card here, and no point value
    # print(cards_ascii.get(dealers_card_to_show), ' ', end=' ')
    PrintArt(dealer_hand)
 
    # If game mode is all stars or fixed income, lets print the money
    if game_mode == 2 or game_mode == 3:
        print(f'{Fore.GREEN}${player_money} | Your hand : {user_hand} : {points}{Style.RESET_ALL}')
        PrintArt(user_hand)
        # for i in user_hand:
            # print(cards_ascii.get(i), ' ', end=' ') 
    else:
         print(f'{Fore.GREEN}\n\nYour hand : {user_hand} : {points}{Style.RESET_ALL}')
         PrintArt(user_hand)
         # for i in user_hand:
         #    print(cards_ascii.get(i), ' ', end=' ')
    

    # Lets check to see if the user already has blackjack. If so, we need to deal dealer cards until the dealer has a card score that
    # is greater than 16. 
    # print('Checking if player has blackjack already...')
    if points == 21:
        print('Player has blackjack!')
        player_has_blackjack = 1

         # If the player has blackjack, we need to finish up the dealers cards now.
         # Anything lower than 16, and the dealer gets another card
        while dealer_points < 16:
             dealer_hand = DealDealerCard(dealer_hand, deck)
             CalculatePoints(dealer_hand)
        print(f'{Fore.YELLOW}Dealers Hand : {dealer_hand} : {dealer_points}{Style.RESET_ALL}')
        PrintArt(dealer_hand)
        
        for i in dealer_hand:
            print(cards_ascii.get(i), ' ', end=' ')
    
        # Now that our dealer total is over 16, we need to be sure its not a blackjack or a bust
        if dealer_points == 21:
            print(f'{Fore.RED}Dealer also has blackjack! Its a tie!{Style.RESET_ALL}')
            player_money += bet
            PlayBlackjack(game_mode, player_name, player_money)
        elif dealer_points > 21:
            print(f'{Fore.GREEN}Dealer has bust! Player wins!{Style.RESET_ALL}')
            bet += bet
            player_money += bet
 
   
        # Ok, so the player doesn't have blackjack with the intial cards. 
        # Now we see if the player wants more cards
            
    ###### START THE LOOP ####################################################
    ##########################################################################
    ##########################################################################

    deal_again = input(f'{Fore.GREEN}Do you want another card? y/n : {Style.RESET_ALL}').lower()
    while deal_again == 'y':
        clear_screen()
        # user_hand.append(random.choice(deck))
        # points = CalculatePoints(user_hand)
        # user_hand.append(random.choice(deck))
        if game_mode != 2 or game_mode != 3:
            print(f'{Fore.YELLOW}Dealers Hand : {dealer_hand[0]}{Style.RESET_ALL}')
            print(cards_ascii.get(dealers_card_to_show), ' ', end=' ')
         
            DealPlayerCard(user_hand, deck)
            points = CalculatePoints(user_hand)
            print(f'{Fore.GREEN}\nYour hand : {user_hand} : {points}{Style.RESET_ALL}')
            PrintArt(user_hand)
        elif game_mode == 2 or game_mode == 3:
            print(f'{Fore.YELLOW}Dealers Hand : {dealer_hand[0]}{Style.RESET_ALL}')
            print(cards_ascii.get(dealers_card_to_show), ' ', end=' ')
         
            DealPlayerCard(user_hand, deck)
            points = CalculatePoints(user_hand)
            print(f'{Fore.GREEN}\n{player_money} | Your hand : {user_hand} : {points}{Style.RESET_ALL}')
            PrintArt(user_hand)
        if points > 21:
            print(f'{Fore.RED}Player has bust!{Style.RESET_ALL}')
            input(' ')
            play_again = input(f'\n\n{Fore.GREEN}Do you want to play another hand? (y/n) : {Style.RESET_ALL}').lower()
            if play_again == 'y':
                clear_screen()
                PlayBlackjack(game_mode, player_name, player_money)
            else:
                sys.exit()
        elif points == 21:
            print('{Fore.GREEN}Player has blackjack!{Style.RESET_ALL}')
            input('Press any key to deal cards to dealer...')
            clear_screen()
            deal_again = 'n'

        if deal_again != 'n':
            deal_again = input(f'{Fore.GREEN}Do you want another card? y/n : {Style.RESET_ALL}').lower()

    #### EXIT PLAYER LOOP #############################
    ###################################################
    #### LETS FINISH THE GAME #########################
    
    # Now that the player has finished getting cards, lets show the dealers full hand
    clear_screen()
    second_dealer_card = random.choice(deck[1:])
    # dealer_hand.append(second_dealer_card)
    dealer_hand[1] = second_dealer_card
    dealer_points = CalculatePoints(dealer_hand)
    print(f'{Fore.YELLOW}Dealers FULL Hand : {dealer_hand} {dealer_points}{Style.RESET_ALL}')
    PrintArt(dealer_hand)
 
    print(f'{Fore.GREEN}\nYour hand : {user_hand} : {points}{Style.RESET_ALL}')
    PrintArt(user_hand)

    # If the dealers hand is less than 16, we need to keep adding cards
    while dealer_points < 16:
        print(f'{Fore.YELLOW}Dealers hand is less than 16. Drawing a card..{Style.RESET_ALL}')
        input('')
        clear_screen()
        dealer_hand = DealDealerCard(dealer_hand, deck)
        dealer_points = CalculatePoints(dealer_hand)
        print(f'{Fore.YELLOW}Dealers hand : {dealer_hand} : {dealer_points}{Style.RESET_ALL}')
        PrintArt(dealer_hand)
     
        print(f'{Fore.GREEN}\nYour hand : {user_hand} : {points}{Style.RESET_ALL}')
        PrintArt(user_hand)


    # We wont be here until our dealers cards are over 16.
    # When they are, lets show a message to say we dont need any more cards
    print(f'{Fore.YELLOW}Dealers points are 16 or above. No more cards needed{Style.RESET_ALL}')
    input(' ')
    clear_screen()

    # Now lets show the players final hand and the points
    # and also the dealers final hand and points
    if game_mode == 2 or game_mode == 3:
        print(f'{Fore.YELLOW}Dealers Final Hand : {dealer_hand} {dealer_points}{Style.RESET_ALL}')
        PrintArt(dealer_hand)
     
        print(f'{Fore.GREEN}\n{player_money} | Players Final Hand : {user_hand} {points}{Style.RESET_ALL}')
        PrintArt(user_hand)
    elif game_mode != 2:
        print(f'{Fore.YELLOW}Dealers Final Hand : {dealer_hand} {dealer_points}{Style.RESET_ALL}')
        PrintArt(dealer_hand)
     
        print(f'{Fore.GREEN}\nPlayers Final Hand : {user_hand} {points}{Style.RESET_ALL}')
        PrintArt(user_hand)
        
    # Now we start to check to see who won.
    if (points == 21) and (dealer_points == 21):
        print(f'{Fore.RED}Tie! No one wins{Style.RESET_ALL}')

    elif dealer_points == 21:
        print(f'{Fore.YELLOW}Dealer has blackjack! {Fore.RED}You lose!{Style.RESET_ALL}')
        print(f'{Fore.RED}You win nothing!{Style.RESET_ALL}')
        play_again = input(f'\n\n{Fore.GREEN}Do you want to play another hand? (y/n) : {Style.RESET_ALL}').lower()
        if play_again == 'y':
            clear_screen()
            PlayBlackjack(game_mode, player_name, player_money)
        else:
            run_game()
        
    elif points == 21:
        print('Player Wins!')
        if game_mode == 2 or game_mode == 3:
            bet += bet
            player_money += bet
            print(f'{Fore.GREEN}You win {bet}. Current Money : {Fore.WHITE}${player_money}{Style.RESET_ALL}')

    elif dealer_points > 21:
        print(f'{Fore.GREEN}Dealer has bust! Player wins!{Style.RESET_ALL}')
        if game_mode == 2 or game_mode == 3:
            bet += bet
            player_money += bet
            print(f'{Fore.GREEN}You win {bet}. Current Money : {Fore.WHITE}${player_money}{Style.RESET_ALL}')

    elif points > dealer_points:
        print(f'{Fore.GREEN}Player wins!{Style.RESET_ALL}')
        if game_mode == 2 or game_mode == 3:
            bet += bet
            player_money += bet
            print(f'{Fore.GREEN}You win {bet}. Current Money : {Fore.WHITE}${player_money}{Style.RESET_ALL}')

    elif dealer_points > points:
        print(f'{Fore.YELLOW}Dealer Wins!{Style.RESET_ALL}')
        if game_mode == 2 or game_mode == 3:
            print(f'{Fore.RED}You win nothing!{Style.RESET_ALL}')

    elif points == dealer_points:
        print('Tie!')
        if game_mode == 2 or game_mode == 3:
            player_money += bet
            print(f'{Fore.GREEN}You win your bet of {bet} back{Style.RESET_ALL}')
            
    # Now lets ask the player if we should keep playing
    play_again = input(f'\n\n{Fore.GREEN}Do you want to play another hand? (y/n) : {Style.RESET_ALL}').lower()
    if play_again == 'y':
        clear_screen()
        PlayBlackjack(game_mode, player_name, player_money)
    else:
        run_game()

def SetupAllStar(game_mode):
    """This function sets up the All Star Game mode. We will take in a player name, 
    and ask the player how much money they would like to start with.
    We will then call the main function PlayBlackJack with our new arguments"""
    player_name = input('\nWhat is your name : ')
    player_money = int(input('How much money do you want to start with : '))
    PlayBlackjack(game_mode, player_name, player_money)

def PreloadBlackjack(game_mode):
    """This function sets up some default values for variables that would normally be
    used in the PlayBlackJack function. We do not need these values, as these values only
    pertain to the All Star mode, but since I am using the same function for both modes, I need
    to pass in values or it will throw an error"""
    player_name = ' ' # Not needed in this mode, can we remove it without throwing an error?
    player_money = 0 # we dont really need to load the value here, but since we have to send an argument
    PlayBlackjack(game_mode, player_name, player_money)

def FixedIncomeSetup(game_mode):
    """This function sets up some default values for variables that would normally be
    used in the PlayBlackJack function. We do not need these values, as these values only
    pertain to the All Star mode, but since I am using the same function for both modes, I need
    to pass in values or it will throw an error"""
    player_name = input('\nWhat is your name : ')
    player_money = 1000 
    PlayBlackjack(game_mode, player_name, player_money)

def run_game():
    """This is the main function for the game.
    Option 1 is the quick blackjack game mode with no betting.
    Option 2 is the betting mode where you can pick your starting value
    Option 3 is betting with a set start value of $1000
    Option 4 quits the game"""
    run_option = {
     1: PreloadBlackjack,
     2: SetupAllStar,
     3: FixedIncomeSetup,
     4: sys.exit
    }
    game_mode = 0
    game_start = False

    try:
        while not game_start:
                print('---------------------')
                print('Welcome to Blackjack')
                print('---------------------')
                print('1. Play Quick Blackjack (no betting)')
                print('2. BlackJack All-Stars (betting, you choose start value)')
                print('3. Fixed Income (betting, start with $1000)')
                print('4. Quit')
                print('---------------------')
                game_mode = int(input('Selection : '))
                if game_mode == 1 or game_mode == 2 or game_mode == 3 or game_mode == 4:
                    game_start = True
    except:
        run_game()

    func = run_option.get(game_mode) 
    clear_screen()
    func(game_mode)


#####################################################
# Lets Initialize the game.
clear_screen()
run_game()


