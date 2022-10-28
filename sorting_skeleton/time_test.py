import random
from itertools import repeat
from timeit import timeit
from sort import quicksort, bubblesort

num_of_elements = 1000

dict_of_lists = {
    'sorted_list': list(range(num_of_elements)),
    'reversed_list': list(range(num_of_elements,0,-1)),
    'same_elements_list': list(repeat(0, num_of_elements)),
    'random_list': random.sample(range(num_of_elements),num_of_elements)
}


###Tests

def time_test_sort(algo, repetitions, lst):
    execution_time = []
    algo_id = f'{algo}({lst})'
    for _ in range(repetitions):
        execution_time.append(timeit(algo_id, number=1, globals=globals()))
    return sum(execution_time) / repetitions
        

repetitions = 10
print(f'Average time for sorting ({repetitions} repetitions)')
for lst_name, lst in dict_of_lists.items():
    print(f'{lst_name} with:')
    for algo in ['quicksort', 'bubblesort']:
    

        print(f'        {algo} is {time_test_sort(algo, repetitions, lst):.5f} s')
    print()    
