# THIS PROGRAM:
# 1. describes a cause to donate to.
# 2. gets (and store) the donors' full name, donation 
# amount, and adds each donation to a total (runs x4).
# 3. evaluates the total and return a specific answer based 
# on the amount reached.

#ask for full name and check validity, then submit
def name():
    while True:
        name = (input('What is your name (first and last)? '))
        if name.startswith(' ')!=True and name.endswith(' ')!=True and name.count(' ')==1:
            break
        else:
            print('Please enter your first and last name with one space between.')

    cap = name.title()
    fullname = cap.split()

    return fullname

#takes the (already split) full name and returns the first name
def firstName(full):
    first = full[0]
    return first

#ask for amt and check validity, then submit
def donate():
    while True:
        money = ( (input('How much would you like to give? ')) )
        if money.isnumeric():
            break
        else:
            print('Please enter a numeric value.')

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

#lots of text incoming
print('Hey guys, I\'m Olivia and I personally birdwatch all the time! I really love birdwatching--in fact, you\'re probably here because of my channel. Because of this I have a strong hate for bluejays.')
print('When my grandpa was young, my great-grandfather would go out with his shotgun and shoot bluejays. That is now illegal under US law. But we can still deter bluejays with more legal methods!')
print('Help me continue a family tradition so I can single-handedly eliminate the bluejay population in my backyard. Remember to subscribe to my YouTube channel for a LIVE FEED of my feeders and my Chickadee nest!')
#onto details ...
print()
print('If we can raise $15, I will install wind chimes near my feeders to deter bluejays, and each donator will get a small packet of birdseed!')
print('If we can raise $50, I will buy a fake owl AND each donators\' name will be listed at the end of my next three videos.')
print('By raising $100, we can install a new bluejay and squirrel proof feeder, complete with a new camera, and donators will get an exclusive installation video!')
print('If we raise $200, I will dance outside, rain or shine, to ward bluejays away on a YouTube livestream--AND each donator will be gifted a channel membership!')
print()

donors = ['Laura','Jenny','Kaleb','Paul']
donations = [0,0,0,0]
#user-facing init
print('Hi there! Thanks for choosing to donate to the Anti-Bluejay cause. Please answer the questions below.')

for i in range(0,4):
    donors[i] = name()
    donorFirst = firstName(donors[i])
    donations[i] = donate()
    total = getTotal(donations)

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

print()

#elseif tragedy
if total>=199:
    print('I can\'t believe it. We\'ve made it to the final tier. Be checking your email for your new channel membership and a voucher to get a birdseed packet FOR FREE! Be sure to catch me warding off bluejays on YouTube livestream next week, and look out for YOUR NAME at the end of my next three videos!')
    print()
    print('And don\'t forget that we have reached our other reward tiers on the way. With your help, I will be able to install a camera-equipped bluejay and squirrel proof feeder, wind chimes, and a fake owl! Be sure to catch an exclusive installation video soon.')
elif total>=100:
    print('Whoa! With your help, we have reached the third tier! We can install a new bluejay and squirrel proof feeder, complete with a new camera--and you\'ll get an exclusive installation video. Plus, I was able to get wind chimes and a fake owl with your help! And as for you, your name will be listed at the end of my next three videos, and check your email to get a birdseed packet FOR FREE!')
elif total>=50:
    print('Awesome! We\'ve made it to the second tier. With your help, I\'m now equipped with wind chimes and a fake owl to deter bluejays. Your name will also be listed at the end of my next three videos. Plus, remember check your email to get a birdseed packet FOR FREE!')
elif total>=15:
    print('Wow, we made it to the first tier! Now I can install wind chimes near my feeders to deter bluejays. Oh, and check your emails for a voucher to get a small packet of birdseed from my favorite supplier FOR FREE!')
else:
    print('Unfortunately, we haven\'t raised enough money to reach the lowest reward tier of $15 total...yet!')

print()
print('Let your friends know about the Anti-Bluejay Cause, and thank you again for donating!')