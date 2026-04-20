import random
import time
import msvcrt


print ("""\033[32m 
       Robot Invaders
    \033[0m  """)
print("Welcome to Robot Invaders!")
print("You have 25 chances to shoot down the invading robots.")
print("When a robot appears, press the corresponding key before it disappears.")
print("Good luck!\n")
time.sleep(3)

score = 0

def robot_invaders_game():
    
     

    #loop that gives 25 tries to the player to shoot down the robot invaders
    for tries in range(25):
        
        #random time delay betwee2 and 5 seconds
        time_delay = random.uniform(2, 5)
        time.sleep(time_delay)
        
        #selects numbers for across and down
        across = random.randint(1, 20)
        down = random.randint(1, 15)
        
        #choose random keyboard key
        key = random.choice('abcdefghijklmnopqrstuvwxyz')
        
        #moves cursor across and down then prints the key to be pressed
        print(f"\033[{down};{across}H\033[31m{key}\033[0m")
        
        #checks if a key is pressed within the time delay and if it matches the key displayed increase the score and print the key in green, if not print the text "missed" and continue the loop
        start_time = time.time()
        while time.time() - start_time < time_delay:
            if msvcrt.kbhit():
                pressed_key = msvcrt.getch().decode('utf-8').lower()
                if pressed_key == key:
                    score += 1
                    print(f"\033[{down};{across}H\033[32m{key}\033[0m")
                    break
        else:
            print(f"\033[{down};{across}H\033[31m missed \033[0m")

#after the loop ends, print the final score
print(f"\nYour final score is: {score} out of 25")


if __name__ == "__main__":
    robot_invaders_game()         