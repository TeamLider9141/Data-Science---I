#!/bin/sh


head -n 1 ../ex01/hh.csv > hh_sorted.csv

# Qolgan qatorlarni sort qilamiz
tail -n +2 ../ex01/hh.csv | sort -t, -k2,2 -k1,1 >> hh_sorted.csv


#chmod +x sorter.sh
#./sorter.sh
#head hh_sorted.csv

