# Kadane's Algorithm

def max_sequence(arr):
    if not arr:
        return 0
    
    max_so_far = 0
    current_max = 0

    for i in range(len(arr)):
        current_max = max(0, current_max + arr[i])
        
        max_so_far = max(max_so_far, current_max)

    return max_so_far

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

# Initialize both variables with the first element
# Traverse from the second element to the end
# Decide: extend current subarray OR start fresh at this element
# Update global maximum if the current one is better