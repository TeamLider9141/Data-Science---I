#!/bin/sh

OUTPUT="hh_concatenated.csv"

# Eski faylni o‘chiramiz (agar bo‘lsa)
rm -f "$OUTPUT"

first_file=$(ls 20??-??-??.csv | head -n 1)

head -n 1 "$first_file" > "$OUTPUT"

for file in 20??-??-??.csv
do
    tail -n +2 "$file" >> "$OUTPUT"
done


#bu fayl 2-bo'lib ishga tushiriladi.

#chmod +x concatenator.sh
# ./concatenator.sh

#bu oxirida bajariladi
#diff ../ex03/hh_positions.csv hh_concatenated.csv



