#GUESSING GAME 
"""
Player-1 picks a number X and Player-2 has to guess that number within N = 3 tries. For each 
wrong guess by Player-2, the program prints “Wrong, N-1 Chance(s) Left!” If Player-2
successfully guesses the number, the program prints “Right, Player-2 wins!” and stops 
allowing further tries (if any left). Otherwise after the completion of N = 3 wrong tries, the 
program prints “Player-1 wins!” and halts.
"""


a = int(input())
b1 = int(input())
N = 3
if a == b1 :
    print("Right, Player-2 wins!")
elif a != b1 :
    N -= 1 
    print(f"Wrong, {N} Chance(s) Left!")
    b2 = int(input())
    if a == b2 :
        print(f"Right, Player-2 wins!")
    elif a != b2 :
        N -= 1
        print(f"Wrong, {N} Chance(s) Left!")
        b3 = int(input())
        if a == b3 :
            print(f"Right, Player-2 wins!")
        elif a != b3 :
            N -= 1
            print(f"Wrong, {N} Chance(s) Left!\nPlayer-1 wins!")
        
