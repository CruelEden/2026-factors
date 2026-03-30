# Ask user for integer and loop they
# enter a number that is more than one but lower then 200
def int_check(question, low, high):

    error = f"please enter number that is more then or equal to {low} or higher then {high}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than one
            if exit == "xxx" or 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here
for item in range(0,20):
    integer = int_check("Integer: ", 1, 200)
    print(integer)

    print()

    if exit == "xxx":
        break