
MIN_LEN = 4
g_puzzle = []
g_puzzle_t = []
g_dictword = []
g_dir = ['n','e','s','w']
g_incr = {                                     #use dictionary to determine the movement
      'n': (-1,0),
      'e': (0,1),
      's': (1,0),
      'w': (0,-1)
    }

g_puzzle = [
        ['J', 'A', 'N', 'S', 'N', 'Y', 'E', 'P', 'A', 'R', 'G', 'X'], 
        ['I', 'P', 'V', 'O', 'O', 'R', 'A', 'N', 'G', 'E', 'V', 'T'], 
        ['W', 'P', 'K', 'V', 'L', 'R', 'P', 'M', 'E', 'C', 'U', 'A'], 
        ['I', 'L', 'U', 'E', 'R', 'E', 'M', 'A', 'A', 'M', 'N', 'G'], 
        ['K', 'E', 'M', 'D', 'U', 'B', 'M', 'I', 'P', 'A', 'I', 'A'], 
        ['S', 'O', 'O', 'U', 'S', 'E', 'Y', 'R', 'N', 'A', 'G', 'L'], 
        ['N', 'U', 'J', 'Y', 'M', 'U', 'M', 'A', 'E', 'M', 'Y', 'R'], 
        ['P', 'P', 'B', 'E', 'L', 'L', 'B', 'I', 'J', 'T', 'H', 'A'], 
        ['P', 'V', 'G', 'N', 'N', 'B', 'M', 'J', 'F', 'H', 'A', 'W'], 
        ['J', 'X', 'H', 'O', 'F', 'A', 'M', 'S', 'X', 'R', 'M', 'W'], 
        ['D', 'P', 'W', 'I', 'P', 'P', 'X', 'F', 'G', 'Z', 'Z', 'P'], 
        ['M', 'E', 'B', 'Q', 'W', 'Z', 'C', 'M', 'M', 'S', 'J', 'L']
    ]

g_dictword = ['APPLE', 'BANANA', 'BLUEBERRY', 'GRAPE', 'KIWI', 'LEMON', 'LIME', 'ORANGE', 'PAPAYA', 'WATERMELON']

# print the puzzle on the console
# with 2 whitespaces between each letter.
def print_puzzle(p_puzzle):
    for row in p_puzzle:
        print('  '.join(row))

# show given word in the puzzle,
# with each letter prefixed with '*'
def show_word(p_y, p_x, p_dir, p_word):
    print('{} @{},{} Direction:{}'.format(p_word, p_y, p_x, p_dir))
    # clone the puzzle
    puz = [x[:] for x in g_puzzle]
    locs = get_all_locations(p_y, p_x, p_dir)
    for y,x in locs[:len(p_word)]:
        puz[y][x] = '*' + puz[y][x]
    print_puzzle(puz)

# return the next valid location as (row,col) in 
# the given direction and starting position, (-1,-1) otherwise
def get_next_location(p_y, p_x, p_dir):
    y_incr, x_incr = g_incr[p_dir]
    new_y = p_y + y_incr
    new_x = p_x +x_incr
    if new_y >= 0 and new_y < len(g_puzzle) and new_x >= 0 and new_x < len(g_puzzle[0]): 
     return (new_y,new_x)
    return(-1,-1)

# return all locations as list of (row,col)
# in the given direction and starting position (p_y,p_x)
def get_all_locations(p_y, p_x, p_dir):
    locs = []
    y,x = p_y,p_x
    while y != -1:
        locs.append( (y,x) )
        y,x = get_next_location(y,x,p_dir)
    return locs

# return all letters as a string 
# in the given direction and starting position (p_y,p_x) 
def get_all_letters(p_y, p_x, p_dir):
    locs = get_all_locations(p_y,p_x,p_dir)
    letters =""
    for y,x in locs:
        letters += g_puzzle[y][x]
    return letters

# search for hidden word in the given direction
# at location (p_y,p_x)
def search_word(p_y, p_x, p_dir, p_min=MIN_LEN):
    letters = get_all_letters(p_y,p_x,p_dir)
    for sz in range(4,len(letters)+1):
      word = letters[:sz]
      if word in g_dictword:
        show_word(p_y,p_x,p_dir,word)
    return

def transpose_puzzle():
    # clone the puzzle
    ret = [x[:] for x in g_puzzle]
    # return the puzzle in transpose format
    return list(zip(*ret))

def main():
    sz_across = len(g_puzzle[0])
    sz_down = len(g_puzzle)
    for row in range(sz_down):
        for col in range(sz_across):
            for dir in g_dir:
                search_word(row, col, dir)


if __name__ == '__main__':
    print_puzzle(g_puzzle)
    main()