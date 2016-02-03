IPython 3.2.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
[TerminalIPythonApp] WARNING | Error in loading extension: kernmagic
Check your config files in /Users/danielmsheehan/.ipython/profile_default
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/IPython/core/shellapp.py", line 266, in init_extensions
    self.shell.extension_manager.load_extension(ext)
  File "/Library/Python/2.7/site-packages/IPython/core/extensions.py", line 85, in load_extension
    __import__(module_str)
ImportError: No module named kernmagic

In [1]: %paste
from scipy.io import loadmat
ocr = loadmat('ocr.mat')

import matplotlib.pyplot as plt
from matplotlib import cm

## -- End pasted text --

In [2]: ocr
Out[2]: 
{'__globals__': [],
 '__header__': 'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Thu Jan 22 15:05:26 2015',
 '__version__': '1.0',
 'data': array([[0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0],
        ..., 
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0]], dtype=uint8),
 'labels': array([[5],
        [0],
        [4],
        ..., 
        [5],
        [6],
        [8]], dtype=uint8),
 'testdata': array([[0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0],
        ..., 
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0]], dtype=uint8),
 'testlabels': array([[7],
        [2],
        [1],
        ..., 
        [4],
        [5],
        [6]], dtype=uint8)}

In [3]: ocr.keys()
Out[3]: 
['testlabels',
 'data',
 'labels',
 '__header__',
 '__globals__',
 '__version__',
 'testdata']

In [4]: ocr['data']
Out[4]: 
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       ..., 
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0]], dtype=uint8)

In [5]: ocr['data'].shape
Out[5]: (60000, 784)

In [6]: 28*28
Out[6]: 784

In [7]: max(ocr['data'])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-7-8ee6d92b498a> in <module>()
----> 1 max(ocr['data'])

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

In [8]: np.max(ocr['data'])