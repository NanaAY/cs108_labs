''' A program for dictionary practice
Lab 03
@author: Toby Sterk (ths6)
@author: Nana Osei (na29)
'''

# Create a dictionary with desired values
scoreDict = {"Joe":10,"Tom":23,"Barb":13,"Sue":19,"Sally":12}

# Print an expression that computes Barb's score
print(scoreDict["Barb"])

# Update the score for Sally to be 13
scoreDict["Sally"] = 13

# Delete Tom
del scoreDict["Tom"]

# Print resulting dictionary
print(scoreDict)