"""
This program will display nine different units of conversion, ask the user to choose a unit to convert from, a unit to convert to, will take the unit measurement from 
the user, and provide a converstion for the user base on the options that were choosen. This program utilizes the "units.txt" file a as dictionary with unit 
conversions store in CSV format. The program opens and reads the selected items to convert from and to and provides the result as a float.
"""

""""
unitMenu
    Display all available users of coversion
    for the user to use in this program

grabUnit
    Opens the unit.txt 
    reads the file
    put data into a dictionary
    find the wanted unit
    converts it to a float
    returns the unit


doMath
    uses the grabUnit frunction with "unit.txt" dictionary find the unit to covert from
    uses grabUnit frunction with "unit.txt" dictionary find the unit to covert from
    returns the result as a float

main
    calls the unitMenu function
    unit_from input from user
    unit_to input from user
    amount_yard input from user to provide unit measure for conversion
    calls doMath function
    provides final conversion and displays it tot he user
"""

""""
unitMenu
    Display all available users of coversion
    for the user to use in this program

grabUnit
    Opens the unit.txt 
    reads the file
    put data into a dictionary
    find the wanted unit
    converts it to a float
    returns the unit


doMath
    uses the grabUnit frunction with "unit.txt" dictionary find the unit to covert from
    uses grabUnit frunction with "unit.txt" dictionary find the unit to covert from
    returns the result as a float

main
    calls the unitMenu function
    unit_from input from user
    unit_to input from user
    amount_yard input from user to provide unit measure for conversion
    calls doMath function
    provides final conversion and displays it tot he user
"""

import csv

def unitMenu():
    print("UNITS OF LENGTH")
    print(" ")
    print("inches   furlongs    yards")
    print("rods     miles       fathoms")
    print("meters   kilometers  feet")
    print("_____________________________")


def grabUnit(txt_file, unitWanted):
    read= open(txt_file, "r")
    chart = csv.reader(read)
    unitDict = {}
  
    for row in chart:
        unitDict[row[0]] = {'amount':row[1]}

    wanted = unitWanted
    stringUnit = (unitDict[wanted]['amount'])


    floatUnit = float(stringUnit) #convert string to float
    return floatUnit


def doMath(unitFrom, unitTo, amount):
    fromU = grabUnit('Units.txt',unitFrom)
    toU =  grabUnit('Units.txt',unitTo)
    length = float(amount)

    result = (fromU * length )/toU

    return result
    



def main():
    unitMenu()
    unit_from = input("Units to convert from: ")
    unit_to = input("Units to convert to: ")
    amount_yard = input("Enter length in " + unit_from +": ")
    length = doMath(unit_from,unit_to,amount_yard)
    print("Length in " + unit_to +": ", round(length, 4))

main()