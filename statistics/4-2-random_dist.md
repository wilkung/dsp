[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```
import random
%matplotlib inline
randnums=[(random.random()) for i in xrange(1000)]
print(randnums)

thous=[0.001 for i in xrange(1000)]
print (thous)

import matplotlib.pyplot as plt
plt.plot(randnums,thous,'ro')
plt.ylabel('frequency')
plt.axis([0, 1, 0, 0.0011])
plt.show()

#insert graph

import thinkstats2
import thinkplot
rn_cdf = thinkstats2.Cdf(randnums)
thinkplot.Cdf(rn_cdf)
thinkplot.Show(xlabel='Random Number 0 to 1', ylabel='CDF')

```

