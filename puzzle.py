def puzzle_solver(pieces, width, height):
    attempts = find_all_possible_next_steps([], pieces, width, height)
    while attempts:
        for placed, remaining in attempts:
            if not remaining:
                return convert_to_solution(placed)
        placed, remaining = attempts.pop()
        attempts.extend(find_all_possible_next_steps(placed, remaining, width, height))
        # print(len(attempts))


def find_all_possible_next_steps(placed, remaining, width, height):
    # print(convert_to_solution(placed))
    
    last_placed_row = len(placed) - 1
    if placed:
        last_placed_column = len(placed[-1]) - 1

    def matches(piece, placed):
        # Top left
        if not placed:
            return (piece[0][0], piece[0][1], piece[1][0]) == (None, None, None)
        piece_left = placed[-1][last_placed_column]
        # First row
        if len(placed) == 1 and len(placed[0]) < width:
            return (piece[0][0], piece[0][1], piece[1][0]) == (None, None, piece_left[1][1])
        # First column
        if len(placed[-1]) == width:
            piece_up = placed[-1][0]
            return (piece[0][0], piece[0][1], piece[1][0]) == (None, piece_up[1][1], None)
        # Rest
        piece_up = placed[-2][last_placed_column + 1]
        return (piece[0][0], piece[0][1], piece[0][0], piece[1][0]) == (piece_up[1][0], piece_up[1][1], piece_left[0][1], piece_left[1][1])
    
    candidates = [(i, piece) for (i, piece) in enumerate(remaining) if matches(piece, placed)]

    if placed and last_placed_column < width - 1:
        return [(placed[:last_placed_row] + [placed[last_placed_row] + [c]],
                 remaining[:i] + remaining[i+1:]) for (i, c) in candidates]
    
    return [(placed + [[c,]], remaining[:i] + remaining[i+1:]) for (i, c) in candidates]


def convert_to_solution(placed):
    #print(placed)
    return [[i for (first_row, second_row, i) in row] for row in placed]


puzzle = [
    ((None, 5), (None, None), 3),
    ((17, None), (None, None), 9),
    ((None, 4), (None, 5), 8),
    ((4, 11), (5, 17), 5),
    ((11, None), (17, None), 2),
    ((None, None), (None, 4), 7),
    ((5, 17), (None, None), 1),
    ((None, None), (11, None), 4),
    ((None, None), (4, 11), 6),
]
print(puzzle_solver(puzzle, 3, 3))
