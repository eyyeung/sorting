# recursive call to split vector in half and then order them, and combine

def mergeSort(nums_list):
    # base case is if the len(subarray) <=1
    if len(nums_list) > 1:
        #print("Splitting ", nums_list)
        # splitting into left an right
        mid_i = len(nums_list)//2
        left = nums_list[:mid_i]
        right = nums_list[mid_i:]
        # recursive call until cannot split anymore (len(subarray<=1))
        mergeSort(left)
        mergeSort(right)

        # this is to order and combine them back
        left_i = 0
        right_i = 0
        nums_i = 0
        # print("left: ",left,"right: ",right)
        # checking left vs right, then put the greater one in the correct position
        while left_i < len(left) and right_i < len(right):
            #print(left_i,right_i,nums_i,"and")
            if left[left_i] < right[right_i]:
                nums_list[nums_i] = left[left_i]
                left_i +=1
                #print(nums_list)
            else:
                nums_list[nums_i] = right[right_i]
                right_i +=1
                #print(nums_list)
            nums_i += 1
        # put the smaller number in the correct position
        while left_i < len(left):
            #print(left_i,right_i,nums_i,"left")
            nums_list[nums_i] = left[left_i]
            left_i += 1
            nums_i += 1
            #print(nums_list)

        while right_i < len(right):
            #print(left_i,right_i,nums_i,"right")
            nums_list[nums_i] = right[right_i]
            right_i += 1
            nums_i += 1
            #print(nums_list)
        #print("Merging ",nums_list)
    return nums_list

A= [1,9,2,5,3,6,7,4,8,2]
print(mergeSort(A)) #[1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
