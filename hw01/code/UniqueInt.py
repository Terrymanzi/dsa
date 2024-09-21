# read file
# remove whitespace using strip
# convert into INT
# sort unique INT in Increasing order
import os

min_int = -(2**10-1)
max_int = (2** 10-1)

# Function to process the input file, sort, and write results
def process_file(input_file_path: str, output_file_path: str):
    # Read the input file and store valid integers
    unique_integers = read_integers_from_file(input_file_path)

    # Sort the unique integers using quicksort
    sorted_unique_integers = quick_sort(list(unique_integers))

    # Write the sorted unique integers to the output file
    write_to_file(sorted_unique_integers, output_file_path)

# Function to read integers from file and handle all conditions
def read_integers_from_file(input_file_path: str):
    unique_integers = set()
    try:
        with open(input_file_path, 'r') as file:
            for line in file:
                # Clean the line and split by whitespace
                clean_line = line.strip()

                # Skip empty or invalid lines (non-integer or more than one integer)
                if not clean_line or len(clean_line.split()) != 1:
                    continue

                # Try converting the cleaned line to an integer
                try:
                    number = int(clean_line)
                    
                    # Only add numbers within the valid range of min_int and max_int
                    if min_int <= number <= max_int:
                        unique_integers.add(number)
                    else:
                        print(f"Skipped {number}: out of range [{min_int}, {max_int}]")

                except ValueError:
                    # Skip lines that cannot be converted to an integer
                    continue
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    
    return unique_integers

# Quick sort algorithm implementation
def quick_sort(arr):
    # Base case: if the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Recursive case: apply quicksort
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Function to write sorted integers to the output file
def write_to_file(sorted_integers, output_file_path: str):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write each integer to a new line in the output file
    with open(output_file_path, 'w') as output_file:
        for integer in sorted_integers:
            output_file.write(f"{integer}\n")

# Example usage
if __name__ == "__main__":
    # Sample input and output paths
    input_path = "hw01\sample_input\small_sample_input_04.txt"
    output_path = "sample_results/sample_input_02_results.txt"

    # calling function to Process the file
    process_file(input_path, output_path)
