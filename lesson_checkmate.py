def checkmate(figures):
    def add_figure(rowcol, key):
        if key not in rowcol:
            rowcol[key] = 0
        rowcol[key] += 1

    def count_pairs(rowcol):
        pairs = 0
        for key in rowcol:
            pairs += rowcol[key] - 1
        return pairs

    figures_in_row = {}
    figures_in_col = {}
    for row, col in figures:
        add_figure(figures_in_row, row)
        add_figure(figures_in_col, col)
    return count_pairs(figures_in_row) + count_pairs(figures_in_col)


figures = [[2, 2], [4, 2], [6, 2], [3, 5], [6, 5], [1, 7], [4, 7], [6, 7], [2, 8]]
print(checkmate(figures))


def checkmate2(figures):
    def add_figure(rowcol, key):
        if key not in rowcol:
            rowcol[key] = 0
        rowcol[key] += 1

    def count_pairs(rowcol):
        pairs = 0
        for key in rowcol:
            pairs += rowcol[key] - 1
        return pairs

    figures_in_di_up = {}
    figures_in_di_down = {}
    for row, col in figures:
        add_figure(figures_in_di_up, row + col)
        add_figure(figures_in_di_down, row - col)
    return count_pairs(figures_in_di_up) + count_pairs(figures_in_di_down)


figures = [[2, 2], [4, 2], [6, 2], [3, 5], [6, 5], [1, 7], [4, 7], [6, 7], [2, 8]]
print(checkmate2(figures))
