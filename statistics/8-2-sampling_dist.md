[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

**Code:**
```python
from __future__ import print_function

import thinkstats2
import thinkplot
import matplotlib.pyplot as plt

import math
import random
import numpy as np


def RMSE(estimates, actual):
    """Computes the root mean squared error of a sequence of estimates.

    estimate: sequence of numbers
    actual: actual value

    returns: float RMSE
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)


def SimulateSample(lam=2, n=10, m=1000):
    """Sampling distribution of L as an estimator of exponential parameter.

    lam: parameter of an exponential distribution
    n: sample size
    m: number of iterations
    """

    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        lamhat = 1.0 / np.mean(xs)
        estimates.append(lamhat)

    stderr = RMSE(estimates, lam)
    print('standard error', stderr)
    print('mean of lamhat:', sum(estimates)/len(estimates))
    
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('90% confidence interval', ci)

    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Show()
    
    return stderr


def main():
    stderr10 = SimulateSample(n=10)
    stderr100 = SimulateSample(n=100)
    stderr1000 = SimulateSample(n=1000)
    stderr10000 = SimulateSample(n=10000)
    
    plt.plot([10,100,1000,10000],[stderr10,stderr100,stderr1000,stderr10000])
    plt.ylabel('stderr')
    plt.xlabel('n')
    plt.show()


if __name__ == '__main__':
    main()
```
