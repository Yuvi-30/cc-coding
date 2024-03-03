def ans(x):  # create a function to find answer
    if x == 0: # return if difference is 0
        return
    else:
        p=0 
        while(2**p <= x): # until 2**p is less than x, keep incrementing p
            p+=1
        power.append(p-1) # the counter begins at 0 hence reduce one for absolute number
        x = x-2**(p-1) # reduce x so that a new 2**p-1 can be identified
        ans(x) # call the function again for recursion

t = int(input()) # testcases input
for _ in range(t):
    x = input() 
    n , k = map(int, x.split()) # deducing n and k from input
    power = [] # list in which powers are appended
    a=k-n
    ans(a) # calling function for difference
    print(len(power)) # length of list is asked
