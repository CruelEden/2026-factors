# Ask user for integer and loop they
# enter a number that is more than one but lower then 200
def num_check(question):

    error = f"please enter number that is between 1 and 200 inclusive\n"
    while True:

        # ask the user for a number or exit
        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask for number
            response = int(response)

            # check that the number is more than 0 and less than or equal to 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine Goes Here
for item in range(0,20):
    integer = num_check("Integer: ")
    print(integer)
