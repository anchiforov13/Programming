def count_all_ways(tower_height):
    if tower_height < 10 or not isinstance(tower_height, int):
        return 0
    all_ways = [0] * (tower_height + 1)
    all_ways[10] = 1

    ones_in_a_row = 0

    for i in range(11, tower_height + 1):
        all_ways[i] = 0

        for y in range(1, 4):
            if i - y * 10 >= 0:
                all_ways[i] += all_ways[i - y * 10]

        if ones_in_a_row < 2:
            all_ways[i] += all_ways[i - 1]
            ones_in_a_row += 1
        else:
            ones_in_a_row = 0

    return all_ways[tower_height]

while True:
    try:
        tower_height = int(input("Enter an integer height: "))
        res = count_all_ways(tower_height)
        print(f"Number of ways to make a tower of height {tower_height} : {2*res}")
        break
    except ValueError:
        print("Invalid input. Please make the height an integer value.")