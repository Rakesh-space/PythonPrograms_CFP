'''
Author: Rakesh Musale
Date: 2022-15-12 02:40:12
Last Modified by: Rakesh Musale
Last Modified time: 2022-15-12 2.30:00:15
Title : Find out Prime Factorial Number
'''
n = 20 
i = 2

while i * i < n:       #4<20 true
    while n%i == 0:     #20%4=0
        n = n / i       #5 is prime
    i = i + 1       #i increment

print(n)