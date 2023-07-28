def printGuess(mileage):
    try:
        with open("thetaValues.txt", 'r') as weight:
            thetaValues = weight.read().split(',')
            t0 = float(thetaValues[0])
            t1 = float(thetaValues[1])

            print("Estimate price: ", (t0 + (t1 * float(mileage))))
    except FileNotFoundError:
        print("File not found!")
    except IOError:
        print("File could not be opened!")

def guess():
    try:
        mil = float(input("Enter the milage value: "))
        printGuess(mil)
    except:
        print("Please enter a valid mileage value")

guess()
