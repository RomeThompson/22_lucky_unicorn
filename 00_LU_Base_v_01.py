
# Functions go here

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()


        if response == "yes" or response == "y":
                response = "yes"
                return response

        elif response == "no" or response == "n":
                  response = "no"
                  return response

        else:
             print("Please answer yes/no")

played_before = yes_no("Have you played this game before?")

def instructions():
    print("**** How To Play ****")
    print()
    print("The rules of the game go here")
    print()
    return""

if played_before == "no":
    instructions()

print("Program continues")
