t = int(input()) # testcases
for _ in range(t):
    n = int(input())     # Input: Length of the sequence
    # Input: Sequence as a space-separated string, convert to a list of integers
    x = input()
    a = list(map(int, x.split()))
    b = 0 # Initialize a variable to 0

    for j in range(2): #For 2 trips possible
        for i in a: # Itratrate each element in way it is received
            if b+1 == i: # Checking if next block is suitable for stairs
                b+=1 # If found: increment to check for next block

    # If at last iteration height of staircase is matched forming a proper staircase:
    if b==n: 
        print("Yes")
    else:
        print("No")