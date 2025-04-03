#!/bin/bash
#TO GENERATE RANDOM BATTERY LEVEL BETWEEN 0-100
battery=$(( RANDOM % 100 + 1 ))
echo "Battery: $battery%"

if [ $battery -lt 20 ]; then
  echo "Battery low! Return to base!" 
  exit 1
fi
# To Check Internet Connection
echo -n "Checking internet....... "
if ping -c 1 google.com &> /dev/null; then
  echo "OK"
else
  echo "Communication failure!"
  exit 1
fi

# If both checks passed
echo "All systems operational!"
exit 0
