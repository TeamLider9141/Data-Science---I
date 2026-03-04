#!/bin/sh

# if [ -z "$1" ]; then
#   echo "Usage: ./hh.sh \"vacancy name\""
#   exit 1
# fi

# curl -s "https://api.hh.ru/vacancies" \
#   --get \
#   --data-urlencode "text=$1" \
#   --data-urlencode "per_page=20" \
# | jq '.' > hh.json
# # 
 
 # bunisi tushunib olish maqsadida 
 # -z operator uchun ishlatsamiz tekshirishda
 # $1 bilan esa argument bo'sh kelganida false bo'ladi ekan...
#curl "https://api.hh.ru/vacancies?text=data%20scientist&per_page=20"
 




 curl -s "https://api.hh.ru/vacancies" \
  --get \
 --data-urlencode "text=$1" \
 --data-urlencode "per_page=20" \
| jq '.' > hh.json

#to run it => 
#./hh.sh "data scientist"

