#!/bin/bash
# temperature in California.

# Take the first positional argument as temperature
temp=$1

# Nested if statements
if [ $temp -lt 55 ]; then
  echo "Freezing"
elif [ $temp -gt 55 ] && [ $temp -lt 67 ]; then
  echo "Cold"
elif [ $temp -ge 67 ] && [ $temp -lt 85 ]; then
  echo "Nice"
else
  echo "Hot"
fi
