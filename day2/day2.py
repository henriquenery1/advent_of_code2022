# TASK 1
# A - ROCK, B - PAPER, C - SCISSORS
# X - ROCK, Y - PAPER, Z - SCISSORS
# X - 1, Y - 2, Z - 3

SHAPE_SCORE_TASK_1 = {"X": 1,
                      "Y": 2,
                      "Z": 3}

DUEL_SCORE_TASK_1 = {"A X": 3,
                     "A Y": 6,
                     "A Z": 0,
                     "B X": 0,
                     "B Y": 3,
                     "B Z": 6,
                     "C X": 6,
                     "C Y": 0,
                     "C Z": 3
                     }

GAME_SCORE = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 4,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}


def solution1():
    file = open("input.txt", "r")
    lines = file.readlines()
    points = 0

    for i in lines:
        if i == "A X\n":
            points += 4
        elif i == "A Y\n":
            points += 8
        elif i == "A Z\n":
            points += 3
        elif i == "B X\n":
            points += 1
        elif i == "B Y\n":
            points += 5
        elif i == "B Z\n":
            points += 9
        elif i == "C X\n":
            points += 7
        elif i == "C Y\n":
            points += 2
        elif i == "C Z\n":
            points += 6
        elif i == "C X":
            points += 7   
            
    return print(points)  

solution1()
