def get_last_stone_weights(stones: list):
    while len(stones) > 1:
        stones.sort() # (n log n) * n = n^2 log n

        # Get largest 2 stones from list
        largest = stones.pop()
        second_largest = stones.pop()

        # if equal remove both
        # if not equal, remove smallest and keep largest reduced by size of smallest
        if largest != second_largest:
            stones.append(largest - second_largest)

    return stones[0] if len(stones) == 1 else 0

weights = [7, 6, 7, 3, 2, 2]
print(get_last_stone_weights(weights))
