nums = [1, 2, 3, 6, 7, 5, 7]

def findMissingRepeatingNumbers(nums:list[int]):
    n = len(nums)
    unique_nums = set()
    duplicated_num = None
    for num in nums:
        if num in unique_nums:
            duplicated_num = num
            break
        unique_nums.add(num)
    
    sum_of_nums = sum(unique_nums)
    sum_of_n_nums = n * (n + 1) // 2
    missing_num = sum_of_n_nums - sum_of_nums

    return [duplicated_num, missing_num]

answer = findMissingRepeatingNumbers(nums)
print(answer)