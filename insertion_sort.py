# insertion sort, maintains a sorted subvector and each new item is inserted into the subvector in the correct position, working toward the entier array
# still O(n^2) since still take n-1! steps

def insertionSort(nums_list):
    for sub_end_i in range(1,len(nums_list)):
        number = nums_list[sub_end_i]
        position = sub_end_i
        # instead of a for loop, use a while so it would stop when nums_list[position-1] is no longer greater than the number
        while position > 0 and nums_list[position-1]>number:
            # if the value at position-1 is greater than number, shift that value right one position
            nums_list[position] = nums_list[position-1]
            # decrease the index by 1 for the next round
            position -=1
        nums_list[position] = number
            
    return nums_list

def gapInsertionSort(nums_list,start_i,gap):
    sub_array=[]
    for num in range(start_i,len(nums_list),gap):
        sub_array.append(nums_list[num])
    for sub_end_i in range(1,len(sub_array)):
        number = sub_array[sub_end_i]
        position = sub_end_i
        # instead of a for loop, use a while so it would stop when nums_list[position-1] is no longer greater than the number
        while position > 0 and sub_array[position-1]>number:
            # if the value at position-1 is greater than number, shift that value right one position
            sub_array[position] = sub_array[position-1]
            # decrease the index by 1 for the next round
            position -=1
        sub_array[position] = number
            
    return sub_array

def shellSort(nums_list,gap):
    num_sub_arrays = len(nums_list)//gap
    for start_num in range(num_sub_arrays):
        # start_num : 0, 1, 2
        sorted_sub_array=gapInsertionSort(nums_list,start_num,gap)
        for j in range(len(sorted_sub_array)):
            # j = 0, 1 , 2
            nums_list[start_num+(gap*j)] = sorted_sub_array[j]
    # then do with gap of 1
    return gapInsertionSort(nums_list,0,1)

# automatically choose gap, use this
def halvenShellSort(nums_list):
    gap = len(nums_list)//2
    num_sub_arrays = len(nums_list)//gap
    while gap > 0:
        for start_num in range(num_sub_arrays):
            sorted_sub_array = gapInsertionSort(nums_list,start_num,gap)
            for j in range(len(sorted_sub_array)):
                nums_list[start_num+(gap*j)] = sorted_sub_array[j]
        #print ("After insertion sort with gap of ",gap,". The list is", nums_list)
        gap = gap//2

    return nums_list

# testing insertionSort
A= [1,9,2,5,3,6,7,4,8,2]
print(insertionSort(A)) # [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

# testing halvenShellSort
print(halvenShellSort(A))