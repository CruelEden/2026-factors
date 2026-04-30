# Statement generator
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("instruction", "-")

# Enter a number that is more than one but lower then 200
def num_check(question, low, high):

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

def get_factor(to_factor):

    factors_list = []

    stop = to_factor ** 0.5
    stop = int(stop)

    for item in range(1, stop + 1):

        if to_factor % item == 0:
            factors_list.append(item)

            partner = to_factor // item

            if partner not in factors_list:
                factors_list.append(partner)

    #output
    factors_list.sort()
    return factors_list

# Main routine here

(statement_generator("Factor Checker", "-"))

want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")
# Display instructions if needed
if want_instructions == "":
    instructions()
    print('''
instructions go here.
- instruction 1
- instruction 2
- etc   
    ''')


while True:

    comment = ""

    to_factor = num_check("Factor: ", 1, 200)

    if to_factor == "xxx":
        break

    elif to_factor != 1:
        all_factors = get_factor(to_factor)

    else:
        all_factors = ""
        comment = "One is unity it has only one factor. Itself :)"

    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    elif len(all_factors) % 2 == 1:
        comment = f"{all_factors} is a perfect square"

    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("we are done")


