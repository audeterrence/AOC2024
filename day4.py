#PART 1 SOLUTION

def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    # Function to check if the word exists starting at (x, y) in a specific direction
    def check_direction(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    # Check all positions in the grid
    for i in range(rows):
        for j in range(cols):
            # Check horizontally (right)
            if check_direction(i, j, 0, 1):
                count += 1
            # Check horizontally (left)
            if check_direction(i, j, 0, -1):
                count += 1
            # Check vertically (down)
            if check_direction(i, j, 1, 0):
                count += 1
            # Check vertically (up)
            if check_direction(i, j, -1, 0):
                count += 1
            # Check diagonally (down-right)
            if check_direction(i, j, 1, 1):
                count += 1
            # Check diagonally (up-left)
            if check_direction(i, j, -1, -1):
                count += 1
            # Check diagonally (down-left)
            if check_direction(i, j, 1, -1):
                count += 1
            # Check diagonally (up-right)
            if check_direction(i, j, -1, 1):
                count += 1

    return count

# Read the grid from day4_data.txt
def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines() if line.strip()]
    return grid

# Main execution
filename = 'day4_data.txt'
grid = read_grid_from_file(filename)

# Count occurrences of 'XMAS'
result = count_word_occurrences(grid, "XMAS")
print(f"The word 'XMAS' appears {result} times.")
