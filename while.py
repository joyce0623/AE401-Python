import random
guess=float(input("guess a number"))
ans=random.randint(1,10)
i=0
while i<1:
    if guess==ans:
        print('good')
        break
    elif guess!=ans:
        i=0
        print('gg')
        guess=float(input("guess again"))
        continue

