# Question: Create a program that once executed the programs prints Hello instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

# My answer:
import time
n = 0
while True:
    if n>3:
        print('End of the loop')
        break
    else:
        print('Hello')
        n+=1
        time.sleep(n)