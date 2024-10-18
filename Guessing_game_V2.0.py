import random
import time
import statistics
#Globals
times_guessed = 0
times_guessed_list = []
games_played_comp = 0
games_won_comp = 0
games_played_user = 0
games_won_user = 0
#GlobalFuncs
def title():
    time.sleep(2)
    print("Hello, ") 
    time.sleep(.5)
    print("Welcome to")
    time.sleep(1)
    print(    """
    ██╗░░██╗░█████╗░████████╗  ░░░░░░  ░█████╗░░█████╗░░░███╗░░██████╗░
    ██║░░██║██╔══██╗╚══██╔══╝  ░░░░░░  ██╔══██╗██╔══██╗░████║░░██╔══██╗
    ███████║██║░░██║░░░██║░░░  █████╗  ██║░░╚═╝██║░░██║██╔██║░░██║░░██║
    ██╔══██║██║░░██║░░░██║░░░  ╚════╝  ██║░░██╗██║░░██║╚═╝██║░░██║░░██║
    ██║░░██║╚█████╔╝░░░██║░░░  ░░░░░░  ╚█████╔╝╚█████╔╝███████╗██████╔╝
    ╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░  ░░░░░░  ░╚════╝░░╚════╝░╚══════╝╚═════╝░
    """)
    return ""
def cheating():
    print("""
    ███╗░░██╗░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░████████╗██╗███╗░░██╗░██████╗░
    ████╗░██║██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░
    ██╔██╗██║██║░░██║  ██║░░╚═╝███████║█████╗░░███████║░░░██║░░░██║██╔██╗██║██║░░██╗░
    ██║╚████║██║░░██║  ██║░░██╗██╔══██║██╔══╝░░██╔══██║░░░██║░░░██║██║╚████║██║░░╚██╗
    ██║░╚███║╚█████╔╝  ╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝
    ╚═╝░░╚══╝░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░""")
    return ""
def win():
    print("""
    ██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
    ╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
    ░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
    ░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
    ░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
    ░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝""")
    return ""
def loss():
    print("""
    ██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗
    ╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝
    ░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░
    ░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░
    ░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗
    ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝""")
    return ""
def guess_count():  
    global times_guessed
    times_guessed += 1
def clear_guess_count():  
    global times_guessed
    times_guessed -= times_guessed
def games_played_comp1(): 
    global games_played_comp 
    games_played_comp += 1
def games_won_comp1(): 
    global games_won_comp 
    games_won_comp += 1
def games_played_user1(): 
    global games_played_user 
    games_played_user += 1
def games_won_user1(): 
    global games_won_user 
    games_won_user += 1
def loadingsoof():
    print("Loading (\033[3mhang in there 100% mark ↓\033[0m)")
    loading = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
    for char in loading:
        loadingvar = [.1,.3,.5,]
        Secs = random.choice(loadingvar)
        time.sleep(Secs)
        print(char, end='', flush=True)
    print("")
    return " "
def game_start(): 
    print("🇼 🇴 🇺 🇱 🇩  - 🇾 🇴 🇺  - 🇱 🇮 🇰 🇪  - 🇹 🇴  - 🇨 🇴 🇳 🇹 🇮 🇳 🇺 🇪")
    print("Enter: (S)tart or (Q)uit  ᶠᵒʳ ʳᵘˡᵉˢ ᵃⁿᵈ ᵍᵃᵐᵉ ᶦⁿᶠᵒʳᵐᵃᵗᶦᵒⁿ ᶦⁿᵖᵘᵗ (ᵢ) ")
    input_str = input("→")
    match(input_str.lower()):
    #first patter
        case 'start' | "s":
            print("\033[3mFetching game modes\033[0m")
            print(loadingsoof())
            print(game_mode())
            return ""
    #second patter
        case 'quit' | "q":
            print("Goodbye!")
            exit()
    #third patter
        case 'info' | "i":
            print(creds())
            exit()
    #default case - user did not enter input correctly
        case _:
            print("You did not enter a proper value")
            print(game_start())
    return ""
def game_mode(): 
    print("🇵 🇮 🇨 🇰  - 🇦  - 🇬 🇦 🇲 🇪  - 🇲 🇴 🇩 🇪 ")
    print("Enter: (C)omp or (U)ser")
    print("ᶜᵒᵐᵖ ⁼ ᴸᵉᵗ'ˢ ᵗʰᵉ ᶜᵒᵐᵖᵘᵗᵉʳ ᵍᵘᵉˢˢ ʸᵒᵘ'ʳᵉ ⁿᵘᵐᵇᵉʳ")
    print("ᵁˢᵉʳ ⁼ ᴸᵉᵗ'ˢ ʸᵒᵘ ᵍᵘᵉˢˢ ᵗʰᵉ ᶜᵒᵐᵖᵘᵗᵉʳ'ˢ ⁿᵘᵐᵇᵉʳ")
    input_str = input("→")
    match(input_str.lower()):
    #first patter
        case 'comp' | "c":
            print(comp_guessing())
    #second patter
        case 'user' | "u":
            print(user_guessing())
    #default case - user did not enter input correctly
        case _:
            print("You did not enter a proper value")
            print(game_mode())
    return ""
def play_again():
    print("🇵 🇱 🇦 🇾  🇦 🇬 🇦 🇮 🇳  ")
    print("Enter: (Y)es or (N)o")
    input_str = input("→")
    match(input_str.lower()):
    #first patter
        case 'yes' | "y":
            print(game_mode())
    #second patter
        case 'no' | "n":
            print(stats())
            exit()
    #default case - user did not enter input correctly
        case _:
            print("You did not enter a proper value")
            print(play_again())
    return ""
def creds():
    print("""This game was made by: Arius clark (oct 17th 24)
    \nRULES:
    \nThis is a simple high and low game using python.
    \nThis game give you 2 options to play.
    \nUser mode meaning that the user guesses the computuers number 
    \nfrom 1 - 100.
    \nComp mode meaning that the computer guesses you're number from 1 - 100
    \nHi Mr. Roeth my sigma""")
    print(game_start())
    return ""
def user_guessing():
    guesses_left = 10
    comp_number = random.randint(1, 100)
    print("Game ready!")
    print("Getting number between 1 and 100.")
    time.sleep(1)
    print("Okay! Ready!")
    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        try:
            guess = int(input("Guess the number → "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if guess < comp_number:
            print("Too low!")
            guess_count()
        elif guess > comp_number:
            print("Too high!")
            guess_count()
        else:
            print(f"Congratulations! You guessed the number!")
            print(win())
            games_won_user1()
            games_played_user()
            times_guessed_list.append(times_guessed)
            play_again()
            return " "
        guesses_left -= 1
    print(f"You ran out of guesses. The number was {comp_number}.")
    games_played_user1()
    times_guessed_list.append(times_guessed)
    print(loss())
    play_again()
    return " "
def comp_guessing():
    min = 1
    max = 100
    guesses_left = 10
    print("Game ready!")
    user_number = int(input("Pick a number →"))
    comp_number = random.randint(min,max)
    while guesses_left > 0:
        if comp_number != user_number:
                    print(f"Comp has {guesses_left} guesses left.")
                    print(comp_number)
                    print(f"Is this your number? {comp_number} \n(H)igher or (L)ower?")
                    response = input("->")
                    match(response.lower()):
                    #first patter
                            case 'higher' | "h":
                                if comp_number < user_number:
                                        min = comp_number
                                        guesses_left -= 1
                                else: 
                                        print(cheating())
                                        comp_number = random.randint(min,max)
                    #second patter
                            case 'lower' | "l":
                                if comp_number > user_number:
                                        max = comp_number
                                        guesses_left -= 1
                                else:
                                        print(cheating())
                                        comp_number = random.randint(min,max)
                    #default case - user did not enter input correctly
                            case _:
                                print("You did not enter a proper value")
                    comp_number = random.randint(min,max)
        else:
                print("your number is " + str(user_number))
                games_played_comp1()
                print(loss())
                print(play_again())
    else:
        print(f"Comp ran out of guesses")
        print(win())
        games_won_comp1()
        games_played_comp1()
        print(play_again())
    return " "
def stats():
    print("🇵 🇷 🇮 🇳 🇹  - 🇸 🇹 🇦 🇹 🇸 ")
    print("Enter: (Y)es or (N)o")
    input_str = input("→")
    match(input_str.lower()):
        case 'yes' | "y" :
            print("🇺 🇸 🇪 🇷  -  🇲 🇴 🇩 🇪 ")
            print(f"Average number of guesses: {statistics.mean(times_guessed_list)}")
            print(f"Fewest guesses: {min(times_guessed_list)}")
            print(f"Most guesses: {max(times_guessed_list)}")
            print(f"Games played: {games_played_user}")
            print(f"Mode win/loss: {games_won_user}/{games_played_user}")
            print("🇨 🇴 🇲 🇵  -  🇲 🇴 🇩 🇪 ")
            print(f"Games played: {games_played_comp}")
            print(f"Mode win/loss: {games_won_comp}/{games_played_comp}")
        case 'no' | "n":
            print("Goodbye!")
            exit()
        case _:
            print("You did not enter a proper value")
            print(stats())
    return " "
#Bottom statment(prints)
print(loadingsoof())
print(title())
print(game_start())
print(play_again())