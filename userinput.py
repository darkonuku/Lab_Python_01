print'EXERCISE 4'
print''

#prompting the user to enter his firstname and lastname
first_name = raw_input('Enter your first name: ')
last_name = raw_input('Enter your last name: ')

#prompting the user to enter the date of birth
print'Enter your date of birth: '
month = raw_input('\tMonth?: ')
day = raw_input('\tDay?')
year = raw_input('\tYear?')

#printing the name and date of birth of the user
print first_name, last_name, 'is born on', month, day + ',', year
