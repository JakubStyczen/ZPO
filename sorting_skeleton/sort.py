# <Jakub> <Styczeń>, <411535>

def quicksort(l: list) -> list:
    lst = l[:]
    if len(lst) > 0:
        current_quicksort(lst, 0, len(lst) - 1)
    return lst

def current_quicksort(lst: list, start: int, stop: int) ->  list:
    i, j = start, stop
    pivot = lst[(start + stop)//2]
    while i < j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    if start < j:
        current_quicksort(lst, start, j)
    if i < stop: 
        current_quicksort(lst, i, stop)
    return lst


def bubblesort(l: list) -> list:
    lst = l[:]
    return current_bubblesort(lst)
    

def current_bubblesort(lst: list) -> None:
    n = len(lst)
    num_of_comp = 0
    while n > 1:
        swaped = False
        for i in range(1, n):
            num_of_comp += 1
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                swaped = True
            
        if not swaped:
            break
            
        n -= 1
    return lst, num_of_comp
