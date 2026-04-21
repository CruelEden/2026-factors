# Ask user for integer and loop they
# enter a number that is more than one but lower then 200
def int_check(question, low, high):

    error = f"please enter number that is more then or equal to {low} or lower then {high}\n"
    while True:

        # ask the user for a number or exit
        response = input(question).lower()
        if response == "xxx":
            return response

        try:

            response = int(response)

            # check that the number is more than 0 and less than or equal to 200
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# gen header
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# displays instructions
def instructions():
    statement_generator("instruction", "-")

# main routine here
print(statement_generator("Factor Checker", "-"))

want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")
# display instructions if needed
if want_instructions == "":
    instructions()
    print('''
instructions go here.
- instruction 1
- instruction 2
- etc   
    ''')

# Main Routine Goes Here
for item in range(0,20):
    integer = int_check("Integer: ", 1, 200)
    print(integer)
    if integer == "xxx":
        break

print("we are done")


