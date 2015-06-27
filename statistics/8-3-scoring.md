# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

>**Results**

>This way of making an estimate is unbiased. 

>lambda=2

>Distribution of Simulated Goals per Game

>('RMSE', 1.409432509913121)

>('Mean Error of Goals in Game', -0.0041000000000000003)
 
>lambda=5

>('RMSE', 2.2405802819805407)

>('Mean Error of Goals in Game', -0.047199999999999999)

>As lam increases, sampling error increases as well.

>**Code**

```python

import thinkstats2
import thinkplot
import random

from estimation import RMSE, MeanError


def EstGoalinGame(lam):
    """Simulates a game and returns that game's simulated number of goals
    lam is goal scoring rate in goals per game
    """
    goals = 0
    t = 0
    while True:
        timebetweengoals = random.expovariate(lam)
        t = t + timebetweengoals
        if t > 1:
            break
        goals = goals + 1
    goalsscored = goals
    return goalsscored

def GoalsDist(lam=5, n=10000):

    goalsinmanygames = []
    for i in range(n):
        goalsingame = EstGoalinGame(lam)
        goalsinmanygames.append(goalsingame)

    print('Distribution of Simulated Goals per Game')
    print('RMSE', RMSE(goalsinmanygames, lam))
    print('Mean Error of Goals in Game', MeanError(goalsinmanygames, lam))

    pmf = thinkstats2.Pmf(goalsinmanygames)

    thinkplot.Hist(pmf)
    thinkplot.Show()
        
GoalsDist()
```
