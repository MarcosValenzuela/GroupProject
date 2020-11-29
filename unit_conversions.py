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
