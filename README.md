# LeaderSTeM-A LSTM model for dynamic leaderidentification within musical streams

PREPARING DATASET
------

We used the file 'GetFeaturesAubio.py' to get all the features from the STEM files of MUSBD18[1]. We used AUBIO [2] beattracking and pitch, amplitude extraction techniques to generate the realtime data sequence.

ARRANGING THE DATASET
------
ArrangeDataset.py - This file was used to arrange the values generated using 'GetFeaturesAubio.py'.

DATASET
------
Excel folder contains the dataset file we used. 

There columns are 16 columns
+------+-----------+-------------+--------------+---------+-----------+------------+---------+-----------+------------+--------------+----------------+-----------------+-----------+-------------+--------------+
| Time | OutputBPM | OutputPitch | OutputVolume | DrumBPM | DrumPitch | DrumVolume | BassBPM | BassPitch | BassVolume | AccompanyBPM | AccompanyPitch | AccompanyVolume | VocalsBPM | VocalsPitch | VocalsVolume |
+------+-----------+-------------+--------------+---------+-----------+------------+---------+-----------+------------+--------------+----------------+-----------------+----------
 
MODELS
------

The codes can be found in the respective folders.
3-Layers - This folder contains six different Tuning Codes. All the models were 3-Layered LSTM.  
4-Layers - This folder contains six different Tuning Codes. All the models were 4-Layered LSTM.
5-Layers - This folder contains six different Tuning Codes. All the models were 5-Layered LSTM.

Ray Tuner was used to find the optimal model. [3]
 
 REFERENCES
 -----------

[1] Rafii, Zafar, et al. "MUSDB18-a corpus for music separation." (2017).
[2] https://aubio.org/
[3] https://docs.ray.io/en/master/tune.html
