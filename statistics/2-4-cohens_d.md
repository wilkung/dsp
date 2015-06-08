[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)


Problem: Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. compute Cohen's d to quantify the difference between the groups

I solved using CohenEffectSize function comparing first to others for totalwgt_lb
> In [84]: thinkstats2.CohenEffectSize(first.totalwgt_lb, others.totalwgt_lb)  
> Out[84]: -0.088672927072601701  

My findings:
> In the case of weight, the Effect Size notes that first babies are lighter than others. Since the value is negative, the difference of the means tells us that first babies weight is lower than others babies weight.

How does it compare to the difference in pregnancy length?

I solved using CohenEffectSize function comparing first to others for prglngth
> In [85]: thinkstats2.CohenEffectSize(first.prglngth, others.prglngth)  
> Out[85]: 0.028879044654449841  

My findings:
> In the case of pregnancy length, the Effect Size tells is that first babies typically see a longer pregnancy length than others, but not by much since the Effect Size is quite small.

