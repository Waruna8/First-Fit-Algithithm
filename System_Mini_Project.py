# University Assignment: Mini Project
# Author: S.P.S.W. Pushpakumara.
# Registration Number: 221643198

# Define memory blocks (predefined for the simulation)
memory_blocks = [100, 500, 200, 300, 600]  # Sizes of memory blocks

# Get processes as user input
print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")
print("   * EEX5563 COMPUTER ARCHITECTURE AND OPERATING SYSTEMS \n   * Mini Project\n ")
print("\n My Reminder is 0,Then the algorithm is First Fit.\n")
print("\n   * Enter the sizes of processes, separated by spaces or commas -\n\n")
process_input = input().replace(",", " ")  # Replace commas with spaces
processes = list(map(int, process_input.split()))  # Split by spaces and convert to integers

def first_fit(memory_blocks, processes):
    """
    Simulates the First Fit memory allocation algorithm.
    
    :param memory_blocks: List of memory block sizes.
    :param processes: List of process sizes to allocate.
    :return: Allocation details and updated memory blocks.
    """
    allocation = [-1] * len(processes)  # Track allocation for each process

    # Allocate each process to the first suitable memory block
    remaining_blocks = memory_blocks.copy()  # To track memory block updates accurately
    for i in range(len(processes)):
        for j in range(len(remaining_blocks)):
            if remaining_blocks[j] >= processes[i]:
                allocation[i] = j  # Allocate process i to block j
                remaining_blocks[j] -= processes[i]  # Reduce the available memory in the block
                break  # Move to the next process

    return allocation, remaining_blocks

# Perform the simulation
allocation, updated_blocks = first_fit(memory_blocks.copy(), processes)

# Display the results
print("\n   * Memory Blocks (Initial) -\n\n",    memory_blocks)
print("\n   * Processes -\n\n",    processes)
print("\n   * Allocation Results -\n\n")
remaining_blocks = memory_blocks.copy()
for i in range(len(processes)):
    if allocation[i] != -1:
        block_index = allocation[i]
        initial_remaining = remaining_blocks[block_index]  # Track the block state before allocation
        remaining_blocks[block_index] -= processes[i]
        print(f"\n   * Process {i} of size {processes[i]} allocated to block {block_index} (Remaining- {remaining_blocks[block_index]})\n")
    else:
        print(f"\n   * Process {i} of size {processes[i]} could not be allocated.\n")

print("\n   * Memory Blocks (After Allocation) -\n\n", remaining_blocks)
