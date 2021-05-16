#selection sort
def selection_sort(ls):
    for x in range(len(ls)):
        minVal = ls[x]
        index = 0
        for y in range(x, len(ls)):
            if ls[y] < minVal:
                index = y
                minVal = ls[y]
        if minVal != ls[x]:
            key = ls[x]
            ls[x] = minVal
            ls[index] = key

#insertion sort
def insertion_sort(ls):
    for i in range(len(ls)):
        key = ls[i]
        if i != len(ls)-1:
            if key <= ls[i+1]: continue
            else:
                ls[i] = ls[i+1]
                ls[i+1] = key
                val = ls[i]
                j = i
                while j-1>=0:
                    if val < ls[j-1]:
                        key = ls[j-1]
                        ls[j-1] = ls[j]
                        ls[j] = key
                    j-=1

#bubble sort
def bubble_sort(ls):
    for x in range(len(ls)):
        for y in range(len(ls)):
            if y != len(ls)-1:
                if ls[y] <= ls[y+1]: continue
                else:
                    key = ls[y]
                    ls[y] = ls[y+1]
                    ls[y+1] = key







