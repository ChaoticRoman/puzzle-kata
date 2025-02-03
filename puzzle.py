def puzzle_solver(pieces, width, height):
    attempts = find_all_possible_next_steps([], pieces, width, height)
    while attempts:
        for placed, remaining in attempts:
            if not remaining:
                return convert_to_solution(placed)
        placed, remaining = attempts.pop()
        attempts.extend(find_all_possible_next_steps(placed, remaining, width, height))
        print(len(attempts))


def find_all_possible_next_steps(placed, remaining, width, height):
    print(convert_to_solution(placed))
    # Handle first top left piece
    if not placed:
        i, top_left = [(i, piece) for (i, piece) in enumerate(remaining)
                       if piece[0][0] is None and piece[0][1] is None and piece[1][0] is None][0]
        placed = [[top_left], ]
        return [(placed, remaining[:i] + remaining[i:])]
    last_placed_row = len(placed) - 1
    last_placed_column = len(placed[-1]) - 1
    # Handle middle of first row
    if last_placed_row == 0 and last_placed_column < width - 1:
        candidates = [(i, piece) for (i, piece) in enumerate(remaining)
                      if piece[0][0] is None and piece[0][1] is None
                      and piece[1][0] == placed[0][last_placed_column][1][1] and piece[1][0] is not None]
        return [([placed[0] + [c]], [remaining[:i] + remaining[i:]]) for (i, c) in candidates]

    return []


def convert_to_solution(placed):
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
