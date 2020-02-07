# (n-1)! so still O(n^2)
# selection sort, each round, put one element in the correct position
def selectionSort(nums_list):
    # starting from the end- set that to the desired position
    for fill_i in range(len(nums_list)-1,0,-1):
        # trying to find the index of the largest element to go into the desired position
        max_i = 0
        for i in range(1, fill_i+1):
            if nums_list[i] > nums_list[max_i]:
                max_i = i
        # make the swap, then go to next round, going for the second largest position
        nums_list[fill_i], nums_list[max_i] = nums_list[max_i], nums_list[fill_i]
    return nums_list

A= [1,9,2,5,3,6,7,4,8,2]
print(selectionSort(A)) # [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]