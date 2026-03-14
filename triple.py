Given an integer array nums, return all the triplets [nums[i], nums[j],  nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.Notice that the solution set must not contain duplicate triplets.Example 1:Input:nums = [-1, 0,  1, 2, -1, -4]   Output:   [ [-1, -1, 2] , [-1, 0, 1] ]
def triple(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    print(numbers[i], numbers[j], numbers[k])


numbers = [-1,0,1,2,-1,-4]
triple(numbers)