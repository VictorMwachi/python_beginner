def binary_search(l,target,low=None,high=None):
    # l=[1,2,3,4,5,6,7,8,9,10]
    # target =8
    
    if low is None:
        low=0

    if high is None:
        high=len(l)-1

    if high<low:
        return -1

    midpoint=(low+high)//2

    if target==l[midpoint]:
        return midpoint

    elif target<l[midpoint]:
        return binary_search(l,target,low,midpoint-1)

    else:
        return binary_search(l,target,midpoint+1,high)


l=[1,2,3,4,5,6,7,8,9,10,20,30,40]
target =8

print(binary_search(l,target))