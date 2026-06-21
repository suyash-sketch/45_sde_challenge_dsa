arr = [1,2,3]

def nextPermutation(nums : list[int]):
    nums[-1], nums[0] = nums[0],nums[-1]
    print(nums)

nextPermutation(arr)