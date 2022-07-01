import random

trials = 0
total_trials = int(input("Zadejte počet pokusů: "))
dice_side_occurence = [0 for x in range(6)]

while trials <= total_trials:
    number = random.randint(1, 6)
    dice_side_occurence[number - 1] += 1
    trials += 1

for number_of_occurences in dice_side_occurence:
    print(f"Počet výskytů: {number_of_occurences}, " + 
    f"Poměr v %: {100*(number_of_occurences/total_trials)}")