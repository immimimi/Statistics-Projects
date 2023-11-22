import numpy as np
import random as rm

#weather prediction markov chain 

#markov chain to predict what activity a person will do next
#three possible weather types

#R rainy , S sunny, C cloudy 

#activities
states = ["Sleep", "Ice Cream", "Run"]
#simplify our transition names,
transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

#

transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]


if (sum(transitionMatrix[0]) + sum(transitionMatrix[1]) +sum(transitionMatrix[0])) ==3: #checking if all is good (probabilites have to add to one)
  print('good')
else: print('Bad')

# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    # Choose the starting state
    activityToday = "Sleep"
    print("Start state: " + activityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [activityToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Run"
                activityList.append("Run")
            else:
                prob = prob * 0.2
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "RR":
              prob = prob * 0.6
              activityList.append("Run")
              pass
            elif change == "RS":
              prob = prob * 0.1
              activityToday = "Sleep"
              activityList.appemd("Sleep")
            else:
              prop = prob * 0.3
              activityToday = "Ice Cream"
              activityList.append("Ice Cream")
        elif activityToday == "Ice Cream":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "II":
              prob = prob * 0.1
              pass
            elif change == "IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
              prob = prob * 0.7
              activityToday = "Run"
              activityList.append("Run")
        i += 1
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

# Function that forecasts the possible state for the next 2 days
activity_forecast(2)
