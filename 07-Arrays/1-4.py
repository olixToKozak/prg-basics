###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value',arr[-1])
print('Last value(non negative)',arr[len(arr)-1])
print('Sum',arr[0]+arr[-1])
print('Middle',arr[int(len(arr)/2)])
a=" "
for i in arr:   
    a+=str(i)+' '
print(a)