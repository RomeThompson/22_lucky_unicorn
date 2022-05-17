 show_instructions = " "
 while show_instructions.lower() != "xxx":
        # Ask the user if they have played before
        show_instructions = input("Have you played this game before?")

        # If they say yes, output 'program continues'
        if show_instructions == "yes" or show_instructions == "y":
            print("program continues")

        elif show_instructions == "no" or show_instructions == "n":
              show_instructions = "yes"
            print("Program Continues")
        # If they say no, output 'display instructions'

        else:
        print("Error please enter yes or no")
