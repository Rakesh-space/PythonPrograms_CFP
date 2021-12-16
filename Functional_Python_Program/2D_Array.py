'''
Author: Rakesh Musale
Date: 2022-15-12 10:07:12
Last Modified by: Rakesh Musale
Last Modified time: 2022-15-12 10:07:12
Title : 2D-Array
'''

def Input2DArray(Number):
    """
    Description: we are taking Input2DArray as a function and passing Number as Parameter
    Parameter: Number
    Number as a input
    
    """

    for i in range(2):
        for j in range(2):
             print(Number,end=" ")
        print()

Number=input("Enter a Number : ")
Input2DArray(int(Number))
Input2DArray(float(Number))
Input2DArray(bool(Number))