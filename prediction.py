def printGuess(mileage):
    try:
        with open("thetaValues.txt", 'r') as weight:
            thetaValues = weight.read().split(',')
            t0 = float(thetaValues[0])
            t1 = float(thetaValues[1])
            prediction = t0 + (t1 * float(mileage))

            if (prediction > 0): print("Estimate price: ", prediction)
            else: print("I need more data.\nI don't want to give that car to my brother :)")
    except FileNotFoundError:
        print("File not found!")
    except IOError:
        print("File could not be opened!")

def guess():
    try:
        mil = float(input("Enter the milage value: "))
        if mil >= 0: printGuess(mil)
        else: print("Milage must be positive number!")
    except:
        print("Please enter a valid mileage value")

guess()
