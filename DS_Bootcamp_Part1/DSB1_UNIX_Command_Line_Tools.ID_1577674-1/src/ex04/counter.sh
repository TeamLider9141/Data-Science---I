#!/bin/sh

INPUT="../ex03/hh_positions.csv"
OUTPUT="hh_uniq_positions.csv"

echo '"name","count"' > "$OUTPUT"

tail -n +2 "$INPUT" \
| awk -F',' '{print $3}' \
| sort \
| uniq -c \
| sort -nr \
| awk '{
    count=$1
    name=$2
    print name","count
}' >> "$OUTPUT"

#chmod +x counter.sh
#./counter.sh
#cat hh_uniq_positions.csv
