# Diarization Metric in One

Support ``DER``, ``JER``, ``CDER``, ``SER`` and ``BER``

## Install

1. Clone this repo 

2. Clone metric
```
bash install.sh
```
3. Install dependencies:
``pip install  -r requirements.txt``


## Usage


Run: 

```
python run_for_all.py -r ref_rttm -s sys_rttm 
```

* ``ref_rttm`` --- the reference rttm from the ground truth
* ``sys_rttm`` --- the system or hypothesis rttm from the models' prediction

Results:
```
 collar    MS    FA    SC    OVL    DER    JER    CDER    SER    BER    ref_part    fa_dur    fa_seg    fa_mean
--------  ----  ----  ----  -----  -----  -----  ------  -----  -----  ----------  --------  --------  ---------
(value)  (val) (val)  (val) (val) (val)  (value) (value) (val) (value)   (value)    (value)   (value)   (value)
```

* ``collar``, ``MS``, ``FA``, ``SC``, ``OVL``, ``DER``, ``JER`` is from the modified dscore [URL](https://github.com/liutaocode/dscore-ovl), original is [URL](https://github.com/nryant/dscore). ``OVL`` means errors occurring in overlapped speeches.
* ``CDER`` is from [URL](https://github.com/SpeechClub/CDER_Metric)
* ``SER``, ``BER``, ``ref_part``, ``fa_dur``, ``fa_seg``, ``fa_mean`` is from [URL](https://github.com/X-LANCE/BER)

## Test Case
This case is from [VBx](https://github.com/BUTSpeechFIT/VBx)

```python run_for_all.py -r cases/callhome_part2_ref_gt.rttm -s ./cases/prediction_callhome_part2_vbx.rttm```

Results:
```
  collar    MS    FA    SC    OVL    DER    JER    CDER    SER    BER    ref_part    fa_dur    fa_seg    fa_mean
--------  ----  ----  ----  -----  -----  -----  ------  -----  -----  ----------  --------  --------  ---------
    0.00  0.14  0.00  0.07   0.15   0.21   0.34    0.28   0.37   0.37        0.37      0.00      0.00       0.00
```



## Reference
* https://github.com/nryant/dscore
* https://github.com/liutaocode/dscore-ovl
* https://github.com/SpeechClub/CDER_Metric
* https://github.com/X-LANCE/BER