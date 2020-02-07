import datetime

# bubble sort takes O(n^2) since needs to make (n-1)! passes 
def bubbleSort(nums_list):
    # the last item would be passed so each time go to one less
    for pass_i in range(len(nums_list)-1,0,-1):
        # checking the neighbor to the right
        for i in range(pass_i):
            if nums_list[i] > nums_list[i+1]:
                nums_list[i] , nums_list[i+1] = nums_list[i+1], nums_list[i]
    return nums_list

# if during a pass, no exchange is made, that means it is sorted, so stop early
def shortBubbleSort(nums_list):
    exchanges = True
    pass_i = len(nums_list)-1
    # uses while loop instead since want to check for whether exchanges is still True
    while exchanges and pass_i > 0:
        exchanges = False
        for i in range(pass_i):
            if nums_list[i] > nums_list[i+1]:
                exchanges = True
                nums_list[i] , nums_list[i+1] = nums_list[i+1], nums_list[i]
        pass_i -=1
    return nums_list

# testing the two bubble sort algorithm
# A= [1,9,2,5,3,6,7,4,8,2]
# print(bubbleSort(A)) # [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
# print(shortBubbleSort(A)) # [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

# microseconds needed to sort an array of size n

# start = datetime.datetime.now()
# print(bubbleSort(A))
# time = datetime.datetime.now() - start
# print(time.microseconds)

# start_2 = datetime.datetime.now()
# print(shortBubbleSort(A))
# time_2 = datetime.datetime.now() - start_2
# print(time_2.microseconds)