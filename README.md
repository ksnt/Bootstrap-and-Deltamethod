# Sampling library - Bootstrap and Deltamethod
Bootstrap method and Delta method implementation in Python (Some method would be added)

## How to use

### Environment

Python2.7

## How to install this library

### Linux(Ubuntu)
```
$sudo pip install git+https://github.com/ksnt/Bootstrap-and-Deltamethod.git
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

TBA  

## Overview of the Bootstrap Method

TBA  

## Result

|    n |     10 |        100|       1000|
|-----------|------------|------------|------------|
|Delta      |    0.928000|    0.948000| 0.955000   |
|Bootstrap  |    0.918000|    0.947000| 0.951000   |

## Reference
You can easily find useful information about Bootstrapping and Delta method from sites such as links below. I recommend Efron's articles and books regarding Bootstrap such as **"The Jackknife,the Bootstrap and Other Resampling Plans" by Bradley Efron**. As for Delta method, I think some books on econometrics and mathematical statistics are useful; for example, you can find in a manuscript titled **["Econometrics" by Bruce E. Hansen](http://www.ssc.wisc.edu/~bhansen/econometrics/)**. The article is free.

Bootstrap method: https://en.wikipedia.org/wiki/Bootstrapping_(statistics) <br>
Delta method: https://en.wikipedia.org/wiki/Delta_method
