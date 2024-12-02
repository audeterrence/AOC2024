# Part 1 SOLUTION


with open('day2_data.txt', 'r') as file:

    safe_report = 0
    
    for line in file:
        level = list(map(int, line.split()))

        # Check if reports are either all increasing or all decreasing
        is_ordered = sum([level == sorted(level), level == sorted(level, reverse=True)]) > 0

        # Check if adjacent reports differ by at least 1 and at most 3
        is_safe = all(1 <= abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))

        # Increment safe_report only if all conditions are satisfied
        if is_ordered and is_safe:
            safe_report += 1

print(f"The number of safe reports in Part 1 is {safe_report}")

# Part 2 SOLUTION


safe_report2 = 0

with open('day2_data.txt', 'r') as file:
    for line in file:
        level = list(map(int, line.split()))

        def is_report_safe(level):
            is_ordered = sum([level == sorted(level), level == sorted(level, reverse=True)]) > 0 
            is_safe = all(1 <= abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))
            return is_ordered and is_safe

        # Check if the report is already safe
        if is_report_safe(level):
            safe_report2 += 1
        else:
            # Check if removing one level can make the report safe
            found_safe = False
            for i in range(len(level)):
                # Create a new list without the i-th level
                modified_level = level[:i] + level[i+1:]
                # Check if the modified report is safe
                if is_report_safe(modified_level):
                    found_safe = True
                    break
            
            if found_safe:
                safe_report2 += 1

print(f"The number of safe reports in Part 2 is {safe_report2}.")