import pyautogui as auto
import time
import sys
import keyboard


print('Enter the message you want to spam')
message = input('=> ')
sign = input('Please enter an keyboard key to end the program: ')
print('Are you ready?')
cf = input('=> ')

if cf == 'no':
    sys.exit()

print('Be careful this is a powerfull tool and if you have a slow computer please exit')
print('exit Y/n?')
cm = input('=> ')

if cm == 'Y':
    sys.exit()
    


for x in range(5):
    print(x)
    time.sleep(1)
    
    
    

while True:
    auto.write(message)
    auto.press('enter')
    time.sleep(0.8)
   






    if keyboard.is_pressed(sign):
        sys.exit()
        
