def ins(l0):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j-=1
            l[j+1]=key
            
    return l
l=[6,3,8,2,9]
print("the sorted is ",ins(l))