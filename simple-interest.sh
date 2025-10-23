#!/bin/bash

# Simple Interest Calculator
# Coursera Shell Scripting Course

echo "========================================="
echo "      SIMPLE INTEREST CALCULATOR"
echo "========================================="

# Function to calculate simple interest
calculate_simple_interest() {
    local principal=$1
    local rate=$2
    local time=$3
    
    # Simple Interest formula: SI = (P * R * T) / 100
    local interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)
    local total_amount=$(echo "scale=2; $principal + $interest" | bc)
    
    echo "========================================="
    echo "           CALCULATION RESULTS"
    echo "========================================="
    echo "Principal Amount: \$$principal"
    echo "Rate of Interest: $rate% per year"
    echo "Time Period: $time years"
    echo "-----------------------------------------"
    echo "Simple Interest: \$$interest"
    echo "Total Amount: \$$total_amount"
    echo "========================================="
}

# Function for input validation
validate_input() {
    local input=$1
    local type=$2
    
    # Check if input is numeric and positive
    if ! [[ "$input" =~ ^[0-9]+\.?[0-9]*$ ]] || (( $(echo "$input <= 0" | bc -l) )); then
        echo "Error: Please enter a valid positive $type"
        return 1
    fi
    return 0
}

# Main script execution
main() {
    echo ""
    echo "Please enter the following details:"
    
    # Get principal amount with validation
    while true; do
        read -p "Enter Principal Amount (\$): " principal
        if validate_input "$principal" "principal amount"; then
            break
        fi
    done
    
    # Get interest rate with validation
    while true; do
        read -p "Enter Rate of Interest (% per year): " rate
        if validate_input "$rate" "interest rate"; then
            break
        fi
    done
    
    # Get time period with validation
    while true; do
        read -p "Enter Time Period (years): " time
        if validate_input "$time" "time period"; then
            break
        fi
    done
    
    # Calculate and display results
    calculate_simple_interest "$principal" "$rate" "$time"
}

# Check if bc calculator is installed
if ! command -v bc &> /dev/null; then
    echo "Error: 'bc' calculator is required but not installed."
    echo "Please install it using:"
    echo "  Ubuntu/Debian: sudo apt-get install bc"
    echo "  CentOS/RHEL: sudo yum install bc"
    echo "  macOS: brew install bc"
    exit 1
fi

# Run the main function
main
