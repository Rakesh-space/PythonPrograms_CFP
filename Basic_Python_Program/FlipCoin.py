'''
Author: Rakesh Musale
Date: 2022-15-12 02:40:12
Last Modified by: Rakesh Musale
Last Modified time: 2022-15-12 2.30:00:15
Title :Flip Coin and print percentage of Heads and Tails
'''

import random

total_heads = 0
total_tails = 0
count = 0

while count < 0.5:

    coin = random.randint(0, 2)

    if coin == 0:
        print("Heads!\n")
        total_heads += 1
        count += 1

    elif coin == 1:
        print("Tails!\n")
        total_tails += 1
        count += 1

print("\nflipped heads", total_heads, "times ")
print("\nflipped tails", total_tails, "times ")