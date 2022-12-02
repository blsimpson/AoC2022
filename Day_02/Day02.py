def part_one(them, you):
    points = 0
    if them == 'A': #Rock
        if you == 'X': #Rock (+1)
            points += 4 #Draw (+3)
        if you == 'Y': #Paper (+2)
            points += 8 #Win (+6)
        if you == 'Z': #Scissors (+3)
            points += 3 #Loss (+0)
    
    elif them == 'B': # Paper
        if you == 'X': # Rock (+1)
            points += 1 # Loss (+0)
        if you == 'Y': # Paper (+2)
            points += 5 # Draw (+3)
        if you == 'Z': # Scissors (+3)
            points += 9 # Win (+6)    
   
    elif them == 'C': # Scissors
        if you == 'X': # Rock (+1)
            points += 7 # Win (+6)
        if you == 'Y': # Paper (+2)
            points += 2 # Loss (+0)
        if you == 'Z': # Scissors (+3)
            points += 6 # Draw (+3)
    return points

def part_two(them, you):
    points = 0
    if them == 'A': # Rock
        if you == 'X': # Need to lose (+0)
            points += 3 # Scissors (+3)
        if you == 'Y': # Need to draw (+3)
            points += 4 # Rock (+1)
        if you == 'Z': # Need to win (+6)
            points += 8 # Paper (+2)
 
    elif them == 'B': # Paper
        if you == 'X': # Need to lose (+0)
            points += 1 # Rock (+1)
        if you == 'Y': # Need to draw (+3)
            points += 5 # Paper (+2)
        if you == 'Z': # Need to win (+6)
            points += 9 # Scissors (+3)  
   
    elif them == 'C': # Scissors
        if you == 'X': # Need to lose (+0)
            points += 2 # Paper (+2)
        if you == 'Y': # Need to draw (+3)
            points += 6 # Scissors (+3)
        if you == 'Z': # Need to win (+6)
            points += 7 # Rock (+1)
    return points

part_1_score = 0
part_2_score = 0

with open('.\day_02\input.txt') as file:
    file = [line.strip() for line in file.readlines()]
    
    for round in file:
        part_1_score += part_one(round[0], round[2])
        part_2_score += part_two(round[0], round[2])
        
print(part_1_score)
print(part_2_score)