print('Welcome to Python Pizza deliveries')
size = input('What size of Pizza do you want? S , M or L\n').lower()
add_pepperoni =input('Do yu want pepperoni? Y or N\n').lower()
extra_cheese = input('Do you want extra cheese? Y or N\n').lower()
if size == 's':
    bill = 15
    if add_pepperoni == 'y':
        bill+=2
        if extra_cheese == 'y':
            bill+=2
            print(f'Your total bill is ${bill}')
elif size == 'm':
    bill = 20
    if add_pepperoni == 'y':
        bill+=3
        if extra_cheese == 'y':
            bill+=3
            print(f'Your total bill is ${bill}')
           
elif size == 'l':
    bill = 25
    if add_pepperoni == 'y':
        bill+=3
        if extra_cheese == 'y':
            bill+=3 
            print(f'Your total bill is ${bill}')
else:
    print('enter correct size')