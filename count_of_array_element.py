def count_element(arr):
    max= 0
    for i in arr:
        if max<i:
            max=i
    count = 0
    for j in arr:
        if j != max:
            count+=1
    return count
array_count=list(map(int,input("Enter the list:").split()
                     ))
print(count_element(array_count))
