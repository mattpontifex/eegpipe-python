eegpipe
==============

What is this?
------------
This python package mimics the functionalities of EEGLAB/ERPLAB.

Installation
------------
To use this package, run the following commands from the terminal:
```python
    pip install git+git://github.com/mattpontifex/eegpipe.git
    
    import eegpipe
    eegpipe.version()
```

Function List
------------
These functions simplify common utilities or mimic parts of EEGLAB.

* **eeglabstructure**: Python class that mimics the structure of the EEG variable in EEGLAB.
```python
    EEG = eegpipe.eeglabstructure()
```

* **checkdefaultsettings**: Function that will check an input against a list and return the value from the list. 
If False is input then it returns the first element from the list as the default option.
```python
    textvalue = 'APPLES'
    textvalue = eegpipe.checkdefaultsettings(textvalue, ['oranges', 'bananas', 'apples'])
    # textvalue returns 'apples'
```

* **smooth**: Function that will smooth the data using a window with requested size. The approaches are: 
'hanning' (default), 'flat', 'hamming', 'bartlett', 'blackman'.
```python
    t = numpy.arange(-3,3,numpy.divide(1.0,256.0))
    x = numpy.sin(t) + numpy.multiply(numpy.random.randn(len(t)), 0.1)
    y = eegpipe.smooth(x, span=40, window='hanning')
    eegpipe.plot(x)
    eegpipe.plot(y)
```

* **closestidx**: Function that returns the index of the closest value in a list. 
Helpful for requesting times when the sampling rate may not perfectly align with the requested value.
```python
    numericlist = numpy.arange(0.98,1.05,numpy.divide(1.0,256.0))
    value = 1.0
    index = eegpipe.closestidx(numericlist, value)
    # index returns 5
```

* **msdatefromref**: Function that returns the number of milliseconds between two date values.
```python
    basedate = pandas.to_datetime('2020-12-29 00:00:20')
    comparisondate = pandas.to_datetime('2020-12-29 00:01:20')
    timevalue = eegpipe.msdatefromref(basedate, comparisondate)
    # timevalue returns 60000.0
```

* **excel_date**: Function that returns the date in a numeric format like in ms Excel.
```python
    basedate = pandas.to_datetime('2020-12-29 00:00:20')
    timevalue = eegpipe.excel_date(basedate)
    # timevalue returns 44194.000231481485
```

* **minmax_scaling**: Function that rescales a vector to have a given minimum and maximimum value.
```python
    scaledvector = eegpipe.minmax_scaling(vector, columns=0, min_val= -10, max_val= 10))
```


Data Read in Function List
------------
* **readUnicornBlack**: Function to read data created by Python Collect from the g.tec Unicorn Hybrid Black.
```python
    EEG = eegpipe.readUnicornBlack('file.csv')
```

* **readEyeTribe**: Function to read data created by Python Collect from the EyeTribe.
```python
    EEG = eegpipe.readEyeTribe('file.tsv')
```




* **readEyeTribe**: Function to read data created by Python Collect from the EyeTribe.
```python
    EEG = eegpipe.readEyeTribe('file.tsv')
```
