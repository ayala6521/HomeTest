import random

vis = []


def create_minesweeper_map(grid_size, mines_number):
    arr = [[0 for row in range(grid_size)] for column in range(grid_size)]  # A matrix (list of lists)
    for bomb in range(mines_number):
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        arr[y][x] = 'X'
        # when y == 0
        if x == 0:  # left side
            if arr[y][x + 1] != 'X':
                arr[y][x + 1] += 1
        if 1 <= x <= grid_size - 2:
            if arr[y][x - 1] != 'X':
                arr[y][x - 1] += 1
            if arr[y][x + 1] != 'X':
                arr[y][x + 1] += 1
        if x == grid_size - 1:  # right side
            if arr[y][x - 1] != 'X':
                arr[y][x - 1] += 1
        # when 1<= y <= grid_size-1
        if 1 <= y <= grid_size - 1:
            # left up
            if 1 <= x <= grid_size - 1:
                if arr[y - 1][x - 1] != 'X':
                    arr[y - 1][x - 1] += 1
            # center up
            if 0 <= x <= grid_size - 1:
                if arr[y - 1][x] != 'X':
                    arr[y - 1][x] += 1
            # right up
            if 0 <= x <= grid_size - 2:
                if arr[y - 1][x + 1] != 'X':
                    arr[y - 1][x + 1] += 1
        # when 0<= y <= grid_size-2
        if 0 <= y <= grid_size - 2:
            # left down
            if 1 <= x <= grid_size - 1:
                if arr[y + 1][x - 1] != 'X':
                    arr[y + 1][x - 1] += 1
            # center down
            if 0 <= x <= grid_size - 1:
                if arr[y + 1][x] != 'X':
                    arr[y + 1][x] += 1
            # right down
            if 0 <= x <= grid_size - 2:
                if arr[y + 1][x + 1] != 'X':
                    arr[y + 1][x + 1] += 1
    return arr


def create_player_map(grid_size):
    arr = [['-' for row in range(grid_size)] for column in range(grid_size)]
    return arr


# print the current map to the user screen
def display_map(map):
    n = len(map)
    st = "   "
    for i in range(n):  # print the numbers of the grid on top
        st = st + "     " + str(i + 1)
    print(st)

    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + " _____"
            print(st)

        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")

        st = " " + f'{str(r + 1):2}' + "  "
        for col in range(n):
            st = st + "|  " + str(map[r][col]) + "  "
        print(st + "|")

        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')

    print()


# check all the neighbours of the selected cell and open others cells according to it
def neighbours(r, col, player_map, minesweeper_map, grid_size):
    global vis

    # If the cell already not visited
    if [r, col] not in vis:

        # Mark the cell visited
        vis.append([r, col])

        # If the cell is zero-valued
        if minesweeper_map[r][col] == 0:

            # Display it to the user
            player_map[r][col] = minesweeper_map[r][col]

            # Recursive calls for the neighbouring cells
            if r > 0:
                neighbours(r - 1, col, player_map, minesweeper_map, grid_size)
            if r < grid_size - 1:
                neighbours(r + 1, col, player_map, minesweeper_map, grid_size)
            if col > 0:
                neighbours(r, col - 1, player_map, minesweeper_map, grid_size)
            if col < grid_size - 1:
                neighbours(r, col + 1, player_map, minesweeper_map, grid_size)
            if r > 0 and col > 0:
                neighbours(r - 1, col - 1, player_map, minesweeper_map, grid_size)
            if r > 0 and col < grid_size - 1:
                neighbours(r - 1, col + 1, player_map, minesweeper_map, grid_size)
            if r < grid_size - 1 and col > 0:
                neighbours(r + 1, col - 1, player_map, minesweeper_map, grid_size)
            if r < grid_size - 1 and col < grid_size - 1:
                neighbours(r + 1, col + 1, player_map, minesweeper_map, grid_size)

                # If the cell is not zero-valued
        if minesweeper_map[r][col] != 0:
            player_map[r][col] = minesweeper_map[r][col]


# Function to check for completion of the game
def check_over(player_map, grid_size, mines_number):
    # Count of all numbered values
    count = 0
    # Loop for checking each cell in the grid
    for row in player_map:
        for cell in row:
            # If cell not empty or flagged
            if cell != '-' and cell != 'F':
                count = count + 1
    # Count comparison
    if count == grid_size * grid_size - mines_number:
        return True
    else:
        return False


def game():
    game_status = True
    while game_status:
        print("Enter board size (N) and number of mines (B)")
        try:
            grid_size = int(input("N: "))
            mines_number = int(input("B: "))
        except ValueError:
            print("Your input is wrong")
            return
        minesweeper_map = create_minesweeper_map(grid_size, mines_number)
        player_map = create_player_map(grid_size)
        score = 0
        display_map(player_map)  # show the map to the user
        while True:
            if check_over(player_map, grid_size, mines_number) == False:
                print("Enter your cell you want to open")
                try:
                    user_input = input(f"column (1 to {grid_size}) and row (1 to {grid_size}) :").split(" ")
                    x = int(user_input[0]) - 1  # 0 based indexing
                    y = int(user_input[1]) - 1  # 0 based indexing
                except ValueError:
                    print("Your input is wrong")
                    return
                if len(user_input) > 2 and (user_input[2] == 'F' or user_input[2] == 'f'):
                    player_map[y][x] = 'F'  # mark the cell
                    display_map(player_map)
                elif (minesweeper_map[y][x] == 'X'):
                    # print("Game Over!")
                    display_map(minesweeper_map)
                    print("Game Over!")
                    print("Your score: ", score)
                    game_status = False
                    break
                else:
                    neighbours(y, x, player_map, minesweeper_map, grid_size)
                    player_map[y][x] = minesweeper_map[y][x]
                    display_map(player_map)
                    score += 1
            else:
                display_map(player_map)
                print("You have Won!")
                print("Your score: ", score)
                game_status = False
                break


# Start of Program
if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
