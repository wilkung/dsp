[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

#####Problem: Use the NSFG respondent variable NUMKDHH to contruct the actual distribution for the number of children under 18 in the household. Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household. Plot the actual and biased distributions, and compute their means.

Using Chapter 1 information, I pulled the variable NUMKDHH values from the respondent data and then ran the actual PMF calculation on the dataset and plotted it.

> import chap01soln  
> resp = chap01soln.ReadFemResp()  
> kids = resp['numkdhh']
> pmf = thinkstats2.Pmf(kids)  
> thinkplot.Pmf(pmf, label='PMF')  
> thinkplot.Show(xlabel='# of Children', ylabel='PMF')  

> <img src="https://github.com/kevntao/dsp/blob/master/statistics/images/childrenPMF1.png?raw=true" width=400 height=300>  

Then I created a copy of pmf to calculated the biased PMF and plot it together with the actual PMF

> new_pmf = pmf.Copy(label='BiasPMF')  

> for x, p in pmf.Items():  
>     new_pmf.Mult(x, x)  

> new_pmf.Normalize()  
> biasedpmf = new_pmf  

> thinkplot.PrePlot(2)  
> thinkplot.Pmfs([pmf, biasedpmf])  
> thinkplot.Show(xlabel='# of Children', ylabel='PMF')  

> <img src="https://github.com/kevntao/dsp/blob/master/statistics/images/childrenPMF2.png?raw=true" width=400 height=300>  

Then using the Mean() function, I called to compute the mean value of each corresponding PMF

> In [27]: pmf.Mean()  
> Out[27]: 1.0242051550438309  

> In [28]: biasedpmf.Mean()  
> Out[28]: 2.4036791006642821  

