# Sampling library - Bootstrap and Deltamethod
Bootstrap method and Delta method implementation in Python (Some method would be added)

I want to refactor this code but this code has not been changed for a long time...  
I remember this code was written in Summer 2013.  
I want to rewrite this code for Python 3.x.  

## How to use

### Environment

Python2.7

## How to install this library

```
$pip install git+https://github.com/ksnt/Bootstrap-and-Deltamethod.git
```

### Delta Method

$python # Go into Python!
```sh
>>> import sampling
>>> import numpy as np
>>> n = 1000 # The number of sampling
>>> S = 1000
>>> dm_result = [] # Result of Delta method
>>> for s in range(int(S)):
...     x = np.random.uniform(0,1,n)
...     dm_result.append(sampling.delta(x,n))
... 
>>> print("Result of Delta-method is : %f" % (np.sum(dm_result)/S) )
Result of Delta-method is : 0.953000
```

### Bootstrap Method
$python # Go into Python!
```sh
>>> import sampling
>>> import numpy as np
>>> n = 1000 # The number of sampling
>>> S = 1000
>>> bs_result = [] # Result of Bootstrap method
>>> for s in range(int(S)):
...     x = np.random.uniform(0,1,n)
...     bs_result.append(sampling.boot(x,n))
... 
>>> print("Result of Delta-method is : %f" % (np.sum(bs_result)/S) )
```

## Overview of the Delta Method

PDF file would be added.  

## Overview of the Bootstrap Method

[Algorithm of Bootstrap Method](https://github.com/ksnt/Bootstrap-and-Deltamethod/blob/master/doc/bootstrap.pdf)

## Result

|    n |     10 |        100|       1000|
|-----------|------------|------------|------------|
|Delta      |    0.928000|    0.948000| 0.955000   |
|Bootstrap  |    0.918000|    0.947000| 0.951000   |

## Reference
You can easily find useful information about Bootstrapping and Delta method from sites such as links below. I recommend Efron's articles and books regarding Bootstrap such as **"The Jackknife,the Bootstrap and Other Resampling Plans", "An Introduction to the Bootstrap" by Bradley Efron**. As for Delta method, I think some books on econometrics and mathematical statistics are useful; for example, you can find useful information in a manuscript titled **["Econometrics" by Bruce E. Hansen](http://www.ssc.wisc.edu/~bhansen/econometrics/)**. This article is free and seems praised as a great book by econometricians.  

Bootstrap method: https://en.wikipedia.org/wiki/Bootstrapping_(statistics)  
Delta method: https://en.wikipedia.org/wiki/Delta_method
