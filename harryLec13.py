day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
# match case using the if condition
num = 15

match num:
    case n if n > 0:
        print("Positive number")
    case n if n < 0:
        print("Negative number")
    case _:
        print("Zero")
# match num: checks the value of num.

# case n if n > 0: matches the value and checks whether n > 0.

# case n if n < 0: checks whether the number is negative.

# case _: handles the remaining case, which is zero here.
# Bro 😎, in Python match-case, we use | (pipe symbol) to match multiple values in a single case. It means OR.

# Example
day = 1

match day:
    case 1 | 2 | 3:
        print("Day is 1, 2, or 3")
    case _:
        print("Other day")