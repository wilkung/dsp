[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

**Need to insert one chart*

>The problem asks us to analyze data to determine if there is a difference in birth weight of first borns versus non first borns.

>We can see if there is a difference by averaging birth weight for first, second, third borns, and so on.  To visually see the averages, I plot the averages by birth order in a bar chart.  

>[insert bar chart]

>Initially, we see a pattern of inreasing weight with higher birth order, so first borns tend to be lighter at birth.  To see if the difference between first borns and non first borns are statistically difference, I calculate cohen's d between first born birth weight and non first born birth weights.

>Cohen's d was calculated to be -0.0690 indicating that the birth weight difference is very small.



>Code:
```python

import nsfg
import matplotlib.pyplot as plt
from numpy import mean, std
from math import sqrt

df = nsfg.ReadFemPreg()
print df
groupbypregordr = df.groupby('pregordr')
groupbypregordr['totalwgt_lb'].describe()
groupbypregordrmean = groupbypregordr['totalwgt_lb'].mean()

plt.figure()
groupbypregordrmean.plot(kind='bar'); plt.axhline(0, color='k')


def cohen_d(x,y):
    return (mean(x) - mean(y)) / sqrt((std(x, ddof = 1) ** 2 + std(y, ddof=1) ** 2) / 2.0)

firstbirthlbs =  df[ (df['pregordr'] == 1) ]['totalwgt_lb']
nonfirstbirthlbs =  df[ (df['pregordr'] != 1) ]['totalwgt_lb']

firstbirthlbslist = firstbirthlbs.tolist()
nonfirstbirthlbslist = nonfirstbirthlbs.tolist()

firstbirthlbslistclean = [x for x in firstbirthlbslist if str(x) != 'nan']
nonfirstbirthlbslistclean = [x for x in nonfirstbirthlbslist if str(x) != 'nan']

print('Cohen_d: %.4f' % cohen_d(firstbirthlbslistclean, nonfirstbirthlbslistclean))
```
