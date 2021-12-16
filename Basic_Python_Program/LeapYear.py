
'''
Author: Rakesh Musale
Date: 2022-15-12 02:40:12
Last Modified by: Rakesh Musale
Last Modified time: 2022-15-12 2.30:00:15
Title : Find out Leap Year
'''

year=int(input("Enter year to be checked:"))    #here input year from user

if(year%4==0 and year%100!=0 or year%400==0):   #here checking leap yere
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")