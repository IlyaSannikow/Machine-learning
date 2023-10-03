import numpy as np

arr = np.arange(1,51)

arr_even = []
arr_not_even = []

for i in range(0,len(arr)):
    if arr[i]%2==0:
        arr_even.append(arr[i])
    else:
        arr_not_even.append(arr[i])

arr_even = np.array(arr_even)
arr_even = arr_even.reshape(5,5)

arr_not_even = np.array(arr_not_even)
arr_not_even = arr_not_even.reshape(5,5)

print(arr_even, '\n'*2)
print(arr_not_even, '\n'*2)

composition = np.dot(arr_even, arr_not_even)
composition = np.array(composition)

print(composition, '\n'*2)

inverse_arr = np.linalg.pinv(composition)

print(inverse_arr)



