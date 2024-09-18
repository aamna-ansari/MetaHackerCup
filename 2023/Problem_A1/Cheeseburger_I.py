def main():
    input_file = 'D:\\MetaHackerCup\\2023\\Problem_A1\\Input.txt'
    output_file = 'D:\\MetaHackerCup\\2023\\Problem_A1\\Output.txt'

    with open(input_file, 'r') as file:
        T = int(file.readline().strip())  # Read the number of test cases
        results = []

        for t in range(1, T + 1):  # Iterate over each test case
            S, D, K = map(int, file.readline().split())

            buns = 2 * (S + D)  # Calculate total number of buns
            patties = S + 2 * D  # Calculate total number of patties

            # Check if we have enough buns and patties
            if buns >= K + 1 and patties >= K:
                results.append(f"Case #{t}: YES")
            else:
                results.append(f"Case #{t}: NO")

    with open(output_file, 'w') as file:
        file.write("\n".join(results))

# Call the main function
main()

        