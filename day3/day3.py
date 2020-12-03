with open("input.txt") as f:
    x = 0
    y = 0
    right = 1
    down = 2
    tree_counter = 0
    my_map = []
    for idx, line in enumerate(f.readlines()):
        my_map.append(line)

    map_length = len(my_map)

    while y < map_length - 1:
        y += down
        x += right
        if x > 30:
            x = x - 31

        current_row = my_map[y]
        if current_row[x] == "#":
            tree_counter += 1

print(tree_counter)
