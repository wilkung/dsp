[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>solution is in StatsEx7.py

>Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.
Repeat the experiment with a few different values of n and make a plot of standard error versus n.

>Plot of sampling distrution of Estimate L:

[insert plot]

>For lambda = 2 and sample size of 10 with 1000 iteration, stderr = 0.76 and 90% CI is [1.26, 3,58]:

**Results of sampling of exponential distribution:**

>n=10
>standard error 0.76351438241
>mean of lamhat: 2.13857883473
>90% confidence interval (1.2562848678552347, 3.5845545120660773)

>n=100
>standard error 0.200277623043
>mean of lamhat: 2.00894674687
>90% confidence interval (1.6967436312201396, 2.3496401715717172)

>n=1000
>standard error 0.0602587918967
>mean of lamhat: 1.99990213082
>90% confidence interval (1.9053269963264716, 2.1034847916420327)

>n=10000
>standard error 0.0206176694726
>mean of lamhat: 1.99977525212
>90% confidence interval (1.9659118554250645, 2.032861426132309)

>As the sample size increases, stderr decreases as expected:

>[insert plot]

**Code:**
```python
from __future__ import print_function

import thinkstats2
import thinkplot
import matplotlib.pyplot as plt

import math
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
