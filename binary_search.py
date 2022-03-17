def binary_search(data, target, low, high):
    if low > high:
        return False # target not in the data
    else:
        mid = (low + high) // 2 
        if target == data[mid]: # found match!
            return True
        elif target < data[mid]: # if target is smaller recur of the portion from left to middle
            return binary_search(data, target, low, mid-1)
        else: # if target is bigger recur of the portion from middle to right
            return binary_search(data, target, mid+1, high)
    
data = [2,5,7,10,15,20]
print(binary_search(data,, 0, len(data)-1))
