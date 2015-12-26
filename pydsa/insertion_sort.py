def insertion_sort(a):
    for i in range(1, len(a)):
            element = a[i]
            j = i
            while j > 0 and a[j-1] > element:
                a[j] = a[j-1]
                j = j - 1
            a[j] = element
    return a
