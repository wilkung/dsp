[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>Solution is in chap05ex

>In order to calculate the percentage of population the population that can join the Blue Man Group, we convert the min and max height to cms.  Then we convert that to standard deviations from mean.  Finally using the SD from mean, we use the CDF function to calculate the population to the left of the SD from mean.  The difference is the percentage of male population that can join the BMG. This is approximately 51%.

>Code:

```
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

dist.mean(), dist.std()

dist.cdf(mu-sigma)

# 1 inch = 2.54cm
lowincm = ((5*12)+10)*2.54
hiincm = ((6*12)+1)*2.54
print (lowincm,hiincm)

#(177.8, 185.42000000000002)

lowsd, hisd = (177.8-178)/sigma, (185.42-178)/sigma
print (lowsd,hisd)
#(-0.025974025974024498, 0.963636363636362)

from scipy.stats import norm
low=norm.cdf(lowsd)
hi=norm.cdf(hiincm)
print (hi-low)*100
#51.0360972135
