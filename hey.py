import numpy as np
import pandas as pd


r = {'one' : pd.Series([1., 2., 3.,], index=['a', 'b', 'c']),
	'two' : pd.Series([1., 2., 3., 4.,], index=['a', 'b', 'c', 'd'])
}

def frame():
	d = pd.DataFrame(r)
	return d

frame()
