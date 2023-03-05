import random
dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)
sum = dice_1+dice_2
print('The sum of dice is: ', dice_1 ,'+',dice_2 ,'=', sum)

if sum == 7 or sum == 11:
    print('You win')
elif sum == 2 or sum == 3 or sum == 12:
    print('Casino win')
else:
    print('Your goal number is: ', sum)
    goal = sum
    sum = 1
    while sum != goal:
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        sum = dice_1+dice_2
        print('The sum of dice is: ', dice_1 ,'+',dice_2 ,'=', sum)
        if sum == 7:
            print('You lose')
            break
        elif sum == goal:
            print('You win')
            break

        