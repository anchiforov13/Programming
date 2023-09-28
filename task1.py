def count_ways(height):
    if height < 10 or not isinstance(height, int):
        return 0
    ways = [0] * (height + 1)
    ways[10] = 1

    consecutive_ones = 0

    for i in range(11, height + 1):
        ways[i] = 0

        for j in range(1, 4):
            if i - j * 10 >= 0:
                ways[i] += ways[i - j * 10]

        if consecutive_ones < 2:
            ways[i] += ways[i - 1]
            consecutive_ones += 1
        else:
            consecutive_ones = 0

    return ways[height]

while True:
    try:
        height = int(input("Enter an integer height: "))
        result = count_ways(height)
        print(f"Number of ways to make a tower of height {height} : {result}")
        break
    except ValueError:
        print("Invalid input. Please enter an integer value for height.")

#####