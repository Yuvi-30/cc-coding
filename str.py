def str(s1):

    c1,o1,k1,f1 = s1.count("C"),s1.count("O"),s1.count("K"),s1.count("F") # counting number of each letter

    if (c1 == o1 == k1 == f1):
        print('Yes')   
    else:
        print('No')
    
t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    str(s1)

# since the string2 contains all the 4 letters and the permutation has to be matched for whole string 2 everytime,
# we can simply match all letters individually