import re

def process_memory_part1(corrupted_memory):
    # Regular expression to find mul instructions
    mul_pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'

    total_sum = 0

    # Find all mul instructions in the corrupted memory
    for match in re.finditer(mul_pattern, corrupted_memory):
        x, y = map(int, match.groups())
        total_sum += x * y

    return total_sum

def process_memory_part2(corrupted_memory):
    # Regular expression to find mul instructions
    mul_pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'

    # Start with mul instructions enabled
    mul_enabled = True
    total_sum = 0

    # Split the input into tokens based on do/don't instructions
    tokens = re.split(f'({do_pattern}|{dont_pattern})', corrupted_memory)

    for token in tokens:
        token = token.strip()
        
        if token == 'do()':
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        else:
            # Find all mul instructions in the current token
            for match in re.finditer(mul_pattern, token):
                if mul_enabled:
                    x, y = map(int, match.groups())
                    total_sum += x * y

    return total_sum

# Read the input from the file
with open('day3_data.txt', 'r') as file:
    corrupted_memory = file.read()

# Process for Part 1
part1_result = process_memory_part1(corrupted_memory)
print(f"Part 1 Result: {part1_result}")

# Process for Part 2
part2_result = process_memory_part2(corrupted_memory)
print(f"Part 2 Result: {part2_result}")