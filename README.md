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

* **checkdefaultsettings**: Function that will check an input against a list and return the value from the list. 
If False is input then it returns the first element from the list as the default option.
```python
    textvalue = 'APPLES'
    textvalue = eegpipe.checkdefaultsettings(textvalue, ['oranges', 'bananas', 'apples'])
    # textvalue returns 'apples'
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

* **crushparula**: Function that creates a parula/viridis like colormap with an expanded yellow segment.
```python
    cmap = eegpipe.crushparula(256)
```

* **crushcolormap**: Function that will crush/expand segments of a colormap. The ratio option will split the colormap into segments based upon the length
of the list (3 elements splits the list into thirds) and then will expand that section based upon the value (0.5 will compress the segment by half, 
1 retains that segment as is, 2 will double the size of the segment).
```python
    cmap = eegpipe.crushcolormap(cmap='viridis', ratio=[1, 2, 4], outsize=256)
```

* **eggheadplot**: Function that will create a topographic plot using label matching on a stylized head. The style can be 'Full' or 'Outline'. To plot multiple eggheads simply provide a list of lists for the Channels, Amplitude, and Titles.
```python
    # plot a single egghead
    Channels = ['FPZ', 'F3', 'FZ', 'F4', 'T7', 'C3', 'CZ', 'C4', 'T8', 'P7', 'P3', 'PZ', 'P4', 'P8', 'OZ']
    Amplitude = [0, 3, 3, 1, 0, 8, 5, 4, 0, 2, 8, 9, 2, 2, 0]
    eegpipe.eggheadplot(Channels, Amplitude, Scale = [1, 9], TickValues=[2,8], Steps = 256, Style='Full', BrainOpacity = 0.2, Title ='Egghead', Colormap=False)
    
    # plot multiple eggheads
    Channels1 = ['FPZ', 'F3', 'FZ', 'F4', 'T7', 'C3', 'CZ', 'C4', 'T8', 'P7', 'P3', 'PZ', 'P4', 'P8', 'OZ']
    Amplitude1 = [0, 3, 3, 1, 0, 8, 5, 4, 0, 2, 8, 9, 2, 2, 0]
    Title1 = 'Egghead 1'
    Channels2 = ['FPZ', 'F3', 'FZ', 'F4', 'T7', 'C3', 'CZ', 'C4', 'T8', 'P7', 'P3', 'PZ', 'P4', 'P8', 'OZ']
    Amplitude2 = [0, 4, 4, 2, 0, 6, 6, 6, 0, 2, 7, 9, 9, 3, 0] 
    Title2 = 'Egghead 2'  
    Channels = [Channels1, Channels2]; Amplitudes = [Amplitude1, Amplitude2]; Titles = [Title1, Title2]
    eegpipe.eggheadplot(Channels, Amplitudes, Scale = [1, 9], TickValues=False, Steps = 256, Style='Full', BrainOpacity = 0.2, Title =Titles, Colormap=False)
```




General IO Function List
------------
* **readUnicornBlack**: Function to read data created by Python Collect from the g.tec Unicorn Hybrid Black.
```python
    EEG = eegpipe.readUnicornBlack('file.csv')
    eegpipe.plot([EEG.data[0]]) # show data from the first channel
```

* **readEyeTribe**: Function to read data created by Python Collect from the EyeTribe.
```python
    EEG = eegpipe.readEyeTribe('file.tsv')
```

* **mergetaskperformance**: Function that will merge behavioral data with the recorded data. This function is automatically called for 
readUnicornBlack() and readEyeTribe(). This function will alter the event codes!  
Correct stimulus events are increased by 10,000 (i.e., type 27 would become 10,027).  
Correct response events are increased by 1,190 (i.e., type 4 would become 1,194).  
Error of Commission stimulus events are increased by 50,000 (i.e., type 27 would become 50,027).  
Error of Commission response events are increased by 2190 (i.e., type 4 would become 2,194).  
Error of Omission stimulus events are increased by 60,000 (i.e., type 27 would become 60,027).  
```python
    EEG = eegpipe.mergetaskperformance(EEG, 'file.psydat')
    eegpipe.plot([EEG.events[0]]) # show all event codes
```

* **saveset**: Function to save data to a file.
```python
    eegpipe.saveset(EEG, 'file.eeg')
```

* **loadset**: Function to read in data from a file.
```python
    EEG = eegpipe.loadset('file.eeg')
```

* **writeeegtofile**: Function to save data into a generic format that can be read into MATLAB or other programs. 
```python
    eegpipe.writeeegtofile(EEG, 'file.csv')
```

* **simplemerge**: Function that merges data together.
```python
    EEG = eegpipe.simplemerge(EEG1, EEG2)
```

* **eeglabstructure**: Python class that mimics the structure of the EEG variable in EEGLAB.
```python
    EEG = eegpipe.eeglabstructure()
```
The data structure is as follows:  
EEG.filename - string filename.  
EEG.filepath - string filepath.  
EEG.data - data is stored as lists. The first index is the channel, the next index is the epoch (skipped for continous), then the point at a given time.  
EEG.pnts - number of data points (continuous data is all data points, epoched data points is points per epoch).  
EEG.times - list of time points.  
EEG.freqdata - frequency data is stored as lists. The first index is the channel, the next index is the epoch (skipped for continous), then the point at a given frequency.  
EEG.freqpnts - number of data points (continuous data is all data points, epoched data points is points per epoch).  
EEG.frequencies - list of frequency points.  
EEG.nbchan - integer of number of channels.  
EEG.channels - list of channel labels.  
EEG.trials - integer of number of epochs, 0 for continous.  
EEG.srate - float of the samples per second.  
EEG.events - list of events. This list mimics the layout of EEG.data. The first list is the event types at each time point. Subsequent lists include other information merged in.  
EEG.eventsegments - list of what each index of EEG.events contains.  
EEG.icawinv   
EEG.icasphere   
EEG.icaweights   
EEG.icaact   
EEG.reject - list of accept (0) or reject (> 0) status of each epoch.  
EEG.stderror - standard error data is stored as lists mirroring that of EEG.data.  
EEG.stddev - standard deviation data is stored as lists mirroring that of EEG.data.  
EEG.acceptedtrials - integer of number of accepted epochs.  
EEG.comments - string.   
EEG.averef - string.   
EEG.ref - string.   
EEG.history - list of what has been done to the data.  


Signal Processing Function List
------------

* **smooth**: Function that will smooth the data using a window with requested size. The approaches are: 
'hanning' (default), 'flat', 'hamming', 'bartlett', 'blackman'.
```python
    t = numpy.arange(-3,3,numpy.divide(1.0,256.0))
    x = numpy.sin(t) + numpy.multiply(numpy.random.randn(len(t)), 0.1)
    y = eegpipe.smooth(x, span=40, window='hanning')
    eegpipe.plot(x)
    eegpipe.plot(y)
```

* **minmax_scaling**: Function that rescales a vector to have a given minimum and maximimum value.
```python
    t = numpy.arange(-3,3,numpy.divide(1.0,256.0))
    x = numpy.sin(t)
    y = eegpipe.minmax_scaling(x, columns=0, min_val= -10, max_val= 10)
    eegpipe.plot(x)
    eegpipe.plot(y)
```

* **regressionbasedartifactremoval**: Function that uses Tomas Knapen's FIRDeconvolution approach to remove an artifact from a vector. Essentially a model of the artifact is built from supplied indices and then the modeled artifact is subtracted only from those periods. The approach has been slightly modified to use a scaling factor that scales the modeled artifact to each individual artifact. Therefore if an artifact is a poor fit for the model, the scaling will minimize the influence of the removal approach.  
artifactindices - a list of indices where the artifact presents (e.g. [140, 520, 890]).  
decompinterval - specifies how many seconds (float) after the index to model the artifact.  
samplerate - specifies the sampling rate (float) of the vector.  
artifactpolarity - specifies if the artifact is a positive going (+1) or negative going (-1) deflection.  
```python
    vector = eegpipe.regressionbasedartifactremoval(vector, artifactindices, decompinterval, samplerate, artifactpolarity)
```

* **extractamplitude**: Function that computes the amplitude at each channel within the given window.
```python
    outvector = eegpipe.extractamplitude(EEG, Window=[0.300, 0.700], Approach='mean')
    eegpipe.plot([outvector])
```

* **simplepsd**: Function that computes the power spectrum density. The frequencies extracted are stored in EEG.frequencies. The data is stored in EEG.freqdata. The Ceiling parameter will limit the reported data to only frequencies below the specified value.
```python
    EEG = eegpipe.simplepsd(EEG, Scale=500, Ceiling=30.0)
    eegpipe.plot(EEG.freqdata[0], EEG.frequencies) # show PSD for first channel for all epochs
```

* **simplefilter**: Function to use scipy signal processing to filter the data for all channels.
```python
    # notch filter (60 hz)
    EEG = eegpipe.simplefilter(EEG, Filter='notch', Cutoff=[60.0])
    
    # bandpass filter (also works for lowpass and highpass)
    EEG = eegpipe.simplefilter(EEG, Filter='bandpass', Design='butter', Cutoff=[0.1, 30], Order=3)
    
    # savitzky-golay smoothing filter
    EEG = eegpipe.simplefilter(EEG, Design='savitzky-golay', Order=4, Window=81)
    
    # hanning smoothing filter (also works for 'flat', 'hamming', 'bartlett', 'blackman')
    EEG = eegpipe.simplefilter(EEG, Design='hanning', Window=81)
```

* **simpleepoch**: Function that creates epochs out of continous data around the specified event types.
```python
    EEG = eegpipe.simpleepoch(EEG, Window=[-0.100, 1.000], Types=[10010, 10011, 10012, 10013])
    eegpipe.plot([EEG.data[0][0]], EEG.times) # show the first channel first epoch
    eegpipe.plot(EEG.data[0], EEG.times) # show the first channel all epochs
    eegpipe.plot([EEG.events[0][0]], EEG.times) # show the event codes for the first epoch
    eegpipe.plot(EEG.events[0], EEG.times) # show the event codes for all epochs
```

* **simplebaselinecorrect**: Function centers the data in each epoch around the mean (or median) of the window period. Window=False will use the entire epoch window.
```python
    EEG = eegpipe.simplebaselinecorrect(EEG, Window=[-0.100, 0], Approach='mean')
```

* **epochtocontinous**: Function that takes epoched data and puts it in a continous state with an optional parameter to skip any rejected epochs.
```python
    EEG = eegpipe.epochtocontinous(EEG, skipreject=True)
```

* **voltagethreshold**: Function that rejects epochs that exceed given parameters. Updates the EEG.reject status of the epoch 
with 1 for voltage threshold, 2 for voltage step, and 4 if the entire epoch contains NaN.
```python
    EEG = eegpipe.voltagethreshold(EEG, Threshold=[-100, 100], Step=100, NaN=True)
    eegpipe.plot([EEG.reject])
```

* **simplezwave**: Function that computes the mean and sd over a baseline period and then z scores the entire dataset based upon that information. Optional parameter to adjust the degrees of freedom parameter for z scoring.
```python
    EEG = eegpipe.simplezwave(EEG, BaselineWindow=[-0.100, 0], ddof=1)
```

* **simpleaverage**: Function that averages all accepted epochs for both time series (EEG.data) and frequecy series (EEG.freqdata) data. Optional parameters to use mean vs median.
```python
    ERP = eegpipe.simpleaverage(EEG, Approach='mean')
    eegpipe.plot(ERP.data, ERP.times) # show average for each channel
```

* **inspectionwindow**: Class that allows for interactively inspecting and rejecting epochs. When multiple channels are provided for a channel list they are averaged together for display purposes. 
```python
    %matplotlib qt
    inspectwin = eegpipe.inspectionwindow(); inspectwin.inspect(EEG, chanlist1=['CP1', 'CPZ', 'CP2'], chanlist2=['PZ'])
    eegpipe.plot([EEG.reject])
```


Specialty Function List
------------
* **EyeTribetousable**: Function that uses a cloud running approach to parse the usable EyeTribe data. Cloud running takes the
peaks within a given interval as 'real' data and ignores any other data points. The interval is then shifted and data is 
reextracted (an interval of 2 seconds with 0.75 percent overlap increments by 0.5 seconds).
```python
    EEG = eegpipe.EyeTribetousable(EEG, Threshold=0.85, Interval=2.0, Overlap=0.75, Peakspacing=1)
```

* **correctEyeTribe**: Function that will correct the eyetribe data to account for the distance from the screen. The data will be returned in micrometers.
```python
    EEG = eegpipe.correctEyeTribe(EEG, [0.005,0.089,-0.00000001])
```

