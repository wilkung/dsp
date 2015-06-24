[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

> *Need to insert 2 plots*

>Using the data, we plot the actual and biased distribution of household size.  Then we compute the actual mean and biased mean.  I compute the actual mean to be 1.02 and the biased mean to be 2.4.  This bias arises because there is an inherent bias to ask more people who comes from larger households since there are more people coming from larger households than smaller households.

>My solution in chap03ex.ipynb
 
>Code:

```
%matplotlib inline

import chap01soln
resp = chap01soln.ReadFemResp()

import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')

pmf

import thinkplot
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,pmf])
thinkplot.Show(xlabel='household size', ylabel='PMF')

# insert plot

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
    
biased_pmf = BiasPmf(pmf, label='observed')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='household size', ylabel='PMF')

#insert plot

print('mean of actual pmf:', pmf.Mean())

#('mean of actual pmf:', 1.0242051550438309)

print('mean of biased pmf', biased_pmf.Mean())

#('mean of biased pmf', 2.4036791006642821)
```
