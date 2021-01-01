Finding the nth digit in a counting series
=================================
**Problem.** If the counting series "1234567891011121314151617181920212223..." is an infinitely long string of digits 0-9 that consists of the positive integers written in ascending order without any separators between the individual numbers, we can develop an algorithm which determines the nth digit in this sequence.

This mean, if we write the series "1234567891011121314151617181920212223" as a string in Python, `string[26]` will be returned as 8. This is the digit at the string's 26th index.
```python
>>string = "1234567891011121314151617181920212223"
```
```python 
>>string[26]
8
``` 

I work through a solution attempt [here](http://nbviewer.ipython.org/urls/raw.github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/master/Chapter2_MorePyMC/Ch2_MorePyMC_PyMC2.ipynb)

### [Read it online here](http://nbviewer.ipython.org/urls/raw.github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/master/Chapter2_MorePyMC/Ch2_MorePyMC_PyMC2.ipynb)
