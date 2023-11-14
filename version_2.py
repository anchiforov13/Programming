def compose_number(n):
    if n < 10:
        return 0

    count = 0

    def explore(current_num, consecutive_ones):
        nonlocal count

        if current_num == n:
            count += 1
            return

        if current_num > n:
            return

        if consecutive_ones < 3:
            explore(current_num + 1, consecutive_ones + 1)

        explore(current_num + 10, 0)

    explore(10, 0)
    count *= 2

    return count
print(compose_number(32))