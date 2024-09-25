#!/bin/bash
# Script to categorize based on age

age=$1

if [ $age -lt 13 ]; then
  echo "Child"
elif [ $age -lt 20 ]; then
  echo "Teen"
elif [ $age -lt 65 ]; then
  echo "Adult"
else
  echo "Elderly"
fi
