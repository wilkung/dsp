[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

#####Problem: In order to join Blue Man Group, you have to be male and between 5'10" and 6'1" tall. What percentage of the US male population is in this range?

Setting up the distribution statistics for analysis required importing the scipy stats library with the mean and standard deviation given.

> import scipy.stats  
> mu = 178  
> sigma = 7.7  
> dist = scipy.stats.norm(loc=mu, scale=sigma)  

5'10" is approximately equivalent to 178 cm
6'1"-5'10" = 3", which is approximately equivalent to 7.7 cm
So in order to calculate the population in the desired range, I used the cdf calculation of the mean+stdev and subtracted the cdf calculation of the mean.  

> In [7]: dist.cdf(mu+sigma)-dist.cdf(mu)  
> Out[7]: 0.34134474606854259  

From the statistical calculation, approximately 34.13% of the US male population is within the eligible range.



