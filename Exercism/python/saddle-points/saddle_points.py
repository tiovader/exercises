def saddle_points(matrix):
    if len(set((len(row) for row in matrix))) > 1:
        raise ValueError("Rows have different lengths.")

    return [
        {'row': x+1, 'column': y+1} for x, row in enumerate(matrix)
        for y, value in enumerate(row) if value == max(matrix[x])
        and value == min(list(zip(*matrix))[y])
    ]
