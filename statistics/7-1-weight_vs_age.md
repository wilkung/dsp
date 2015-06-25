[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>Solution in StatsEx6.py

>Using data from the NSFG, make a scatter plot of birth weight versus mother’s age. Plot percentiles of birth weight versus mother’s age. Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?

>Pearsons Correlation: 0.069

>Spearman Correlation: 0.095

**Code:**
```python
import numpy as np

import first
import thinkplot
import thinkstats2
    
all, first, nonfirst = first.MakeFrames()
all = all.dropna(subset=['agepreg', 'totalwgt_lb'])

ages = all.agepreg
weights = all.totalwgt_lb

all.plot(kind='scatter', x='agepreg', y='totalwgt_lb')

def BinnedPercentiles(df):
    """Bin the data by age and plot percentiles of weight for each bin.

    df: DataFrame
    """
    bins = np.arange(10, 48, 3)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)

    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)    
    thinkplot.Show()

BinnedPercentiles(all)
#

print('Pearsons Correlation: %.3f') % thinkstats2.Corr(ages, weights)
print('Spearman Correlation: %.3f') % thinkstats2.SpearmanCorr(ages, weights)
```
