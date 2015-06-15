[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

#####Problem: Generate 1000 numbers from random.random and plot PMF & CDF. Is the distribution uniform?

I solved by using a loop counter to append randomly generated numbers to a list
> for i in range(0,1000):  
>     storedvals.append(random.random())  

I then graphed the PMF and CDF of the randomly generated list of values
> pmf = thinkstats2.Pmf(storedvals)  
> thinkplot.Pmf(pmf, label='PMF')  
> thinkplot.Show(xlabel='random', ylabel='PMF')  
> <img src="https://github.com/kevntao/dsp/blob/master/statistics/images/PMF.png?raw=true" width=400 height=300>  

> cdf = thinkstats2.Cdf(storedvals)  
> thinkplot.Cdf(cdf, label='CDF')  
> thinkplot.Show(xlabel='random', ylabel='CDF')  
> <img src="https://github.com/kevntao/dsp/blob/master/statistics/images/CDF.png?raw=true" width=400 height=300>  

My Findings:
> After generating 1000 random numbers, the CDF showed a positive linear slope, which tells me that the stored list of numbers is indeed uniform.
