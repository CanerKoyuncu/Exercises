import random

def numberGuessinggame():

    minimumNumber = int(input("Minimum number is: "))
    maximumNumber = int(input("Maximum number is: "))

    targetNumber = random.randint(minimumNumber,maximumNumber)
    counter = 1
    flag = True

    while flag:
        middle =(minimumNumber + maximumNumber)//2
        
        if targetNumber == middle:
            print("The number is {}, we found in {} steps".format(targetNumber,counter))
            flag = False

        elif targetNumber < middle:
            maximumNumber = middle
            print("My guess is {}".format(middle))
            print("Number is higher than")
            counter += 1

        elif targetNumber > middle:
            minimumNumber = middle
            print("My guess is {}".format(middle))
            print("Number is lower than")
            counter += 1

if __name__ == '__main__':
    numberGuessinggame()