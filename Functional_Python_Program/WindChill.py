'''
Author: Rakesh Musale
Date: 2022-16-12 10:38:09
Last Modified by: Rakesh Musale
Last Modified time: 2022-16-12 10:38:12
Title : WindChill.
'''
import math

try:
    #initlize the tempreture and speed of windchill.
    t_tempreture =int(input("Enter the Tempreture in Fahranheit: "))
    v_windspeed =int(input("Enter the Wind Speed in miles per hours: "))
    
    #formula for calculating the effective temp.
    effective_tempreture = (35.74+0.6215*t_tempreture+(0.4275*t_tempreture-35.75)*v_windspeed**0.16)

    # Condition for temp and speed.
    if(t_tempreture < 50 and(v_windspeed <120 or v_windspeed>3)):
        print(effective_tempreture)   
    else:
        print("Follow instructions while giving input of tempreture and speed ")  
except Exception as e:
    print("Enter int value" ,e)