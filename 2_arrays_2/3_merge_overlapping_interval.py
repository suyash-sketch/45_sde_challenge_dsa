intervals = [[1,3],
             [2,6],
             [8,10],
             [15,18]]

def merge(intervals: list[list[int]]) -> list[list[int]]:

    merged_arr = []
    m = len(intervals)
    n = len(intervals[0])
    for i in range(m-1):
        for j in range(n-1):
            if intervals[i][j+1] >= intervals[i+1][j]:
                merged_arr.append([intervals[i][j],intervals[i+1][j+1]])

    for i in range(len(merged_arr)):
    return merged_arr


output = merge(intervals)
print(output)