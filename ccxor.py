def find(arr, xor , sums): 
    count = 0     # Initialize a variable 'count' to keep track of the number of subarrays
    for p in (arr):
        if p < 0:
            print("0")
            return
        
    for i in range(len(arr)):   # Iterate over all possible starting indices i in the array

        # Initialize variables 'xor_sum' and 'sum_sum' for calculating XOR and SUM of subarrays
        xor_sum = 0
        sum_sum = 0
        
        for j in range(i,len(arr)): # Iterate over all possible ending indices j in the array, starting from i to end of arr
            #Updating xor_sum and sum_sum 
            xor_sum ^= arr[j]
            sum_sum += arr[j]
            
            if xor_sum == xor and sum_sum == sums and i!=j : # Check if the current subarray satisfies the given xor and sums conditions
                count+=1 # If yes increment the count
    print(count)

    
t = int(input())
for _ in range(t):

    n = int(input())  # Input: Length of the array
    
    x = input()  # Input: Array elements as a space-separated string
    
    arr = list(map(int, x.split())) # Convert x to a list of integers
    
    y= input() # Input: Target XOR and SUM values
    xor,sums = map(int, y.split()) # Convert y to integers
    
    # Call the 'find' function with the array and target values for test case
    find(arr,xor,sums) 