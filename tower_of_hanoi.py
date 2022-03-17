def tower_of_hanoi(n,start,end,middle):
    if n == 1:
        print('move disk %i from tower %s to tower %s' %(n,start,end))
    else:
        tower_of_hanoi(n-1,start,middle,end)
        print('move disk %i from tower %s to tower %s' %(n,start,end))
        tower_of_hanoi(n-1,middle,end,start)
        
print(tower_of_hanoi(4,'A','C','B'))
