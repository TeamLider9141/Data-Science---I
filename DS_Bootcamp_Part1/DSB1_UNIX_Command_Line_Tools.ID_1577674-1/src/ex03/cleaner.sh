#!/bin/sh

INPUT="../ex02/hh_sorted.csv"
OUTPUT="hh_positions.csv"

# Header
head -n 1 "$INPUT" > "$OUTPUT"

# Data qatorlari
tail -n +2 "$INPUT" | awk -F',' '
BEGIN { OFS="," }
{
    name=$3

    # Quote’larni olib tashlaymiz vaqtincha
    gsub(/^"/,"",name)
    gsub(/"$/,"",name)

    result=""

    if (name ~ /Junior/) result="Junior"
    if (name ~ /Middle/) {
        if (result!="") result=result"/Middle"
        else result="Middle"
    }
    if (name ~ /Senior/) {
        if (result!="") result=result"/Senior"
        else result="Senior"
    }

    if (result=="") result="-"

    $3="\""result"\""

    print
}
' >> "$OUTPUT"

# chmod +x cleaner.sh
#./cleaner.sh
# head hh_positions.csv