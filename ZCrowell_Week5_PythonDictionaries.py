# ZCrowell_Week5_Dictionaries.py
# 
# Iterates through dictionary once, prints list of players and the points   
#   they scored and, the total number of points they scored, and the name
#   of the highest scorer on the team. 
#  
# Last edited December 16, 2020 by Zane Crowell
# CSCI 111, Section 002

# declare variables
topScore = 0
topPlayer = ""
scoreSum = 0

# declare dictionary 
playersAndPoints ={
    "Harris": 24, "Butler" : 11,
    "Embiid" : 31, "Simmons" : 15,
    "Reddick" : 9, "Scott" : 8,
    "Ennis" : 7, "Marjanovic" : 4,
    "Bolden" : 1, "McConnell" : 2 }

print("Player:", "|", "Score:")
print()

# loop that iterates through dictionary
for player, score in playersAndPoints.items():
    print(player, " - ", score)
    if score > topScore:    # find highest score without built-in method
        topScore = score
    topPlayer = max(playersAndPoints, key = playersAndPoints.get)   # get key that corresponds with highest score value
    scoreSum = sum(playersAndPoints.values())   # sum the scores

# print results
print() 
print("The highest score was", topScore, "points by", topPlayer)
print()
print("The total number of points scored is: ", scoreSum)       













