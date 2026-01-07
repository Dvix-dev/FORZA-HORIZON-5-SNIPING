# Imports for keyboard inputs, timed delays and a custom function
import keyboard
import time
import os

# Function to clear the terminal
def clear():
    command = 'cls'
    os.system(command)

clear()
timer = (0.0) # Seconds
counter = 0 # Times sniped
start = 1
# This will initiate the script
if start == 1:
    while True:
        # Prints the explanation for using the script
        clear()
        print(' ----------------------------------------------------------------------')
        print('|                     Python FH5 Sniping Script                        |')
        print('|                                                                      |')
        print('|   1- First select the car you want and the potential max buyout      |')
        print('|   2- Make sure to focus the FH5 window when the countdown starts     |')
        print('|   3- Second monitor highly recommended because when you want to      |')
        print('|      close the script you have to just force close the window        |')
        print('|      (Put the game in windowed mode and put the script over it       |')
        print('|       if you don\'t have a second monitor)                            |')
        print('|   4- It will start counting down from 5 once you start the script.   |')
        print('|      \'y\' = yes | \'n\' = no                                            |')
        print('|                                                                      |')
        print('|      GOOD LUCK SNIPING!                                              |')
        print(' ----------------------------------------------------------------------')
        # Asks if user wants to start sniping 
        a = str(input('\nDo you want to start the script? y/n: '))
        # If user input equals 'n' it will close the program immediately
        if a == 'n':
            break
        # If user input from -a- equals 'y' it will start counting down from 5 and will start sniping
        elif a == 'y':
            clear()
            for i in range(5, -1, -1):        
                print('!!FOCUS WINDOW!!\nSniping in: ')        
                print(str(i) + ' seconds')                
                time.sleep(1)
                clear()
            # The keyboard inputs and timings
            while True:
                counter = counter + 1
                timer = timer + (2.33)
                minuteCounter = timer / 60
                clear()                                
                print('Intentos: ' + str(counter) + ' veces')  
                print(str(round(timer, 1)) + ' segundos (' + str(round(minuteCounter, 1)) + ' minutos)')                              
                keyboard.press_and_release('Enter')
                # *
                time.sleep(0.25)
                keyboard.press_and_release('Enter')
                # *
                time.sleep(0.78)
                keyboard.press_and_release('y')                
                time.sleep(0.25)      
                keyboard.press_and_release('down')                
                time.sleep(0.1)
                keyboard.press_and_release('Enter')
                # *
                time.sleep(0.2)    
                keyboard.press_and_release('Enter')                   
                keyboard.press_and_release('Escape') 
                time.sleep(0.75) 
                  
        # If input from -a- doesn't equal 'y' or 'n' it will start a loop where the user will be asked to restart or exit the program                                    
        else:            
            while True:
                clear()
                # Asks user for input to restart or exit the program
                restart = input('You didn\'t press \'y\' to start the script, do you want to restart? y/n : ')
                # If user input from -restart- 'y' it will go loop back to -a-
                if restart == 'y':
                    break 
                # If input from -restart- equals 'n' it will close the program
                elif restart == 'n':
                    exit() 
                # If the user does not input 'y' or 'n' it will loop back to -restart-          
                else:
                    continue

clear()    
