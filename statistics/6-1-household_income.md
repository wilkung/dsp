[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>This exercise asks us to use provided income data and run some statistics on a sample of the data. It also asks us to see what happens to the statistics when the upper bound assumed changes.

**Results**
>10**6 upperbound

>median, mean, skewness, std: 51226.45, 74278.71, 4.95, 93946.93

>pearson skewness: 0.74 

>percent below mean: 0.66 

>10**7 upperbound

>median, mean, skewness, std: 51226.45, 124267.40, 11.60, 559608.50 :

>pearson skewness: 0.39 

>percent below mean: 0.86

**With a higher upper bound, median stays the same.  Mean increases, skewness increases and std increases.  Pearson skewness drops.  Percent below mean increases.

**Code**

```python
df = hinc.ReadData()
log_sample = InterpolateSample(df, log_upper=6.0)

sample = np.power(10, log_sample)
samplemedian = thinkstats2.Median(sample)
samplestd = sample.std()
sampleskewness = thinkstats2.Skewness(sample)
samplemean = sample.mean()
samplepearskewness = thinkstats2.PearsonMedianSkewness(sample)
samplecdf = thinkstats2.Cdf(sample)
   
print ('10**6 upperbound')   
print ('median, mean, skewness, std: %.2f, %.2f, %.2f, %.2f :' % (samplemedian, samplemean, sampleskewness, samplestd))
print ('pearson skewness: %.2f ' % (samplepearskewness))
print ('percent below mean: %.2f ' % (samplecdf[samplemean]))
    
log_sample = InterpolateSample(df, log_upper=7.0)

sample = np.power(10, log_sample)
samplemedian = thinkstats2.Median(sample)
samplestd = sample.std()
sampleskewness = thinkstats2.Skewness(sample)
samplemean = sample.mean()
samplepearskewness = thinkstats2.PearsonMedianSkewness(sample)
samplecdf = thinkstats2.Cdf(sample)
   
print ('10**7 upperbound')   
print ('median, mean, skewness, std: %.2f, %.2f, %.2f, %.2f :' % (samplemedian, samplemean, sampleskewness, samplestd))
print ('pearson skewness: %.2f ' % (samplepearskewness))
print ('percent below mean: %.2f ' % (samplecdf[samplemean]))

#10**6 upperbound
#median, mean, skewness, std: 51226.45, 74278.71, 4.95, 93946.93 :
#pearson skewness: 0.74 
#percent below mean: 0.66 
#10**7 upperbound
#median, mean, skewness, std: 51226.45, 124267.40, 11.60, 559608.50 :
#pearson skewness: 0.39 
#percent below mean: 0.86
```
