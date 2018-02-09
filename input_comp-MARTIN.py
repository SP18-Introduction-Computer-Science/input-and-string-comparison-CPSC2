#!/usr/bin/python

#  Name: Michael Martin
#  Date: 2.8.2018
#  Course: CSPC-20 000
#  Assignment: Input and Comparisons

##In this assignment you are to read in a file from strings.txt. Create two list instances lets say a and b. Put all the even instances into a, and all the odd instances into b.
##
##Points :
##
##Listing all the elements from the even line  - 5 points
##
##Listing all the elements from the odd line - 5 points
##
##Remember you must you a loop to print out the element, and specify the set your elements are coming from.
##
##Go to the google classroom :  https://classroom.github.com/a/KBmG2A2n to get your repository
##
##the strings.txt file can be access through this link: https://www.dropbox.com/s/4en9ki36n8op673/strings.txt?dl=0
##
##This is due Thursday week 4, 11:59 pm - 10 pts
#  Links:
##https://classroom.github.com/a/KBmG2A2n
##
##https://www.dropbox.com/s/4en9ki36n8op673/strings.txt?dl=0

# global variables for reading in list, seperated by lines
master_list = []
list_a = []  #  list for odd number lines from string text
list_b = []  #  list for even number lines from string text

def main():

    # location of file:  D:\other colleges\lewis\CPSC-20000\strings.txt
    # string.txt: Hello(1), Goodbye(2), Farewell(3), Adios(4), Buenos(5), Noches(6)

    print("\tpre-processing before loops presented \n\tfor instructional purposes ONLY.\n")
    print("First, read thru file into one list:  ")
    with open("D:\other colleges\lewis\CPSC-20000\strings.txt") as f:
        lines = f.readlines()

    print(lines)
    
    even_list = []
    odd_list = []

    big_list = []

    count = 0
    # print("\n Append list Presented HERE:  \n")
    
    for x, y in enumerate(lines):
        big_list.append(y)
        # print(big_list[count])
        if count == 0 or count == 2 or count == 4 or count == 6:
            odd_list.append(y)
        else:
            even_list.append(y)
        count = count + 1
        # print("\n--NEXT--\n")

    print("Raw lists from file based on odd or even line number for each element:")
    print("EVEN LIST: 2,4,6,8,etc:  ",even_list)
    print("ODD LIST:  1,3,5,7, etc:  ",odd_list)
    print("\n\n\n")
    print("\n\nLoop thru Even and Odd List. \nFirst, odd:   ")    
    for x in odd_list:
        print(x,"\t-From Odd List\n")

    print("\n\tNow, even list:  ")
    for x in even_list:
        print(x,"\t-From Even List\n")

    print("\n LIST COMPLETE !! \n")

main()
