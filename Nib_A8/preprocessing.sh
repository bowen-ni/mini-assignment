#!/bin/bash

# Remove rows with missing values
echo "Removing rows with missing values..."
awk -F',' 'NF == 16' AB_NYC_2019.csv > cleaned_AB_NYC_2019.csv

# Remove duplicate rows
echo "Removing duplicate entries..."
awk '!seen[$0]++' cleaned_AB_NYC_2019.csv > deduplicated_AB_NYC_2019.csv

# Handle outliers in the price column
echo "Identifying and handling outliers..."
mean=$(awk -F',' '{sum+=$10; count++} END {print sum/count}' deduplicated_AB_NYC_2019.csv)
std_dev=$(awk -F',' -v mean=$mean '{sum+=($10-mean)^2} END {print sqrt(sum/NR)}' deduplicated_AB_NYC_2019.csv)
awk -F',' -v mean=$mean -v std_dev=$std_dev '($10 >= mean - 3*std_dev) && ($10 <= mean + 3*std_dev)' deduplicated_AB_NYC_2019.csv > final_AB_NYC_2019.csv

echo "Preprocessing complete. Final dataset saved as final_AB_NYC_2019.csv."

