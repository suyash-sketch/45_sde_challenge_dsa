arr = [5,4,3,2,1]
# 5,4,3,2,1
def number_of_inversions(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                count+=1
    
    return count


answer = number_of_inversions(arr)
print(answer)