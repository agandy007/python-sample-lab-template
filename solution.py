# Import necessary libraries

# Define the function to calculate speeds
def calculate_speeds(distances, times):
    # TODO: Implement the function to calculate speeds
    # 1. Initialize an empty list to store speeds
    speeds = []
    # 2. Loop over the range of distances (or times)
    for i in range(len(distances)):
        # 3. For each index, calculate speed as distance divided by time
        speed = distances[i] / times[i]
        # 4. Append the calculated speed to the speeds list
        speeds.append(speed)
    # 5. Return the list of speeds
    return speeds

if __name__ == "__main__":
    # Hardcoded data for distances and times
    distances = [10, 15, 17, 26, 30, 45, 50, 60, 70, 80]
    times = [0.3, 0.47, 0.55, 1.20, 1.5, 2.5, 3.0, 3.5, 4.0, 4.5]
    
    # Calculate speeds using the function
    speeds = calculate_speeds(distances, times)
    
    # Print the calculated speeds
    print(speeds)
