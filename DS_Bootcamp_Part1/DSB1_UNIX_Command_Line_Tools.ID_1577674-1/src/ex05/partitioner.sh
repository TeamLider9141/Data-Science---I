#!/bin/sh

INPUT="../ex03/hh_positions.csv"

# Headerni saqlab olamiz
HEADER=$(head -n 1 "$INPUT")

# Data qatorlari
tail -n +2 "$INPUT" | while IFS= read -r line
do
    # created_at ustunini olish (2-ustun)
    created_at=$(echo "$line" | awk -F',' '{print $2}')
    
    # Quote olib tashlash
    created_at=$(echo "$created_at" | tr -d '"')
    
    # Sana qismini olish (YYYY-MM-DD)
    date_part=$(echo "$created_at" | cut -d'T' -f1)

    FILE="$date_part.csv"

    # Agar fayl yo‘q bo‘lsa, header yozamiz
    if [ ! -f "$FILE" ]; then
        echo "$HEADER" > "$FILE"
    fi

    # Qatorni yozamiz
    echo "$line" >> "$FILE"

done

# bu fayl 1-run qilinishi kerak
#chmod +x partitioner.sh
#./partitioner.sh