import numpy as np

arr = np.random.randint(0, 10, (5, 5)) # случайные от 0 до 10, размера (10 на 10)
max_min = []

print(arr,'\n'*2)

for i in range(0,len(arr)):
    max_min.append([max(arr[i]), min(arr[i])])
    
arr = np.hstack((arr,max_min))
print(arr)
    