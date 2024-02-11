#this code:
# 1. gets (and stores) the donors' full name, donation amount, and adds each donation to a total (runs x4).
# 2. returns the total and the donor who donated the most and the least (including the amount).

#coder's note:
#THIS CODE IS EDITED SPECIFICALLY TO DISPLAY CORRECTLY TO THE USER IN-BROWSER WITH THE AID OF PYSCRIPT. at this time (2/10/24), input is the ONLY way to display text! DO NOT JUDGE ME BY THIS CODE I AM WORKING W WHAT I GOT :praying_emoji:
#also i cut a ton of text just because

#make inputs appear in popup
from js import prompt
def input(p):
    return prompt(p)
__builtins__.input = input


#the code below has had the while True moved from the input to the last (which WAS a print statement, then the first input would repeat...)
def name():
    name = (input('What is your name (first and last)? '))
    if name.startswith(' ')!=True and name.endswith(' ')!=True and name.count(' ')==1:
        pass
    else:
        while(True):
            name = input('Please enter your first and last name with one space between.')
            if name.startswith(' ')!=True and name.endswith(' ')!=True and name.count(' ')==1:
                break

    cap = name.title()
    fullname = cap.split()

    return fullname

#takes the (already split) full name and returns the first name
def firstName(full):
    first = full[0]
    return first

#ask for amt and check validity, then submit. same while True and print() editing as the name() function above
def donate():
    money = ( (input('How much would you like to give? ')) )
    if money.isnumeric():
        pass
    else:
        while True:
            money = input('Please enter a numeric value.')
            if money.isnumeric():
                break

    return int(money)

#sum of all donations
def getTotal(donations):
    total = sum(donations)
    return total

#compares lists and gets the name that matches to index num
def getMaxName(money, names):
    x = max(money)
    placement = money.index(x)
    answer = names[placement]
    first = answer[0]
    return first

#compares lists and gets the name that matches to index num
def getMinName(money, names):
    x = min(money)
    i = money.index(x)
    answer = names[i]
    first = answer[0]
    return first


donors = ['Laura','Jenny','Kaleb','Paul']
donations = [0,0,0,0]
#user-facing init--for pyscript, user-facing starts at the for loop
print('Hi there! Thanks for choosing to donate to the Anti-Bluejay cause. Please answer the questions below.')

for i in range(0,4):
    donors[i] = name()
    donorFirst = firstName(donors[i])
    donations[i] = donate()
    total = getTotal(donations)

    #unable to display in browser prompt...
    print(f'Thanks for donating, {donorFirst}! You donated ${donations[i]}, bringing our total to ${total}.')


#devise total thru function
print()
print(f'Together, we have raised ${total}!')
print()

maxi = max(donations)
maxName = getMaxName(donations, donors)
print(f'{maxName} donated the most to our cause with ${maxi}!')

mini = min(donations)
minName = getMinName(donations, donors)
print(f'{minName} donated the least with ${mini}--but we appreciate ALL donations!')