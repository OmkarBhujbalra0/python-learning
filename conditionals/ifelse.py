# if-else

age = 18

if age < 18:
    print("Not Eligible")
else:
    print("Eligible.")

#  if-elif-else

a = 34
b = 8
c = 5

if (a > b) and (b > c):
    print(f"{a} is highest of them all")
elif (b > a) and (b > c):
    print(f"{b} is highest of them all.")
else:
    print(f"{c} is highest of them all.")

# if statement

age = 18

if age >= 18:
    print("You are Eligible for Driving License.")

# Nested if-else

course = 'computer'
year = 'first'

if year == 'first':
    if course == 'computer':
        print("First Year Student of Computer Engineering")
    elif course == 'it':
        print("First Year Student of IT")
    else:
        print("First Year Student")
elif year == 'second':
    if course == 'computer':
        print("Second Year Student of Computer Engineering")
    elif course == 'it':
        print("Second Year Student of IT")
    else:
        print("Second Year Student")
elif year == 'third':
    if course == 'computer':
        print("Third Year Student of Computer Engineering")
    elif course == 'it':
        print("Third Year Student of IT")
    else:
        print("Third Year Student")
elif (year == 'final') or (year == 'fourth'):
    if course == 'computer':
        print("Final Year Student of Computer Engineering")
    elif course == 'it':
        print("Final Year Student of IT")
    else:
        print("Final Year Student")

# One line Conditional Statement

print("Eligible") if age > 18 else print("Not Eligible")

gender = "Male"
result = "Man" if gender == "Male" else "Female"
print(result)

# Match Case

subject = "Internet Programming" 

match subject:
    case "Computer Networks" : 
        print("Subject name is Computer Networks")
    case "Internet Programming" : 
        print("Subject name is Internet Programming")
    case "Software Engineering" : 
        print("Subject name is Software Engineering")
    case _ : 
        print("Invalid Subject Name")

# Conditionals with input function

age = input("Enter your age:")

if age >= 18:
    print('Eligible.')
else:
    print('Not Eligible.')