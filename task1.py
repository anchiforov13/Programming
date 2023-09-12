def count_ways(k):
    if k < 10 or not isinstance(k, int):
        return 0
    # Create a list to store the number of ways for each value from 0 to k.
    # Initialize all values to 0.
    dp = [0] * (k + 1)

    # There is only one way to make 10, which is adding 10 itself.
    dp[10] = 1

    # Initialize a variable to keep track of consecutive 1s added.
    consecutive_ones = 0

    # Iterate through all possible values from 11 to k.
    for i in range(11, k + 1):
        # Initialize the number of ways to make i.
        dp[i] = 0

        # Start with adding 10 to i and check for the valid combinations.
        for j in range(1, 4):
            if i - j * 10 >= 0:
                dp[i] += dp[i - j * 10]

        # Check if adding 1 is allowed without exceeding the consecutive ones constraint.
        if consecutive_ones < 2:
            dp[i] += dp[i - 1]
            consecutive_ones += 1
        else:
            consecutive_ones = 0  # Reset consecutive ones counter

    # If there's no way to make k with the given constraints, return 0.
    return dp[k]

while True:
    try:
        k = int(input("Enter an integer value for k: "))
        result = count_ways(k)
        print(f"Number of ways to make {k} by adding 10 and 1 with the constraint: {result}")
        break  # Exit the loop if valid input is provided
    except ValueError:
        print("Invalid input. Please enter an integer value for k.")