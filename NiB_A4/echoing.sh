#!/bin/bash
# Activity 1: Displaying messages

# Display the current time and date
echo "The time and date are: $(date)"

# Display the users logged into the system
echo "Let’s see who is logged into the system:"
who

# Display the home directory for the current user
echo "For $USER, the home directory is $HOME"

# Activity 2: Working with positional arguments

# Check if the correct number of arguments is provided
if [ $# -eq 2 ]; then
# Display a message with your name and money amount
     echo "My name is $1 and I have \$$2 in my wallet."
else
    # Display an error message if the number of arguments is not equal to 2
    echo "Error: Please provide exactly 2 arguments."
fi

# Activity 3: Math time

# Define mathvar1
mathvar1=$((1 + 5))

# Calculate mathvar2
mathvar2=$((mathvar1 * 20))

# Define mathvar3
mathvar3=10

# Calculate mathvar4
mathvar4=$((mathvar1 * (mathvar2 + mathvar3)))

# Display the values of all variables
echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4."

# Activity 4: More math - Working with floating-point solution

# Define a floating-point variable using bc with scale (number of decimal places)
floating=$(echo "scale=3; 4.5/1.7" | bc)

# Display the value of the floating variable
echo "Our floating variable is $floating"





