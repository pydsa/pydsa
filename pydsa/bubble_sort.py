def bubble_sort(a):
    for k in range(len(a)):
        flag = 0
        for i in range(0, len(a)-k-1):
            if(a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                flag = 1
        if(flag == 0):
            break
    return a
