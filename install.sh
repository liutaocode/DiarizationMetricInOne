#!/usr/bin/env bash 


git clone https://github.com/liutaocode/dscore-ovl
cd dscore-ovl
cd ..

git clone https://github.com/SpeechClub/CDER_Metric.git
cd CDER_Metric
git checkout b509fd71e2f2df190cf738707663e9ca4e7618c3
cd ..

git clone https://github.com/X-LANCE/BER
cd BER
git checkout 8dbb7ca9d38778fc4dd57d8ae2e8f010b3d35739
cd ..